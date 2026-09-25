# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day40_app.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

from flask import Flask, jsonify, request
# istallare usando pip install flask


app = Flask(__name__)

# Mock Weather Data
weather_data = {
    "new york": {"temperature": 22, "condition": "Sunny"},
    "london": {"temperature": 15, "condition": "Cloudy"},
    "tokyo": {"temperature": 28, "condition": "Clear"},
    "sydney": {"temperature": 18, "condition": "Rainy"}
}

# Root Finepoint
@app.route('/')
def home():
    return jsonify({"message": "Benvenuto to the Mini Weather API!"})

# Get Weather for All Cities
@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)

# Get Weather for a Specific City
@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = city.lower()
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    return jsonify({"Errore": "City not found"}), 404

# Aggiungi New weather Data
@app.route('/weather', methods=['POST'])
def Aggiungi_city_weather():
    data = request.json
    city = data.get('city', '').lower()
    temperature = data.get('temperature')
    condition = data.get('condition')

    if not city or not temperature or not condition:
        return jsonify({'Errore': 'Missing city, temperature or condition'}), 400

    weather_data[city] = {"temperature": temperature, "condition": condition}
    return jsonify({"message": f"weather for {city} Aggiungied Successofully"}), 201


# Run App
if __name__ == '__main__':
    app.run(debug=True)
