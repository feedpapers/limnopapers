# limnopapers

Code for creating an AWS lambda function to monitor limnology RSS feeds and tweet new articles.

## Setup

### Python depedencies

```
pip install pandas -t . 
pip install python-twitter -t .
pip install datetime -t .
pip install feedparser -t .
```

### Prep for AWS lambda

* enter consumer and token keys in `limnopapers.py`
* zip limnopapers directory
* open lambda console
	* create new function
	* blank function
	* configure trigger - cloudwatch events
	* runtime - python3.6
	* code entry -> upload zip
	* handler -> limnopapers.limnotoots
	* adjust timeout length as needed

## Prior art

https://github.com/ropenscilabs/data-packages
