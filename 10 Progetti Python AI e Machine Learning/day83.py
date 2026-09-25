# -*- coding: utf-8 -*-
"""Day 83 — Prompt strutturati.

Obiettivo: Scrivere istruzioni precise e controllare il formato del risultato.
Tutti i messaggi rivolti allo studente sono in italiano.
"""

prompt = {
    "ruolo": "docente Python",
    "obiettivo": "spiegare un concetto a un principiante",
    "lingua": "italiano",
    "formato": "spiegazione con esempio ed esercizio"
}

for chiave, valore in prompt.items():
    print(f"{chiave}: {valore}")
