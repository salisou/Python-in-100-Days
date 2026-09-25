# -*- coding: utf-8 -*-
"""Giorno 6 — Funzioni.

Obiettivo: definire funzioni, passare argomenti e restituire valori.
"""

def saluta():
    print("Ciao dalla funzione!")

saluta()


def saluta_utente(name):
    print(f"Ciao, {name}! Benvenuto in Python.")

saluta_utente("Vivian")


def add(a, b):
    print(f"La somma è: {a + b}")

add(5, 4)


def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Il risultato è:", result)


# Quiz matematico.
import random


def genera_domanda():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    return f"{num1} {operator} {num2}", answer


def quiz_matematico():
    score = 0
    rounds = 5

    print("\n--- Quiz matematico ---")
    print("Risolvi i problemi e inserisci la risposta corretta.")

    for i in range(rounds):
        question, correct_answer = genera_domanda()
        print(f"\nDomanda {i + 1}: {question}")
        user_answer = int(input("La tua risposta: "))

        if user_answer == correct_answer:
            print("Corretto!")
            score += 1
        else:
            print(f"Sbagliato! La risposta corretta è: {correct_answer}")

    print("\n--- Fine del quiz ---")
    print(f"Il tuo punteggio finale è: {score}/{rounds}.")

    if score == rounds:
        print("Complimenti! Hai risposto correttamente a tutte le domande.")
    elif score >= rounds // 2:
        print("Bravo! Hai svolto un buon lavoro.")
    else:
        print("Continua ad allenarti: la prossima volta puoi fare ancora meglio.")


quiz_matematico()
