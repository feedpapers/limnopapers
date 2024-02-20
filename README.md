# limnopapers

![pytest](https://github.com/jsta/limnopapers/workflows/pytest/badge.svg)

Code to monitor [limnology RSS feeds](limnopapers/journals.csv) and post new articles to [Mastodon](https://fediscience.org/@limnopapers).

## Scope

The keywords and journal choices herein aim to focus on limnology (the study of inland waters). They are also meant to exclude related topics such as fisheries ecology, water resources engineering, estuarine/marine ecology, ecological genetics, and the study of specific "inland seas" like the North American Great Lakes. Feel free to weigh-in in the repository issues on scope recommendations!

## Usage

Query papers that came out prior to today without posting:

`limnopapers`

Query papers that came out prior to today and open in browser:

`limnopapers --browser`

Manually approve posting of papers that came out prior to today:

`limnopapers --interactive`

Unsupervised posting of papers that came out prior to today:

`limnopapers --tweet`

"Reset" the tweet log:

```shell
limnopapers --ignore_all
# manually delete old log entries
```

## Setup

### Enable posting (optional)

* Create a file named `config.py` that stores your Twitter/Mastodon API keys

### Enable unsupervised posting (optional)

* Create a _cron_ job. On Linux this can be done with the following commands:

```shell
crontab -e 
0 15 * * * python /path/to/limnopapers.py
```

### Python dependencies

See [requirements.txt](requirements.txt)

Install these to the activated environment with:

`pip install -r requirements.txt`

or:

`mamba env create -f environment.yml`

## Contributing

* Please help by adding missing journals to [limnopapers/journals.csv](limnopapers/journals.csv) or filing an [issue](https://github.com/jsta/limnopapers/issues)

* Filtering keywords are located in [limnopapers/keywords.csv](limnopapers/keywords.csv).

## Prior art

https://github.com/ropenscilabs/data-packages
