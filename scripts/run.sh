#!/bin/bash

ENV="develop"
ENTRY="main.py"
PROJECT_NAME="app"
CONFIGURATION_FILE="configuration.yaml"

PROJECT_ROOT_DIR="$(dirname -- "$(readlink -f -- "$PWD")")"
PROJECT_DIR="${PROJECT_ROOT_DIR}/${PROJECT_NAME}"

export PYTHONPATH="$PYTHONPATH:${PROJECT_DIR}"

export CONFIG_PATH="${PROJECT_ROOT_DIR}/${CONFIGURATION_FILE}"
export ENVIRONMENT="${ENV}"

export SERVER_PORT=8080

export DATABASE_USERNAME=postgres
export DATABASE_PASSWORD=postgres
export DATABASE_PORT=5432
export DATABASE_HOST=0.0.0.0
export DATABASE_NAME=develop_db

cd "../"
source "${PROJECT_ROOT_DIR}/venv/bin/activate"
python "${PROJECT_DIR}/${ENTRY}"
