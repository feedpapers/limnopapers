## Setup

### Python depedencies
```
pip install pandas -t . 
pip install python-twitter -t .
pip install datetime -t .
pip install feedparser -t .
```

### Prep for AWS lambda

* Zip limnopapers directory
* open lambda console
	* create new function
	* blank function
	* configure trigger - cloudwatch events
	* runtime - python3.6
	* code entry -> upload zip
	* handler -> limnopapers.limnotoots
