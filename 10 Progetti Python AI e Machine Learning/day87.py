# -*- coding: utf-8 -*-
"""Day 87 — Concorrenza.

Obiettivo: Distinguere esecuzione sequenziale e attività concorrenti.
Tutti i messaggi rivolti allo studente sono in italiano.
"""

from concurrent.futures import ThreadPoolExecutor


def elabora(numero):
    return numero * numero

with ThreadPoolExecutor(max_workers=3) as executor:
    risultati = list(executor.map(elabora, [2, 3, 4, 5]))

print(f"Risultati: {risultati}")
