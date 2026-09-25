# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day11.py.
Le spiegazioni e i messaggi rivolti allo studente sono in italiano.
"""

# -*- coding: utf-8 -*-
try:
  num = int(input("Inserisci un numero:"))
  Risultato = 10 / num
  print("Risultato: ", Risultato)
except ZeroDivisionError:
  print("Error: Division by zero is not allowed.")
except ValueError:
  print("Error: Invalid input. Please enter a valid number.")

try:
  # Code that might raise an exception
except ExceptionType:
  # Code to handle the exception
else:
  # Execute if no exception occurs
finally:
  # Always execute, even if an exception occurs

try:
  num = int(input("Inserisci un numero:"))
  Risultato = 10 / num
except ZeroDivisionError:
  print("Error: Division by zero is not allowed.")
else:
  print("No exception occurred. Risultato: ", Risultato)
finally:
  print("Finally block executed. Program Ended")

try:
  num = int(input("Inserisci un numero:"))
  Risultato = 10 / num
except (ZeroDivisionError, ValueError):
  print("Error: Division by zero or Invalid Input")

def withdraw(amount):
  if amount < 0:
    raise ValueError("Invalid withdrawal amount - Amount cannot be negative")
  print(f"You have withdrawn ${amount}")

try:
  withdraw(-50)
except ValueError as e:
  print(e)

# Safe Calculator

# Step 1: Define Calculator Functions
def Aggiungi(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    raise ZeroDivisionError("Cannot divide by zero")
  return x / y

# Step 2: Display Menu
def show_menu():
  print("\n--- Safe Calculator Menu ---")
  print("1. Aggiungi")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Esci")

# Step 3: Main Program
while True:
  show_menu()
  choice = input("Inserisci la tua scelta (1-5): ")

  if choice == '5':
    print("Esciing the calculator. Arrivederci!")
    break

  try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
      print("Risultato:", Aggiungi(num1, num2))
    elif choice == '2':
      print("Risultato:", subtract(num1, num2))
    elif choice == '3':
      print("Risultato:", multiply(num1, num2))
    elif choice == '4':
      print("Risultato:", divide(num1, num2))
    else:
      print("Scelta non valida. Please select a valid option.")

  except ValueError:
    print("Invalid input. Please enter valid numbers.")
  except ZeroDivisionError as e:
    print(f"Error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    print("Thank you for using the Safe Calculator!... Restarting...")