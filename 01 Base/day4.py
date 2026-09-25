# -*- coding: utf-8 -*-
"""Giorno 4 — Condizioni e operatori logici.

Obiettivo: prendere decisioni usando if, elif, else, or e confronti.
"""

number = 4

if number > 5:
    print("Il numero è maggiore di 5.")
elif number == 5:
    print("Il numero è uguale a 5.")
elif number == 4:
    print("Il numero è uguale a 4.")
else:
    print("Il numero è minore di 5.")

a = 2
b = 20

if a > 5 or b < 15:
    print("Almeno una delle due condizioni è vera.")
else:
    print("Entrambe le condizioni sono false.")

# Strumento di confronto tra due numeri.
num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

print("\n--- Risultati del confronto ---")

if num1 == num2:
    print(f"I due numeri sono uguali: {num1}.")
elif num1 > num2:
    print(f"{num1} è maggiore di {num2}.")
else:
    print(f"{num2} è maggiore di {num1}.")

if num1 == 0 or num2 == 0:
    print("Almeno uno dei due numeri è zero.")
else:
    print("Entrambi i numeri sono diversi da zero.")
