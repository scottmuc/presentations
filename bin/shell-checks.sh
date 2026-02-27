#!/usr/bin/env bash

set -e

# shellcheck disable=SC2038
find . -path '*/venv' -prune -o -name "*.sh" -print \
  | xargs shellcheck

cat << EOT
********************************************************************************
The code has passed all the bash static analyis checks!
********************************************************************************
EOT
