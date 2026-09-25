# -*- coding: utf-8 -*-
"""Day 81 — AI applicativa.

Obiettivo: Validare sempre gli output di un sistema AI.
Tutti i messaggi rivolti allo studente sono in italiano.
"""

def valida_output(testo):
    return bool(testo and testo.strip())

risposta = input("Inserisci una risposta da verificare: ")
print("Risposta valida." if valida_output(risposta) else "Risposta vuota o non valida.")
