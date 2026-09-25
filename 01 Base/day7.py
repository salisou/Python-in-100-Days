# -*- coding: utf-8 -*-
"""Giorno 7 — Liste.

Obiettivo: creare, leggere, modificare e scorrere una lista.
"""

shopping_list = []

def mostra_menu():
    print("\n--- Menu lista della spesa ---")
    print("1. Visualizza la lista")
    print("2. Aggiungi un elemento")
    print("3. Rimuovi un elemento")
    print("4. Svuota la lista")
    print("5. Esci")


while True:
    mostra_menu()
    choice = input("Inserisci la tua scelta (1-5): ")

    if choice == "1":
        print("\n--- Lista della spesa ---")
        if not shopping_list:
            print("La lista della spesa è vuota.")
        else:
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")

    elif choice == "2":
        item = input("Inserisci l'elemento da aggiungere: ").strip()
        if item:
            shopping_list.append(item)
            print(f"{item} è stato aggiunto alla lista della spesa.")
        else:
            print("Non hai inserito alcun elemento.")

    elif choice == "3":
        item = input("Inserisci l'elemento da rimuovere: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} è stato rimosso dalla lista della spesa.")
        else:
            print(f"{item} non è presente nella lista della spesa.")

    elif choice == "4":
        shopping_list.clear()
        print("La lista della spesa è stata svuotata.")

    elif choice == "5":
        print("Arrivederci!")
        break

    else:
        print("Scelta non valida. Riprova.")
