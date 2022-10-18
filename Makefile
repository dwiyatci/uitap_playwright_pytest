.PHONY: install install_pw test test_ci debug_test concat_vids

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	make install_pw

upgrade:
	pip install --upgrade pip
	pip install upgrade-requirements
	upgrade-requirements
	make install_pw

install_pw:
	python -m playwright install chromium
	python -m playwright install-deps chromium

test_parallel:
	make test args="--workers 2 --tests-per-worker auto $(args)"

test:
	make test_ci args="--headed $(args)"

test_ci:
	make run_pytest args="$(args)"

debug_test:
	PWDEBUG=1 make run_pytest args="$(args)"

run_pytest:
	python -m pytest -s $(args)
