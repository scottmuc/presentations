#!/usr/bin/env bash

set -eu -o pipefail

PYTHON_CMD=python3
PIP_CMD=pip3

main() {
    print_env
    check_python
    check_pip
    check_virtualenv
    setup_virtualenv
    activate_virtualenv
    install_dependencies
    style_check
    run_tests
}

print_env() {
    env
}

style_check() {
    find features/ -name "*.py" -exec pycodestyle --show-pep8 {} +
}

run_tests() {
    behave --no-source --no-timings --no-summary
}

install_dependencies() {
    $PIP_CMD install -r ./requirements.txt
}

activate_virtualenv() {
    source venv/bin/activate
}

setup_virtualenv() {
    if [[ ! -d ./venv ]]; then
        virtualenv venv
    fi
}

check_virtualenv() {
    if ! command -v virtualenv >/dev/null; then
        echo "Virtualenv not detected, please install virtualenv via pip"
        exit 1
    fi
    echo "Virtualenv location : $(command -v virtualenv)"
    echo "Virtualenv version  : $(virtualenv --version)"
}

check_pip() {
    if ! command -v $PIP_CMD >/dev/null; then
        echo "Pip not detected, please install pip in your python environment"
        exit 1
    fi
    echo "Pip location : $(command -v $PIP_CMD)"
    echo "Pip version  : $($PIP_CMD --version)"
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
