setup: setup-local
	@pip install -r ./src/requirements.txt

setup-local:
    @pip install -r ./requirements-dev.txt
