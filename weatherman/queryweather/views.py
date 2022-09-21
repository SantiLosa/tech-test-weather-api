from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
from django.template import loader



# Create your views here.
def index(request):

    return HttpResponse("hello world")

def get_weather(request):
    city=request.GET.get("city")
    country=request.GET.get("country")
    appid= settings.APP_ID
    url =f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={appid}"
    print("URL", url)
    external_weather_api_response = requests.get(url)
    data = external_weather_api_response.json()
    print("response", data)
    for k,v in data.items():
        print(k,v)
    #Transform data
    def to_farenheit(num):
        return num
    def get_wind_message(num):
        return num
    def get_clouds_message(num):
        return num
    def get_time_format(num):
        return num
    def get_coordinates_format(num):
        return num
    response_json = {}
    response_json['location_name'] = f'{data["sys"]["main"]}'
    response_json['celcius_temperature'] = f'{data["main"]["temp"]} °C'
    response_json['farenheit_temperature'] = f'{to_farenheit(data["main"]["temp"])}'
    response_json['wind']= get_wind_message(data["wind"])
    response_json['cloudiness'] = get_clouds_message(data["clouds"])
    response_json['pressure'] = f'{data["main"]["pressure"]} hpa'
    response_json['humidity'] = f'{data["main"]["humidity"]}%'
    response_json['sunrise'] = get_time_format(data["sys"]["sunrise"])
    response_json['sunset'] = get_time_format(data["sys"]["sunrise"])
    response_json['geo_coordinates'] = get_coordinates_format(data["coord"])
    response_json['requested_time'] = datetime.now()
    response_json['forecast'] = {"veremos"}
    template = loader.get_template('weather.html')
    context={data}
    return HttpResponse(template.render(context, request))
