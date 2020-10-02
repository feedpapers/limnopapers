# limnopapers

[![Build Status](https://api.travis-ci.org/jsta/limnopapers.png)](https://travis-ci.org/jsta/limnopapers) [![Feed Status](https://img.shields.io/badge/feed%20status-good-green.svg)]

Code to monitor [limnology RSS feeds](limnopapers/journals.csv) and [tweet](https://twitter.com/limno_papers) new articles.

## Scope

The keywords and journal choices herein aim to focus on limnology (the study of inland waters). They are also meant to exclude related topics such as fisheries ecology, water resources engineering, estuarine/marine ecology, ecological genetics, and the study of specific "inland seas" like the North American Great Lakes. Feel free to weigh-in in the repository issues on scope recommendations! 

## Usage

Query papers that came out prior to today without tweeting:

`python limnopapers/limnopapers.py`

Query papers that came out prior to today and open in browser:

`python limnopapers/limnopapers.py --browser`

Manually approve tweeting of papers that came out prior to today:

`python limnopapers/limnopapers.py --interactive`

Unsupervised tweeting of papers that came out prior to today:

`python limnopapers/limnopapers.py --tweet`

## Setup

### Enable tweeting (optional)

* Create a file named `config.py` that stores your twitter API keys

### Enable unsupervised tweeting (optional)

* Create a _cron_ job. On Linux this can be done with the following commands:

```
crontab -e 
0 15 * * * python /path/to/limnopapers.py
```

### Python dependencies

See [requirements.txt](requirements.txt)

Install these to the activated environment with:

`pip install -r requirements.txt`

## Contributing

* Please help by adding missing journals to [limnopapers/journals.csv](limnopapers/journals.csv) or filing an [issue](https://github.com/jsta/limnopapers/issues)

* Filtering keywords are located in [limnopapers/keywords.csv](limnopapers/keywords.csv).

## Prior art

https://github.com/ropenscilabs/data-packages
