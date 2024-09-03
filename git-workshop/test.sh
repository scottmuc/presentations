#!/usr/bin/env bash

set -eu -o pipefail

main() {
    check_python
    check_pip
    check_virtualenv
    setup_virtualenv
    activate_virtualenv
    install_dependencies
    run_tests
}

run_tests() {
    behave
}

install_dependencies() {
    pip install -r ./requirements.txt
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
    if ! command -v pip >/dev/null; then
        echo "Pip not detected, please install pip in your python environment"
        exit 1
    fi
    echo "Pip location : $(command -v pip)"
    echo "Pip version  : $(pip --version)"
}

check_python() {
    if ! command -v python >/dev/null; then
        echo "Python not detected, please install python first"
        exit 1
    fi
    echo "Python location : $(command -v python)"
    echo "Python version  : $(python --version)"
}

main "$@"
