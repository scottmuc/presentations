{
  description = "An empty flake template that you can adapt to your own environment";

  inputs = {
    nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0";
    uv2nix.url = "github:pyproject-nix/uv2nix";
    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  # Flake outputs
  outputs =
    {
      self,
      nixpkgs,
      uv2nix,
      pyproject-nix,
      pyproject-build-systems,
      ...
    }@inputs:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config = {
          allowUnfreePredicate =
            pkg:
            builtins.elem (nixpkgs.lib.getName pkg) [
              "vault"
            ];
        };
      };

      workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };
      overlay = workspace.mkPyprojectOverlay { sourcePreference = "wheel"; };
      python = nixpkgs.lib.head (
        pyproject-nix.lib.util.filterPythonInterpreters {
          inherit (workspace) requires-python;
          inherit (pkgs) pythonInterpreters;
        }
      );
      pythonBase = pkgs.callPackage pyproject-nix.build.packages {
        inherit python;
      };
      pythonSet = pythonBase.overrideScope (
        nixpkgs.lib.composeManyExtensions [
          pyproject-build-systems.overlays.wheel
          overlay
        ]
      );
      virtualenv = pythonSet.mkVirtualEnv "git-workshop" workspace.deps.default;
      editableOverlay = workspace.mkEditablePyprojectOverlay {
        # Use environment variable pointing to editable root directory
        root = "$REPO_ROOT";
        # Optional: Only enable editable for these packages
        # members = [ "hello-world" ];
      };

      editablePythonSet = pythonSet.overrideScope editableOverlay;

      virtualenv2 = editablePythonSet.mkVirtualEnv "git-workshop" workspace.deps.all;

      # The systems supported for this flake's outputs
      supportedSystems = [
        "x86_64-linux" # 64-bit Intel/AMD Linux
        "aarch64-linux" # 64-bit ARM Linux
        "aarch64-darwin" # 64-bit ARM macOS
      ];

      # Helper for providing system-specific attributes
      forEachSupportedSystem =
        f:
        inputs.nixpkgs.lib.genAttrs supportedSystems (
          system:
          f {
            inherit system;
            # Provides a system-specific, configured Nixpkgs
            pkgs = import inputs.nixpkgs {
              inherit system;
              # Enable using unfree packages
              config.allowUnfree = true;
            };
          }
        );
    in
    {
      # Development environments output by this flake

      # To activate the default environment:
      # nix develop
      # Or if you use direnv:
      # direnv allow
      devShells = forEachSupportedSystem (
        { pkgs, system }:
        {
          # Run `nix develop` to activate this environment or `direnv allow` if you have direnv installed
          default = pkgs.mkShellNoCC {
            # The Nix packages provided in the environment
            packages = [
              # Add the flake's formatter to your project's environment
              self.formatter.${system}

              virtualenv2
              pkgs.uv
            ];

            # Set any environment variables for your development environment
            env = {
              UV_PYTHON_DOWNLOADS = "never";
            };

            # Add any shell logic you want executed when the environment is activated
            shellHook = "";
          };
        }
      );

      packages.${system} = {
        ci-image = pkgs.dockerTools.buildLayeredImage {
          name = "infrastructure-ci";
          tag = "latest";
          contents = [
            pkgs.dockerTools.usrBinEnv # provides /usr/bin/env
            (pkgs.buildEnv {
              name = "ci-env";
              paths = [
                pkgs.bashNonInteractive
                pkgs.coreutils # provides ls, env, cat, etc...
                pkgs.findutils # provides find and xargs
                pkgs.flake-checker
                pkgs.git
                pkgs.nixfmt
                pkgs.shellcheck
                virtualenv
              ];
            })
          ];
          config = {
            Env = [
              "UV_PYTHON_DOWNLOADS=never"
            ];
          };
        };
      };

      # Nix formatter

      # This applies the formatter that follows RFC 166, which defines a standard format:
      # https://github.com/NixOS/rfcs/pull/166

      # To format all Nix files:
      # git ls-files -z '*.nix' | xargs -0 -r nix fmt
      # To check formatting:
      # git ls-files -z '*.nix' | xargs -0 -r nix develop --command nixfmt --check
      formatter = forEachSupportedSystem ({ pkgs, ... }: pkgs.nixfmt-rfc-style);
    };
}
