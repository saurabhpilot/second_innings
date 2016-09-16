import requests
import re

def get_weather_forecast():
    # Connecting to the weather api
    url="http://api.openweathermap.org/data/2.5/weather?q=shrewsbury,us&units=imperial&appid=2b6b6ad043e6570938e91cda8bdafb89"
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    # Getting the location
    locationMatch=re.search(r'q=([A-Za-z]+)',url)
    location=locationMatch.group(1)
    # Parsing the JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    # Creating a forecast message
    forecast = "Today's Weather Forecast for " + location + ' is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of '+ str(int(temp_min))

    return forecast
