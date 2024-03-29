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
	make playwright args="install chromium"
	make playwright args="install-deps chromium"

test:
	make run_pytest args="--headed $(args)"

test_ci_parallel:
	make test_ci args="--numprocesses auto $(args)"

test_ci:
	make run_pytest args="$(args)"

debug:
	PWDEBUG=1 make run_pytest args="$(args)"

concat_vids:
	rm -f list.txt && for f in videos/*.webm; do echo file \'$$f\' >> list.txt; done && ffmpeg -f concat -i list.txt -c copy -y test_all.webm && rm list.txt

run_pytest:
	python -m pytest -s $(args)

codegen:
	make playwright args="codegen http://www.uitestingplayground.com/home"

playwright:
	python -m playwright $(args)
