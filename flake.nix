{
  description = "A very basic flake";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
    in
    {
      inherit system;
      devShell.${system} =
        pkgs.mkShell {
          # The packages we need for this project
          buildInputs = [
            pkgs.python311
            pkgs.poetry
          ];
        };
    };
}
