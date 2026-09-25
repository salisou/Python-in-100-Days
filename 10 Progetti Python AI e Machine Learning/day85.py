# -*- coding: utf-8 -*-
"""Day 85 — Sicurezza applicativa.

Obiettivo: Non inserire segreti nel codice e validare l'input.
Tutti i messaggi rivolti allo studente sono in italiano.
"""

import os

chiave = os.getenv("SERVIZIO_API_KEY")
if chiave:
    print("Chiave configurata correttamente nell'ambiente.")
else:
    print("Chiave non configurata: usa una variabile d'ambiente.")
