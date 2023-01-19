from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
import urllib
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        try:
            api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=ad6d91c541e7f84004e3201f55d89a05')
            api_url2 = json.loads(api_url.read())
            data = {
                "country": city,
                "weather_description": api_url2['weather'][0]['description'],
                "weather_temperature": api_url2['main']['temp'],
                "weather_pressure": api_url2['main']['pressure'],
                "weather_humidity":api_url2['main']['humidity'],
                "weather_icon": api_url2['weather'][0]['icon'],
            }
        except urllib.error.HTTPError as e:
            data = {
            "weather_description": 'Not found',
            "weather_temperature": 'Not found',
            "weather_pressure": 'Not found',
            "weather_humidity":'Not found',
            "weather_icon": 'Not found',
            }
            return render(request ,'index.html', {"city": city, "data" :data})
    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity":None,
            "weather_icon": None,
        }
    return render(request ,'index.html', {"city": city, "data" :data})


