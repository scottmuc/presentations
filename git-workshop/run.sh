#!/usr/bin/env bash

set -e

docker run -it --rm \
  -v $PWD:/workspace \
  -w /workspace \
  -e UID="$(id -u)" \
  -e GID="$(id -g)" \
  -e USER="handsongit" \
  -e HOME="/home/handsongit" \
  scottmuc/handsongit
