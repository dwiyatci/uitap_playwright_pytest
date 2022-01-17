.PHONY: install install_pw test test_ci

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	make install_pw

install_pw:
	playwright install chromium
	playwright install-deps chromium

test:
	python -m pytest -s --headed

test_ci:
	python -m pytest -s
