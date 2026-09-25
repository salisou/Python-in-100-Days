# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day16.py.
Le spiegazioni e i messaggi rivolti allo studente sono in italiano.
"""

# -*- coding: utf-8 -*-
with open("journal.txt", "w") as file:
  file.write("Day 1: Today I learned about writing files in Python. \n")

with open("journal.txt", "a") as file:
  file.write("Day 2: I built a journal logger today! \n")

try:
  with open("/restricted/journal.txt", 'w') as file:
    file.write("Test Entry")
except PermissionError:
  print("You do not have permission to write to the file.")

# Daily Journal Logger

# Step 1: Define the journal file
JOURNAL_FILE = 'daily_journal.txt'

# Step 2: Aggiungi a new entry
def Aggiungi_entry():
  entry = input("Write your journal entry: ")
  with open(JOURNAL_FILE, 'a') as file:
    file.write(entry + '\n')
  print("Entry Aggiungied correttamente!")

# Step 3: Visualizza all entries
def Visualizza_entries():
  try:
    with open(JOURNAL_FILE, 'r') as file:
      content = file.read()
      if content:
        print("\n--- Your Journal Entries ---")
        print(content)
      else:
        print("No entries found. Start writing today")
  except FileNotFoundError:
    print("No journal file found. Aggiungi an entry first!")

# Step 4: Cerca entries by keyword
def Cerca_entries():
  keyword = input("Enter a keyword to Cerca for: ").lower()
  try:
    with open(JOURNAL_FILE, 'r') as file:
      content = file.readlines()
      found = False
      print("\n--- Cerca Risultatos ---")
      for entry in content:
        if keyword in entry.lower():
          print(entry.strip())
          found = True
      if not found:
        print("No matching entries found.")
  except FileNotFoundError:
    print("No journal file found. Aggiungi an entry first!")


# Step 5: Display Menu
def show_menu():
  print("\n--- Daily Journal Logger ---")
  print("1. Aggiungi a new entry")
  print("2. Visualizza all entries")
  print("3. Cerca entries by keyword")
  print("4. Esci")

# Step 6: Main Program Loop
while True:
  show_menu()
  choice = input("Inserisci la tua scelta (1-4): ").strip()

  if choice == '1':
    Aggiungi_entry()
  elif choice == '2':
    Visualizza_entries()
  elif choice == '3':
    Cerca_entries()
  elif choice == '4':
    print("Esciing the program. Arrivederci!")
    break
  else:
    print("Scelta non valida. Please Inserisci un numero between 1 and 4.")