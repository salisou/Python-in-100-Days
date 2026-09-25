# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day69.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import tkinter as tk
from tkinter import ttk
import json

def load_exchange_rates(file_path="exchange_rates.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundErrore:
        print("Exchange rate file not found!")
        return {}

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]

def handle_conversion():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_dropdown.get()
        to_currency = to_currency_dropdown.get()
        rates = load_exchange_rates()
        Risultato = convert_currency(amount, from_currency, to_currency, rates)
        if Risultato is not None:
            Risultato_label.config(text=f"{amount} {from_currency} = {Risultato:.2f} {to_currency}")
        else:
            Risultato_label.config(text="Conversion Errore!")
    except ValueErrore:
        Risultato_label.config(text="Non valido Amount!")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Amount Entry
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# From Currency Dropdown
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)
from_currency_dropdown = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "JPY"])
from_currency_dropdown.pack(pady=5)

# To Currency Dropdown
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency_dropdown = ttk.Combobox(root, values=["USD", "EUR", "GBP", "INR", "JPY"])
to_currency_dropdown.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=handle_conversion)
convert_button.pack(pady=10)

Risultato_label = tk.Label(root, text="", font=("Arial", 14))
Risultato_label.pack(pady=10)

root.mainloop()
















# rates = load_exchange_rates()
# amount = 100
# converted = convert_currency(amount, "USD", "JPY", rates)
# print(f"Converted {amount} USD to JPY: {converted:.2f}")


