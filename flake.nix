{
  description = "Smootz' Presentations Dev Shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
      };

      ciPkgs = [
        pkgs.bashNonInteractive
        pkgs.flake-checker
        pkgs.nixfmt
        pkgs.shellcheck
      ];

      devPkgs = [
        pkgs.cachix
      ]
      ++ ciPkgs;

    in
    {
      devShells.${system} = {
        default = pkgs.mkShell {
          packages = devPkgs;
        };
        ci = pkgs.mkShell {
          packages = ciPkgs;
        };
      };
    };
}
