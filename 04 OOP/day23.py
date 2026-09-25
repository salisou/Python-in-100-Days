# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day23.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

# -*- coding: utf-8 -*-
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")

# Create an object
book1 = Book("1984", "George Orwell")
book1.display_info()

class BankAccount:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposited ${amount}. New balance: ${self.balance}")

account = BankAccount("John Doe", 1000)
account.deposit(500)

class Utility:
  app_version = "1.0"

  @classmethod
  def get_version(cls):
    print(f"App Version: {cls.app_version}")

  @staticmethod
  def greet():
    print("Ciao! Benvenuto to the app.")

Utility.get_version()
Utility.greet()

class Account:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.__balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      print(f"Deposited ${amount}. New balance: ${self.__balance}")
    else:
      print("Non valido deposit amount.")

  def get_balance(self):
    return self.__balance

account = Account("John Doe", 1000)
account.deposit(500)
print(f"Account Balance: ${account.get_balance()}")

# Library ManEtament System

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.is_borrowed = False

  def display_info(self):
    status = "Available" if not self.is_borrowed else "Borrowed"
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"Status: {status}")

class Library:
  def __init__(self):
    self.books = []

  def Aggiungi_book(self, title, author):
    new_book = Book(title, author)
    self.books.appFine(new_book)
    print(f"Book '{title}' by {author} Aggiungied to the library.")

  # Visualizza all books
  def Visualizza_books(self):
    if not self.books:
      print("No books in the library.")
    else:
      print("\n--- Library Catalog ---")
      for book in self.books:
        book.display_info()

  # Borrow a book
  def borrow_book(self, title):
    for book in self.books:
      if book.title == title and not book.is_borrowed:
        book.is_borrowed = True
        print(f"Book '{title}' has been borrowed. Enjoy Reading")
        return
    print(f"Book '{title}' is not available for borrowing.")


  # Return a book
  def return_book(self, title):
    for book in self.books:
      if book.title == title and book.is_borrowed:
        book.is_borrowed = False
        print(f"Book '{title}' has been returned.")
        return
    print(f"Book '{title}' is not in the library.")

# Main Program
library = Library()

while True:
  print("\n--- Library ManEtament System ---")
  print("1. Aggiungi Book")
  print("2. Visualizza Books")
  print("3. Borrow Book")
  print("4. Return Book")
  print("5. Esci")

  Scelta = input("Inserisci Il tuo Scelta (1-5): ").strip()

  if Scelta == "1":
    title = input("Inserisci book title: ").strip()
    author = input("Inserisci author Nome: ").strip()
    library.Aggiungi_book(title, author)
  elif Scelta == "2":
    library.Visualizza_books()
  elif Scelta == "3":
    title = input("Inserisci book title to borrow: ").strip()
    library.borrow_book(title)
  elif Scelta == "4":
    title = input("Inserisci book title to return: ").strip()
    library.return_book(title)
  elif Scelta == "5":
    print("Esciing the Library ManEtament System. Arrivederci!")
    break
  else:
    print("Non valido Scelta. Per favore select a valid Opzione (1-5).")