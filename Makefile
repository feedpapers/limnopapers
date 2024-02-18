run:
	limnopapers --interactive

ignore:
	limnopapers --interactive --ignore_all

# pytest test_foo.py
tests/test_data.json: tests/create_test_data.py
	python $<

test:
	pytest -v --ignore=scratch --ignore=build_dashboard.py

dashboard:
	echo dashboard created
	python build_dashboard.py
	pandoc dashboard.md -o dashboard.html	

install:
	pip install --upgrade -e .

keywords:
	git pull && git add limnopapers/keywords.csv && git commit -m "stash keywords [skip ci]" && git push

log:
	git pull && git add log.csv && git commit -m "stash log [skip ci]" && git push