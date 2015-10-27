## Description

This project intends to add sample code to quickly access data via APIs.

## Usage

API speficics (e.g. key) need to be changed before running the the scripts. In general, the scripts do not take any additional arguments. For individual API usage please see their specific sections below.

```
$ python wunderground.py
```

## APIs

### Wunderground

Wunderground (Weather Underground) provides local and international weather reports. They offer an excellent API to access their data. You can sign up for an account [here](http://www.wunderground.com/weather/api/). All relevant information related to the API use is [here](http://www.wunderground.com/weather/api/d/docs).

This script is setup to retrieve historical data between a given start date and end date, for a given city and state. The script does not take any arguments. Below is the snippet of the code section that needs to be changed in the script. Please note that the end date is not inclusive. Thus, in the below example, data for January 1, 2015 will not be included. 

```
# Set up date and key information
city = 'Washington'
state = 'DC'
api_key = 'Insert API Key here'

# Date format (YYYY, M, D)
start_date = dt.date(2014,1,1)
end_date = dt.date(2015,1,1)
``` 

Please note that the code only returns a limited number of 