# -*- coding: utf-8 -*-
"""Day 93 — Validazione.

Materiale didattico in italiano.
"""

def crea_utente(nome):
    nome = nome.strip()
    if len(nome) < 2:
        raise ValueError("Il nome deve contenere almeno due caratteri.")
    return {"nome": nome}

try:
    print(crea_utente(input("Nome: ")))
except ValueError as errore:
    print(f"Errore di validazione: {errore}")
