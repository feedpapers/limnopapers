# limnopapers

Code to monitor [limnology RSS feeds](journals.csv) and [tweet](https://twitter.com/limnopapers) new articles.

## Usage

Tweet papers that came out today:

`python limnopapers.py`

Tweet papers that came out on an arbitrary day:

`python limnopapers.py '2018-07-29'`

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

Please help by adding missing journals to `journals.csv` or filing an [issue](https://github.com/jsta/limnopapers/issues)

## Prior art

https://github.com/ropenscilabs/data-packages
