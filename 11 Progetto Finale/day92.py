# -*- coding: utf-8 -*-
"""Day 92 — Architettura.

Materiale didattico in italiano.
"""

class Repository:
    def salva(self, valore):
        print(f"Salvataggio: {valore}")

class Servizio:
    def __init__(self, repository):
        self.repository = repository

    def crea(self, valore):
        self.repository.salva(valore)

Servizio(Repository()).crea("Nuovo elemento")
