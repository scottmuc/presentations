#!/usr/bin/env bash

set -e

docker run -it --rm \
  -w /root/workshop \
  -v $PWD:$PWD \
  -w $PWD \
  gitworkshop tmuxinator start workshop
