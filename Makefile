.PHONY: install test test_ci

install:
	pip install -r requirements.txt
	playwright install chromium

test:
	python -m pytest -s --headed

test_ci:
	python -m pytest -s
