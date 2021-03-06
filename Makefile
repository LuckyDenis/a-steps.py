SHELL := /bin/bash
CMD_INSTALL := pip install -r


install-dev:
	$(CMD_INSTALL) ./requirements-dev.txt

install:
	$(CMD_INSTALL) ./requirements.txt

test:
	pytest ./

flake8:
	flake8 ./app ./tests/
