test:
	pytest -v --ignore=scratch

dashboard:
	echo dashboard created
	pandoc dashboard.md -o dashboard.html
