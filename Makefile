.PHONY: install install_pw test test_ci debug_test concat_vids

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	make install_pw

install_pw:
	python -m playwright install chromium
	python -m playwright install-deps chromium

test:
	make run_pytest args="--headed $(args)"

test_ci:
	make run_pytest args="$(args)"

debug_test:
	PWDEBUG=1 make run_pytest args="$(args)"

concat_vids:
	rm -f list.txt && for f in videos/*.webm; do echo file \'$$f\' >> list.txt; done && ffmpeg -f concat -i list.txt -c copy -y test_all.webm && rm list.txt

run_pytest:
	python -m pytest -s $(args)
