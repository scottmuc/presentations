#!/usr/bin/env bash

set -euo pipefail

fly -t concourse.scottmuc.com \
  set-pipeline \
  --pipeline presentations \
  --config ./pipeline.yml
