# -*- coding: utf-8 -*-
"""Giorno 1 — Introduzione a Python.

Obiettivo: imparare a usare print(), input(), variabili e f-string.
"""

print("Ciao, mondo Python!")

print("Il numero è", 4)
print("2 + 2 =", 2 + 2)

name = "Vivian"
print(f"Ciao, {name}! Benvenuto nella programmazione Python.")

user_name = input("Come ti chiami? ")
print(f"Ciao, {user_name}! Benvenuto nella programmazione Python.")

# Generatore di messaggi di benvenuto.
name = input("Come ti chiami? ")
hobby = input("Qual è il tuo hobby preferito? ")

print("\n--- Messaggio di benvenuto ---")
print(f"Ciao, {name}!")
print("Benvenuto nel mondo della programmazione Python.")
print(f"È bello sapere che ti piace {hobby}.")
print("Preparati a costruire qualcosa di interessante oggi.")
