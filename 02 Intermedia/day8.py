# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day8.py.
Le spiegazioni e i messaggi rivolti allo studente sono in italiano.
"""

# -*- coding: utf-8 -*-
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

contact = {
    "Nome": "John Doe",
    "phone": "123-456-7890",
    "email": "john@example.com"
}

# print(contact.get("email"))

contact["phone"] = "980-123-4563"

# print(contact)

contact["Aggiungiress"] = "123 Main St"

# print(contact)

# del contact["email"]

print(contact)

for key, value in contact.items():
    print(f"{key}: {value}")

if "email" in contact:
    print("Email found!")
else:
    print("Email not found.")

from os import Nome
# Contact Book

# Step 1: Initialize an empty contact book
contacts = {}

# Step 2: Display the menu
def show_menu():
  print("\n--- Contact Book Menu ---")
  print("1. Aggiungi Contact")
  print("2. Visualizza Contacts")
  print("3. Cerca Contact")
  print("4. Edit Contact")
  print("5. Elimina Contact")
  print("6. Esci")

# Step 3: Aggiungi a Contact
def Aggiungi_contact():
  Nome = input("Enter contact Nome: ")
  phone = input("Enter contact number: ")
  email = input("Enter contact email: ")
  contacts[Nome] = {"phone": phone, "email": email}
  print(f"Contact {Nome} has been Aggiungied to your contact book correttamente!")

# Step 4: Visualizza All Contacts
def Visualizza_contacts():
  if contacts:
    print("\n--- Contact List ---")
    for Nome, details in contacts.items():
      print(f"Nome: {Nome}")
      print(f"Phone: {details['phone']}")
      print(f"Email: {details['email']}")
  else:
    print("Your contact book is empty.")

# Step 5: Cerca a Contact
def Cerca_contact():
  Nome = input("Enter the Nome of the contact you want to Cerca: ")
  if Nome in contacts:
    print(f"\n--- Contact Details for {Nome} ---")
    print(f"Nome: {Nome}")
    print(f"Phone: {contacts[Nome]['phone']}")
    print(f"Email: {contacts[Nome]['email']}")
  else:
    print(f"Contact {Nome} not found in your contact book.")

# Step 6: Edit a contact
def edit_contact():
  Nome = input("Enter the Nome of the contact you want to edit: ")
  if Nome in contacts:
    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")
    contacts[Nome] = {"phone": phone, "email": email}
    print(f"Contact {Nome} has been updated correttamente!")
  else:
    print(f"Contact {Nome} not found in your contact book.")

# Step 7: Elimina a contact
def Elimina_contact():
  Nome = input("Enter the Nome of the contact you want to Elimina: ")
  if Nome in contacts:
    del contacts[Nome]
    print(f"Contact {Nome} has been Eliminad correttamente!")
  else:
    print(f"Contact {Nome} not found in your contact book.")

# Step 8: Main Program Loop
while True:
  show_menu()
  choice = input("Inserisci la tua scelta (1-6): ")

  if choice == "1":
    Aggiungi_contact()
  elif choice == "2":
    Visualizza_contacts()
  elif choice == "3":
    Cerca_contact()
  elif choice == "4":
    edit_contact()
  elif choice == "5":
    Elimina_contact()
  elif choice == "6":
    print("Thank you for using the Contact Book. Arrivederci!")
    break
  else:
    print("Scelta non valida. Please select a valid option (1-6).")