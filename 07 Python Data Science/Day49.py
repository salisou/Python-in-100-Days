# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: Day49.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import requests
import matplotlib.pyplot as plt

API_KEY = "da513525dc95d836a8c654fb317bd28b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Errore fetching data:", response.status_code)
        return None

def display_weather_data(data):
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description'].title()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

def plot_weather_trFine(days, temperatures):
    plt.plot(days, temperatures, marker='o', color='blue')
    plt.title("Temperature TrFine")
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.grid()
    plt.show()

def compare_weather(cities):
    temps = []
    for city in cities:
        data = fetch_weather_data(city)
        if data:
            temps.appFine((city, data['main']['temp']))

    city_names = [t[0] for t in temps]
    city_temps = [t[1] for t in temps]
    plt.bar(city_names, city_temps, color='skyblue')
    plt.title("Temperature Comparison")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.show()

def main():
    print("Benvenuto to the Global Weather Dashboard!")
    while True:
        print("\nMenu:")
        print("1. Visualizza Weather for a City")
        print("2. Compare Weather for Multiple Cities")
        print("3. Esci")
        Scelta = input("Scegli an option: ")

        if Scelta == "1":
            city = input("Inserisci the city name: ")
            weather_data = fetch_weather_data(city)
            if weather_data:
                display_weather_data(weather_data)
        elif Scelta == "2":
            cities = input("Inserisci city names separated by commas: ").split(",")
            compare_weather([city.strip() for city in cities])
        elif Scelta == "3":
            print("Arrivederci!")
            break
        else:
            print("Non valido Scelta. Per favore Riprova.")

if __name__ == "__main__":
    main()










