import urllib2
import json
import datetime as dt
import csv
import time

def main():
    # Set up date and key information
    city = 'Washington'
    state = 'DC'
    api_key = 'Insert API Key ere'
    # Date format (YYYY, M, D)
    start_date = dt.date(2014,1,1)
    end_date = dt.date(2015,1,1)

    # Obtain date_list
    date_list = [single_date.strftime("%m/%d/%Y") for single_date in daterange(start_date, end_date)]

    # list of weather variables
    wx_vars = ['date',
               'hour',
               'heatindexm',
               'windchillm',
               'hail',
               'thunder',
               'snow',
               'pressurem',
               'fog',
               'precipm',
               'conds',
               'tornado',
               'hum',
               'tempm',
               'rain',
               'vism',
               'wspdm']

    weather_data = [wx_vars]

    # Loop through all dates
    for date in date_list:
        t = api_call(api_key, date, state, city)
        json_string = t.read()
        parsed_json = json.loads(json_string)

        for hour in range(0, len(parsed_json['history']['observations'])):
            hour_data = parsed_json['history']['observations'][hour]
            tmp_wx = [hour_data[var] for var in wx_vars if var not in ['date', 'hour']]
            tmp_wx.insert(0, hour_data['date']['mon'] 
             + '/' + hour_data['date']['mday'] + '/' + hour_data['date']['year'])
            tmp_wx.insert(1, hour_data['date']['hour'])
            weather_data.append(tmp_wx)
    t.close()
    time.sleep(7)

    # Write it to csv
    filename = city + '_weather.csv'
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(weather_data)

def daterange(start_date, end_date):
    # This function obtains a list of date ranges. Excludes end_date
    for n in range(int ((end_date - start_date).days)):
        yield start_date + dt.timedelta(n)

def api_call(api_key, date, state, city):
    '''
    This function makes an API call to Wunderground. As set up the call
    obtains historical data for a given date, state, and city. The call
    returns a json file.
    '''
    # Split Date
    month, day, year = date.split('/')
    # Get URL
    f = urllib2.urlopen('http://api.wunderground.com/api/'
        + api_key  
        + '/history_'
        + year 
        + month
        + day 
        + '/q/'
        + state
        + '/' 
        + city
        + '.json')
    return f

if __name__ == '__main__':
    main()