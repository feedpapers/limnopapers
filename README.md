# limnopapers

Code for creating an AWS lambda function to monitor limnology RSS feeds and tweet new articles.

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

### Python depedencies

See [requirements.txt](requirements.txt)

For local operation install these to the activated environment with:

`pip install -r requirements.txt`

For AWS lambda, these need to be installed to the local `limnopapers` directory with: 

`pip install foo -t .`

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
