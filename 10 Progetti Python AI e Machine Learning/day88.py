# -*- coding: utf-8 -*-
"""Day 88 — Programmazione asincrona con asyncio."""
import asyncio

async def saluta(nome):
    await asyncio.sleep(0.1)
    return f"Ciao {nome}"

async def main():
    risultati = await asyncio.gather(saluta("Anna"), saluta("Marco"))
    for risultato in risultati:
        print(risultato)

asyncio.run(main())
