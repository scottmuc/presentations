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
    uv sync
}

style_check() {
    find features/ -name "*.py" -exec uv run pycodestyle --show-pep8 {} +
}

run_tests() {
    if [[ -n "${TEST_WIP}" ]]; then
        uv run behave --define steps_dir=features/steps/in_memory_steps \
            --no-source --no-timings --no-summary --stop
    else
        uv run behave --no-source --no-timings --no-summary --stop
    fi
}

check_uv() {
    if ! command -v uv >/dev/null; then
        echo "uv not detected, please install uv first"
        exit 1
    fi
    echo "uv location : $(command -v uv)"
    echo "uv version  : $(uv --version)"

}

check_python() {
    if ! command -v $PYTHON_CMD >/dev/null; then
        echo "Python not detected, please install python first"
        exit 1
    fi
    echo "Python location : $(command -v $PYTHON_CMD)"
    echo "Python version  : $($PYTHON_CMD --version)"
}

main "$@"
