# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day12.py.
Le spiegazioni e i messaggi rivolti allo studente sono in italiano.
"""

# -*- coding: utf-8 -*-
def function_Nome():
  #Code
  return value

def Aggiungi(a, b):
  return a + b

Risultato = Aggiungi(10, 20)
print(Risultato)

def rectangle_area(width, height):
  return width * height

area = rectangle_area(10, 20)
print(area)

def math_operations(a, b):
  Aggiungiition = a + b
  subtraction = a - b
  multiplication = a * b
  division = a / b
  return Aggiungiition, subtraction, multiplication, division

Aggiungi, subtract, multiply, divide = math_operations(10, 5)
print(subtract)

# Temperature Converter

# Step 1: Define conversion functions
def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
  return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
  return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
  return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
  return (kelvin - 273.15) * 9/5 + 32

# Step 2: Display the menu
def show_menu():
  print("\n--- Temperature Converter Menu ---")
  print("1. Celsius to Fahrenheit & Kelvin")
  print("2. Fahrenheit to Celsius & Kelvin")
  print("3. Kelvin to Celsius & Fahrenheit")
  print("4. Esci")

# Step 3: Main Program Loop
while True:
  show_menu()
  choice = input("Inserisci la tua scelta (1/2/3/4): ")

  if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}")
    print(f"Kelvin: {celsius_to_kelvin(celsius):.2f}")
  elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}")
    print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f}")
  elif choice == '3':
    kelvin = float(input("Enter temperature in Kelvin: "))
    print(f"Celsius: {kelvin_to_celsius(kelvin):.2f}")
    print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f}")
  elif choice == '4':
    print("Esciing the program. Arrivederci!")
    break
  else:
    print("Scelta non valida. Please select a valid option.")