# limnopapers

Code to monitor limnology RSS feeds and tweet new articles.

Specific feeds include:

* Limnology and Oceanography

* Limnology and Oceanography Letters

* Freshwater Science

* Inland waters

* Freshwater Biology

* Water Resources Research

* Journal of Geophysical Research: Biogeosciences

* Hydrological processes

* Ecological Applications

## Setup

* Create a _cron_ job. On Linux this can be done with the following commands:

```
crontab -e 
* */15 * * * /path/to/limnopapers.py
```

### Python depedencies

See [requirements.txt](requirements.txt)

For local operation install these to the activated environment with:

`pip install -r requirements.txt`

## Prior art

https://github.com/ropenscilabs/data-packages
