# -*- coding: utf-8 -*-
"""Day 82 — API per servizi AI.

Obiettivo: Separare la logica dell'applicazione dal servizio esterno.
Tutti i messaggi rivolti allo studente sono in italiano.
"""

class ServizioAI:
    def genera_risposta(self, richiesta):
        if not richiesta.strip():
            raise ValueError("La richiesta non può essere vuota.")
        return f"Richiesta ricevuta: {richiesta}"

servizio = ServizioAI()
print(servizio.genera_risposta("Spiega le liste Python."))
