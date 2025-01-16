# Define variables
PYINSTALLER_FLAGS=--onefile \
                  --add-data "static:static" \
                  --add-data "templates:templates" \
                  --add-data "app:app"
MAIN_SCRIPT=main.py
DOCKER_COMPOSE_FILE=docker-compose-local.yml

default: help

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  native  - Build the Python application using PyInstaller"
	@echo "  docker  - Build and run the application using Docker Compose"

.PHONY: native
native:
	pyinstaller $(PYINSTALLER_FLAGS) $(MAIN_SCRIPT)

.PHONY: docker
docker:
	docker compose -f $(DOCKER_COMPOSE_FILE) up --build -d