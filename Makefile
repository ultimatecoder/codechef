install:
	pip install pipenv
	pipenv install --dev
test: unit-test
unit-test:
	pipenv run pytest solutions
