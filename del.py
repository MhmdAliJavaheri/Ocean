import requests

city_name = str(input('Enter City Name: '))


def find_weather_temp():
    api_key = '367f87de8e875c17fd636edb1ba4a992'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(url)
    if response.json()['cod'] == "404":
        print('city not found')
    else:
        temp_in_fahrenheit = float(response.json()['main']['temp'])
        converted_temp = temp_in_fahrenheit - 273.15
        humidity = response.json()['main']['humidity']
        print('temperature:', round(converted_temp, 3), 'celsius')
        print('humidity of weather in', city_name, ':', humidity)
        print('country of city:', response.json()['sys']['country'])


find_weather_temp()
