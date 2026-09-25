# -*- coding: utf-8 -*-
"""Giorno 3 — Conversione dei tipi e operatori aritmetici.

Obiettivo: usare int(), str(), float() e gli operatori matematici.
"""

name = input("Inserisci il tuo nome: ")
print(f"Ciao, {name}.")

num1 = int(input("Inserisci un numero: "))
print(f"Il numero trasformato in testo due volte è: {str(num1) * 2}")

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))
result = num1 + num2
print(f"La somma di {num1} e {num2} è {result}.")

a = 5
b = 3
print(f"Addizione: {a + b}")
print(f"Sottrazione: {a - b}")
print(f"Moltiplicazione: {a * b}")
print(f"Divisione: {a / b}")
print(f"Divisione intera: {a // b}")
print(f"Resto: {a % b}")
print(f"Potenza: {a ** b}")

# Calcolatrice semplice.
number1 = float(input("Inserisci il primo numero: "))
number2 = float(input("Inserisci il secondo numero: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2 if number2 != 0 else "Impossibile dividere per zero"

print("\n--- Risultati della calcolatrice ---")
print(f"Addizione: {number1} + {number2} = {addition}")
print(f"Sottrazione: {number1} - {number2} = {subtraction}")
print(f"Moltiplicazione: {number1} x {number2} = {multiplication}")
print(f"Divisione: {number1} / {number2} = {division}")
