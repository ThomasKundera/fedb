{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = [ (pkgs.haskellPackages.ghcWithPackages (p: [p.aeson p.bytestring p.text])) ];
}
