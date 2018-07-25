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

Create a `twitter_api.py` file with the following keys defined:

```
import twitter
api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='',	access_token_secret='')
```

### Python depedencies

See [requirements.txt](requirements.txt)

For local operation install these to the activated environment with:

`pip install -r requirements.txt`

## Prior art

https://github.com/ropenscilabs/data-packages
