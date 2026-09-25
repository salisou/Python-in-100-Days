# -*- coding: utf-8 -*-
"""Giorno 2 — Variabili, tipi di dati e conversioni.

Obiettivo: distinguere stringhe, interi, numeri decimali e booleani.
"""

name = "Vivian"
age = 42
height = 5.8
is_student = False

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

age_testo = "42"
my_age = int(age_testo)
print(my_age + 5)

print(f"Ciao, {name}!")
print("Ciao, {}!".format(name))

# Programma di saluto personalizzato.
name = input("Come ti chiami? ")
age = int(input("Quanti anni hai? "))
color = input("Qual è il tuo colore preferito? ")

print("\n--- Saluto personalizzato ---")
print(f"Ciao, {name}!")
print(f"Hai {age} anni e {color} è un bellissimo colore.")
print("Ora sei pronto per iniziare il tuo percorso con Python.")
