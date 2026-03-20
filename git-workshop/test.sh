#!/usr/bin/env bash

set -e -o pipefail

PYTHON_CMD=python3

main() {
    check_python
    check_uv

    # If we've reached here, all machine dependecnies are met!
    uv_sync
    style_check
    run_tests
}

uv_sync() {
    if ! command -v behave >/dev/null; then
        echo "did not detect behave, so performing uv sync"
        uv sync
    fi
}

style_check() {
    find features/ -name "*.py" -exec pycodestyle --show-pep8 {} +
}

run_tests() {
    if [[ -n "${TEST_WIP}" ]]; then
        behave --define steps_dir=features/steps/in_memory_steps \
            --no-source --no-timings --no-summary --stop
    else
        behave --no-source --no-timings --no-summary --stop
    fi
}

check_uv() {
    if command -v uv >/dev/null; then
        echo "uv location : $(command -v uv)"
        echo "uv version  : $(uv --version)"
    fi
}

check_python() {
    if  command -v $PYTHON_CMD >/dev/null; then
        echo "Python location : $(command -v $PYTHON_CMD)"
        echo "Python version  : $($PYTHON_CMD --version)"
    fi
}

main "$@"
