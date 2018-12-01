# limnopapers

[![Build Status](https://api.travis-ci.org/jsta/limnopapers.png)](https://travis-ci.org/jsta/limnopapers) [![Feed Status](https://img.shields.io/badge/feed%20status-good-green.svg)](https://jsta.github.io/limnopapers)

Code to monitor [limnology RSS feeds](journals.csv) and [tweet](https://twitter.com/limno_papers) new articles.

## Feed status
pad1|Last tweet|Last RSS entry|pad2
---|---|---|---
|![alt text](https://img.shields.io/badge/Limnology and Oceanography: Letters-2018--11--05-green.svg)|![alt text](https://img.shields.io/badge/Limnology and Oceanography: Letters-2018--11--08-green.svg)|
||![alt text](https://img.shields.io/badge/CJFAS-2018--11--12-green.svg)|
||![alt text](https://img.shields.io/badge/Freshwater Science-2018--11--20-green.svg)|
|![alt text](https://img.shields.io/badge/Freshwater Biology-2018--11--27-green.svg)|![alt text](https://img.shields.io/badge/Freshwater Biology-2018--11--20-green.svg)|
||![alt text](https://img.shields.io/badge/Global Biogeochemical Cycles-2018--11--26-green.svg)|
||![alt text](https://img.shields.io/badge/Marine and Freshwater Research-2018--11--29-green.svg)|
|![alt text](https://img.shields.io/badge/Inland Waters-2018--11--09-green.svg)|![alt text](https://img.shields.io/badge/Inland Waters-2018--11--29-green.svg)|
|![alt text](https://img.shields.io/badge/Oikos-2018--11--17-green.svg)|![alt text](https://img.shields.io/badge/Oikos-2018--11--29-green.svg)|
||![alt text](https://img.shields.io/badge/Global Ecology and Biogeography-2018--11--29-green.svg)|
|![alt text](https://img.shields.io/badge/JAWRA-2018--11--30-green.svg)|![alt text](https://img.shields.io/badge/JAWRA-2018--11--29-green.svg)|
|![alt text](https://img.shields.io/badge/Limnology and Oceanography-2018--11--16-green.svg)|![alt text](https://img.shields.io/badge/Limnology and Oceanography-2018--11--29-green.svg)|
|![alt text](https://img.shields.io/badge/Water Resources Research-2018--11--28-green.svg)|![alt text](https://img.shields.io/badge/Water Resources Research-2018--11--29-green.svg)|
||![alt text](https://img.shields.io/badge/Ecology-2018--11--29-green.svg)|
||![alt text](https://img.shields.io/badge/Journal of Geophysical Research: Biogeosciences-2018--11--30-green.svg)|
||![alt text](https://img.shields.io/badge/Biogeosciences-2018--11--30-green.svg)|
||![alt text](https://img.shields.io/badge/Earth System Science Data-2018--11--30-green.svg)|
|![alt text](https://img.shields.io/badge/HESS-2018--11--27-green.svg)|![alt text](https://img.shields.io/badge/HESS-2018--11--30-green.svg)|
||![alt text](https://img.shields.io/badge/Ecological Applications-2018--11--30-green.svg)|
|![alt text](https://img.shields.io/badge/Biogeochemistry-2018--11--24-green.svg)|![alt text](https://img.shields.io/badge/Biogeochemistry-2018--12--01-green.svg)|
||![alt text](https://img.shields.io/badge/Ambio-2018--12--01-green.svg)|
||![alt text](https://img.shields.io/badge/Aquatic Ecology-2018--12--01-green.svg)|
||![alt text](https://img.shields.io/badge/Ecosystems-2018--12--01-green.svg)|
|![alt text](https://img.shields.io/badge/Hydrobiologia-2018--11--19-green.svg)|![alt text](https://img.shields.io/badge/Hydrobiologia-2019--01--01-green.svg)|
|||

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

* Please help by adding missing journals to [journals.csv](journals.csv) or filing an [issue](https://github.com/jsta/limnopapers/issues)

* Filtering keywords are located in the [limnopapers.filter_limno](limnopapers.py) function.

## Prior art

https://github.com/ropenscilabs/data-packages
