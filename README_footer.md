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
