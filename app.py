# this app runs in GUI mode
import tkinter as tk
import requests
from datetime import datetime

root = tk.Tk()
root.geometry("400x400")

root.title("International Weather App")


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


city_value = tk.StringVar()


def show_weather():
    api_key = '367f87de8e875c17fd636edb1ba4a992'
    city_name = city_value.get()
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")
    if weather_info['cod'] == 200:
        kelvin = 273
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(tk.INSERT, weather)


city_head = tk.Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)

inp_city = tk.Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()

tk.Button(root, command=show_weather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black',
          activebackground="teal", padx=5, pady=5).pack(pady=20)

weather_now = tk.Label(root, text="The Weather is:", font='arial 12 bold').pack(pady=10)

tfield = tk.Text(root, width=46, height=10)
tfield.pack()

root.mainloop()
