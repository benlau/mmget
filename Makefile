.PHONY: install test build clean format lint convert

install:
	pip install -r requirements.txt

test:
	pytest tests -v

build:
	rm -rf build dist mmget.egg-info
	python setup.py sdist bdist_wheel

clean:
	rm -rf build dist *.egg-info

format:
	black .

lint:
	flake8 .

convert:
	quarto convert  runbooks/tests.qmd 