## Usage

Query papers that came out prior to today without tweeting:

`python limnopapers.py`

Manually approve tweeting of papers that came out prior to today:

`python limnopapers.py --tweet --interactive`

Unsupervised tweeting of papers that came out prior to today:

`python limnopapers.py --tweet`

## Setup

* Create a file named `config.py` that stores your twitter API keys

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
