import os
from pprint import pprint
from datetime import datetime
import requests

#http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us,&units=metric&appid=175bbb8490512ae8c294388a17496add
# setting up the weather key 
key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'metric', 'appid': key}

#url and quiry 
url = 'http://api.openweathermap.org/data/2.5/forecast'
data =  requests.get(url, params=query).json()
pprint(data)

list_of_forecasts = data['list']

#displaying the date and time and also a tempeture 
for forecast in list_of_forecasts:
    temp = forecast['main'] ['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print (f'At {forecast_date} the temperature will be {temp} C')