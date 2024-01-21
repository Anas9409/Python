import tkinter as tk
from tkinter import ttk
import requests

def get_weather(city, units):
    api_key = 'd629960515208772ab7f9e1d7233b022'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric' if units == 'celsius' else 'imperial', 'appid': api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        result_label.config(text=f'Temperature: {temperature}°{units.capitalize()}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s')

    except requests.exceptions.RequestException as e:
        result_label.config(text=f'Error: {e}')

def show_weather():
    city_name = city_entry.get()
    units = unit_var.get().lower()
    get_weather(city_name, units)


root = tk.Tk()
root.title("Weather App")
root.geometry('480x240')
root.minsize(480, 240)
root.maxsize(480, 240)
root.configure(bg='#3498db')

tk.Label(root, text="City:", bg='#3498db', fg='white', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

city_entry = tk.Entry(root, font=('Arial', 12))
city_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Units:", bg='#3498db', fg='white', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

unit_var = tk.StringVar()
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=['Celsius', 'Fahrenheit'], font=('Arial', 12))
unit_menu.grid(row=1, column=1, padx=10, pady=10)
unit_menu.current(0)

result_label = tk.Label(root, text="", bg='#3498db', fg='white', font=('Arial', 12))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

show_button = tk.Button(root, text="Show Weather", command=show_weather, font=('Arial', 12), bg='#2ecc71', fg='white')
show_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
