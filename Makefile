# Define targets
.PHONY: pretty test

pretty: isort black

black:
	black . --exclude env/

isort:
	isort . --skip env/

test_ml:
	pytest tests/test_ml.py
	