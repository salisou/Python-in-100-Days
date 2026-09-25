# -*- coding: utf-8 -*-
"""Giorno 5 — Cicli for e while.

Obiettivo: capire come ripetere istruzioni in modo controllato.
"""

# Sintassi generale del ciclo for:
# for variabile in range(inizio, fine, passo):
#     istruzioni da ripetere

for i in range(5, 0, -1):
    print(i)

# Sintassi generale del ciclo while:
# while condizione:
#     istruzioni da ripetere

count = 0
while count < 5:
    print(count)
    count += 1

# Esempio con attesa tra le iterazioni.
import time

for i in range(10, 0, -2):
    print(i)
    time.sleep(1)

print("Buon anno!")

# Conto alla rovescia.
start = int(input("Inserisci il numero da cui iniziare il conto alla rovescia: "))

print("\n--- Inizio del conto alla rovescia ---")
while start > 0:
    print(start)
    time.sleep(1)
    start -= 1

print("Conto alla rovescia completato!")
