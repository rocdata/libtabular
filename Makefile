.PHONY: clean test release

clean:
	rm -rf dist/*

test:
	pytest -s

release: clean ## package and upload a release
	pip install twine
	python setup.py sdist
	twine upload dist/*
