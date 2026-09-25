# -*- coding: utf-8 -*-
"""Day 91 — Mappatura a oggetti.

Materiale didattico in italiano.
"""

class Studente:
    def __init__(self, nome):
        self.nome = nome

studente = Studente("Anna")
print(f"Studente: {studente.nome}")
