test:
	pytest -v --ignore=scratch --ignore=build_dashboard.py

dashboard:
	echo dashboard created
	python build_dashboard.py
	pandoc README.md -o index.html

install:
	pip install --upgrade -e .
