import requests


def get_weather(city):
    geocoding_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
    geocoding_response = requests.get(geocoding_url)

    if geocoding_response.status_code == 200:
        geocoding_data = geocoding_response.json()
        if geocoding_data.get('results'):
            latitude = geocoding_data['results'][0]['latitude']
            longitude = geocoding_data['results'][0]['longitude']

            weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto'
            weather_response = requests.get(weather_url)

            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                daily = weather_data['daily']
                max_temp = daily['temperature_2m_max'][0]
                min_temp = daily['temperature_2m_min'][0]
                weathercode = daily['weathercode'][0]

                # Преобразование weathercode в описание
                weather_descriptions = {
                    0: 'Clear sky',
                    1: 'Mainly clear',
                    2: 'Partly cloudy',
                    3: 'Overcast',
                    45: 'Fog',
                    48: 'Depositing rime fog',
                    51: 'Drizzle: Light',
                    53: 'Drizzle: Moderate',
                    55: 'Drizzle: Dense intensity',
                    56: 'Freezing Drizzle: Light',
                    57: 'Freezing Drizzle: Dense intensity',
                    61: 'Rain: Slight',
                    63: 'Rain: Moderate',
                    65: 'Rain: Heavy intensity',
                    66: 'Freezing Rain: Light',
                    67: 'Freezing Rain: Heavy intensity',
                    71: 'Snow fall: Slight',
                    73: 'Snow fall: Moderate',
                    75: 'Snow fall: Heavy intensity',
                    77: 'Snow grains',
                    80: 'Rain showers: Slight',
                    81: 'Rain showers: Moderate',
                    82: 'Rain showers: Violent',
                    85: 'Snow showers: Slight',
                    86: 'Snow showers: Heavy',
                    95: 'Thunderstorm: Slight or moderate',
                    96: 'Thunderstorm with slight hail',
                    99: 'Thunderstorm with heavy hail'
                }

                weather_description = weather_descriptions.get(weathercode, 'Unknown weather')
                return f"Weather in {city}: {weather_description}, Temperature: {min_temp}°C - {max_temp}°C"
            else:
                return "Could not fetch weather data."
        else:
            return "City not found."
    else:
        return "Could not fetch geocoding data."


# Example usage
if __name__ == "__main__":
    city = "Moscow"
    print(get_weather(city))