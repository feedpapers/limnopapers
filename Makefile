test:
	pytest -v --ignore=scratch

dashboard:
	echo dashboard created
	python build_dashboard.py
	pandoc dashboard.md -o index.html
