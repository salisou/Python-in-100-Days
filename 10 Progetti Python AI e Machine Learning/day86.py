# -*- coding: utf-8 -*-
"""Day 86 — Performance.

Obiettivo: Misurare il tempo prima di ottimizzare.
Tutti i messaggi rivolti allo studente sono in italiano.
"""

from time import perf_counter

inizio = perf_counter()
totale = sum(range(1_000_000))
durata = perf_counter() - inizio
print(f"Totale: {totale}")
print(f"Tempo di esecuzione: {durata:.6f} secondi")
