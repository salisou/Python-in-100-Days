# -*- coding: utf-8 -*-
"""Giorno 10 — File di testo.

Obiettivo: leggere, scrivere e aggiungere contenuto a un file.
"""

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("\nQuesta è una nuova nota.\n")

with open("notes1.txt", "a", encoding="utf-8") as file:
    file.write("\nQuesta è una seconda nota.")


# Applicazione per la gestione delle note.
FILE_NAME = "myNotes.txt"


def mostra_menu():
    print("\n--- Menu gestione note ---")
    print("1. Aggiungi una nuova nota")
    print("2. Visualizza tutte le note")
    print("3. Elimina tutte le note")
    print("4. Esci")


def aggiungi_nota():
    note = input("Inserisci la tua nota: ")
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(note + "\n")
    print("Nota aggiunta correttamente!")


def visualizza_note():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                print("\n--- Le tue note ---")
                print(content)
            else:
                print("\nNessuna nota presente.")
    except FileNotFoundError:
        print("Nessuna nota presente.")


def elimina_note():
    confirm = input("Sei sicuro di voler eliminare tutte le note? (s/n): ")
    if confirm.lower() == "s":
        with open(FILE_NAME, "w", encoding="utf-8"):
            pass
        print("Tutte le note sono state eliminate.")
    else:
        print("Eliminazione annullata.")


while True:
    mostra_menu()
    choice = input("Inserisci la tua scelta (1-4): ")

    if choice == "1":
        aggiungi_nota()
    elif choice == "2":
        visualizza_note()
    elif choice == "3":
        elimina_note()
    elif choice == "4":
        print("Uscita dall'applicazione. Arrivederci!")
        break
    else:
        print("Scelta non valida. Inserisci un numero da 1 a 4.")
