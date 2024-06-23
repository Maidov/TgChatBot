import requests
from config import GISMETEO_API_KEY
#TODO: Узнать токен (сделал реквест на почту)
def get_weather(city):
    url = f'https://api.gismeteo.net/v2/weather/current/?city={city}'
    headers = {
        'X-Gismeteo-Token': GISMETEO_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        weather = data['response']['weather']
        return f"Weather in {city}: {weather['description']}, Temperature: {weather['temperature']['air']['C']}°C"
    else:
        return "Could not fetch weather data."