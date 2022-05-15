#!/usr/bin/env bash

set -e

docker run -it --rm \
  -v $PWD:$PWD \
  -w $PWD \
  -e UID="$(id -u)" \
  -e GID="$(id -g)" \
  -e USER="$(whoami)" \
  -e HOME="/home/$(whoami)" \
  scottmuc/handsongit tmuxinator start workshop
