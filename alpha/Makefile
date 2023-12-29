.PHONE: clean env dev
VENV_DIR := .venv

all: build

clean:
	rm -rf $(VENV_DIR)

env: clean
	python3 -m venv $(VENV_DIR) && \
	. $(VENV_DIR)/bin/activate && \
	pip install --upgrade pip && \
	pip install poetry

dev: env
	. $(VENV_DIR)/bin/activate && \
	poetry install --no-interaction

setup:
	poetry install

lint: setup
	poetry run black src
	poetry run ruff check --fix src

build: lint setup
	rm -rf dist
	poetry build
	docker build . -t alpha -f Dockerfile
