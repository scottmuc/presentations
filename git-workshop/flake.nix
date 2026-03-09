{
  description = "An empty flake template that you can adapt to your own environment";

  # Flake inputs
  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0"; # Stable Nixpkgs (use 0.1 for unstable)

  # Flake outputs
  outputs =
    { self, nixpkgs, ... }@inputs:
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

              pkgs.python3
              pkgs.python3Packages.pip
              pkgs.python3Packages.virtualenv
            ];

            # Set any environment variables for your development environment
            env = { };

            # Add any shell logic you want executed when the environment is activated
            shellHook = "";
          };
        }
      );

      packages = {
        ci-image = pkgs.dockerTools.buildLayeredImage {
          name = "infrastructure-ci";
          tag = "latest";
          contents = [
            pkgs.dockerTools.caCertificates # installs CAs into expected /etc/ssl/certs
            pkgs.dockerTools.usrBinEnv # provides /usr/bin/env
            pkgs.dockerTools.fakeNss # provides /etc/passwd and /etc/group so that getpwuid() works
            (pkgs.buildEnv {
              name = "ci-env";
              paths = [
                pkgs.python3
                pkgs.python3Packages.pip
                pkgs.python3Packages.virtualenv
              ];
            })
          ];
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
