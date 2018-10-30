# limnopapers

[![Build Status](https://api.travis-ci.org/jsta/limnopapers.png)](https://travis-ci.org/jsta/limnopapers)

Code to monitor [limnology RSS feeds](journals.csv) and [tweet](https://twitter.com/limno_papers) new articles.

## Usage

Query papers that came out prior to today without tweeting:

`python test_fetch.py`

Tweet papers that came out prior to today:

`python limnopapers.py`

## Setup

* Create a file named `config.py` that stores your twitter API keys

* Create a _cron_ job. On Linux this can be done with the following commands:

```
crontab -e 
0 15 * * * python /path/to/limnopapers.py
```

### Python depedencies

See [requirements.txt](requirements.txt)

Install these to the activated environment with:

`pip install -r requirements.txt`

## Contributing

* Please help by adding missing journals to [journals.csv](journals.csv) or filing an [issue](https://github.com/jsta/limnopapers/issues)

* Filtering keywords are located in the [limnopapers.filter_limno](limnopapers.py) function.

## Prior art

https://github.com/ropenscilabs/data-packages
