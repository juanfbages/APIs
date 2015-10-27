## Description

This project provides sample code to quickly access data via APIs.

### Current APIs

* [Wundeground](#wunderground)

## Usage

API speficics (e.g. key) need to updated before running the the scripts. In general, the scripts do not take any additional arguments. For individual API usage please see their specific sections below.

```
$ python wunderground.py
```

## Dependencies
* I try to use standard python modules that can be installed using ```pip```
* While not required, I recommend installing and maintaining packages using [anaconda](https://www.continuum.io/why-anaconda)

## APIs

### Wunderground

Wunderground (Weather Underground) provides local and international weather reports. They offer an excellent API to access their data. You can sign up for an account [here](http://www.wunderground.com/weather/api/). All relevant information related to the API use is [here](http://www.wunderground.com/weather/api/d/docs).

The script retrieves historical data as specified for a given city, state, and start and end dates. This script parses data returned in ```json``` format and saves it as a ````csv``` file. It does not take any additional arguments. Below is a snippet of the section that needs to be updated before running the script. Please note that the end date is not inclusive. In other words, in the example below, data for January 1, 2015 will not be returned. 

```
# Set up date and key information
city = 'Washington'
state = 'DC'
api_key = 'Insert API Key here'

# Date format (YYYY, M, D)
start_date = dt.date(2014,1,1)
end_date = dt.date(2015,1,1)
``` 
For the purpose of this example, I limit the number of variables included in the output. Feel free to add or remove any variables as needed. This can be done by adding elements to the ```wx_vars``` list. A comprehensive list of features included for historical data can be found [here](http://www.wunderground.com/weather/api/d/docs?d=data/history&MR=1). 

While the script targets historic data, the structure can be easily adapted to retrieve any other data feature provided through Wundeground's API.

