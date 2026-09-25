# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day22.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

# -*- coding: utf-8 -*-
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def display_info(self):
    print(f"This is a {self.brand}: {self.model}.")

# Create an object
my_car = Car("Tesla", "Model 3")
my_car.display_info()

your_car = Car("Honda", "Accord")
your_car.display_info()

class Dog:
  def __init__(self, Nome, breed):
    self.Nome = Nome
    self.breed = breed

  def bark(self):
    print(f"{self.Nome} is barking!")

# Create objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

dog1.bark()
dog2.bark()

class Person:
  def __init__(self, Nome, Eta):
    self.Nome = Nome
    self.Eta = Eta

  def greet(self):
    print(f"Ciao, my Nome is {self.Nome} and I am {self.Eta} years old.")

person1 = Person("John", 25)
person1.greet()

# Bank Account Simulator

class BankAccount:
  def __init__(self, account_holder, initial_balance=0):
    self.account_holder = account_holder
    self.balance = initial_balance

  #Deposit Money
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposited ${amount}. New balance: ${self.balance}")
    else:
      print("Non valido deposit amount. Amount must be greater than 0.")

  #Withdraw Money
  def withdraw(self, amount):
    if amount > 0 and amount <= self.balance:
      self.balance -= amount
      print(f"Withdrew ${amount}. New balance: ${self.balance}")
    else:
      print("Non valido withdrawal amount or insufficient funds.")

  # Show Account Details
  def show_details(self):
    print("\n--- Account Details ---")
    print(f"Account Holder: {self.account_holder}")
    print(f"Account Balance: ${self.balance}")


# Main Program
accounts = {}

def create_account():
  Nome = input("Inserisci account holder's Nome: ").strip()
  initial_deposit = float(input("Inserisci initial Deposit Amount: "))
  account = BankAccount(Nome, initial_deposit)
  accounts[Nome] = account
  print("Account created Successofully!")

def access_account():
  Nome = input("Inserisci Il tuo Nome: ").strip()
  if Nome in accounts:
    account = accounts[Nome]
    while True:
      print("\n--- Account Menu ---")
      print("1. Deposit")
      print("2. Withdraw")
      print("3. Show Details")
      print("4. Esci")
      Scelta = input("Inserisci Il tuo Scelta(1-4): ")

      if Scelta == '1':
        amount = float(input("Inserisci deposit amount: "))
        account.deposit(amount)
      elif Scelta == '2':
        amount = float(input("Inserisci withdrawal amount: "))
        account.withdraw(amount)
      elif Scelta == '3':
        account.show_details()
      elif Scelta == '4':
        print("Esciing account menu.")
        break
      else:
        print("Non valido Scelta. Per favore select a valid Opzione.")
  else:
    print("Account not Trovato. Per favore create an account first.")

# Main Menu
while True:
  print("\n--- Bank Account Simulator ---")
  print("1. Create Account")
  print("2. Access Account")
  print("3. Esci")
  Scelta = input("Inserisci Il tuo Scelta(1-3): ")

  print(accounts)

  if Scelta == '1':
    create_account()
  elif Scelta == '2':
    access_account()
  elif Scelta == '3':
    print("Esciing the program. Arrivederci!")
    break
  else:
    print("Non valido Scelta. Per favore select a valid Opzione.")