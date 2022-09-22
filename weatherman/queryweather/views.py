from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
from django.template import loader
from .utils import get_wind_message, k_to_celcius, get_clouds_message, get_time_format, get_coordinates_format, get_forecast, k_to_farenheit


# Create your views here.
def index(request):

    return HttpResponse("hello world")

def get_weather(request):
    city=request.GET.get("city")
    country=request.GET.get("country")
    appid= settings.APP_ID
    # GET CURRENT WEATHER
    url =f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={appid}"
    print("URL", url)
    external_weather_api_response = requests.get(url)
    data = external_weather_api_response.json()
    # GET FORECAST DATA (4 dias)
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={appid}"
    print("URL", url)
    external_forecast_api_response = requests.get(url)
    forecast_data = external_forecast_api_response.json()
    print("response", data)
    for k,v in data.items():
        print(k,v)
    #Transform data

    response_json = {}
    response_json['location_name'] = f'{data["name"]}, {data["sys"]["country"]}'
    response_json['celcius_temperature'] = f'{k_to_celcius(data["main"]["temp"])} °C'
    response_json['farenheit_temperature'] = f'{k_to_farenheit(data["main"]["temp"])} °F'
    response_json['wind']= get_wind_message(data["wind"])
    response_json['cloudiness'] = get_clouds_message(data["clouds"]["all"])
    response_json['pressure'] = f'{data["main"]["pressure"]} hpa'
    response_json['humidity'] = f'{data["main"]["humidity"]}%'
    response_json['sunrise'] = get_time_format(data["sys"]["sunrise"])
    response_json['sunset'] = get_time_format(data["sys"]["sunset"])
    response_json['geo_coordinates'] = get_coordinates_format(data["coord"])
    response_json['requested_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response_json['forecast'] = {} #get_forecast(forecast_data)
    template = loader.get_template('weather.html')
    context={"current_weather": response_json}
    return HttpResponse(template.render(context, request))

{"dt":1663804800,
"main":{
    "temp":287.57,
    "feels_like":287.05,
    "temp_min":284.94,
    "temp_max":287.57,
    "pressure":1021,
    "sea_level":1021,
    "grnd_level":752,
    "humidity":76,
    "temp_kf":2.63
    },
"weather":[
        {"id":500,
        "main":"Rain",
        "description":
        "light rain",
        "icon":"10n"}
        ],
    "clouds":{
        "all":83
        },
    "wind":{
        "speed":0.15,
        "deg":204,
        "gust":0.76
        },
    "visibility":10000,
    "pop":0.96,
    "rain":{
        "3h":1.69
        },
    "sys":{
        "pod":"n"
        },
    "dt_txt":"2022-09-22 00:00:00"
    }