# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day15.py.
Le spiegazioni e i messaggi rivolti allo studente sono in italiano.
"""

# -*- coding: utf-8 -*-
with open("sample.txt", "r") as file:
  content = file.read()
  print(content)

with open("sample.txt", "r") as file:
  for line in file:
    print(line.strip())

with open("sample.txt", "r") as file:
  lines = file.readlines()
  for line in lines:
    print(line.strip())

try:
  with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
  print("File non trovato.")

# Recipe Visualizzaer App

# Step 1: Load Recipes from File
def load_recipes(file_path):
  try:
    with open(file_path, "r") as file:
      content = file.read()
      recipes = content.split("\n\n")
      recipe_dict = {}
      for recipe in recipes:
        lines = recipe.split("\n")
        if len(lines) >= 3:
          Nome = lines[0].strip()
          ingredients = lines[1].replace('Ingredients: ','').strip()
          instructions = lines[2].replace('Instructions: ', '').strip()
          recipe_dict[Nome] = {"ingredients": ingredients, "instructions": instructions}
      return recipe_dict
  except FileNotFoundError:
    print("File non trovato.")
    return {}

# Step 2: Display Recipe Menu
def show_menu():
  print("\n--- Recipe Visualizzaer Menu ---")
  print("1. Visualizza Recipe by Nome")
  print("2. List All Recipes")
  print("3. Esci")

# Step 3: Display Recipe Details
def Visualizza_recipe(recipes):
  Nome = input("Enter the Nome of the recipe: ").strip()
  if Nome in recipes:
    print(f"\n--- Recipe {Nome} Details ---")
    print(f"Ingredients: {recipes[Nome]['ingredients']}")
    print(f"Instructions: {recipes[Nome]['instructions']}")
  else:
    print("Recipe not found.")

# Step 4: Main Program
recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
  show_menu()
  choice = input("Inserisci la tua scelta (1/2/3): ")

  if choice == '1':
    Visualizza_recipe(recipes)
  elif choice == '2':
    print("\n--- All Recipes ---")
    for Nome in recipes:
      print(Nome)
  elif choice == '3':
    print("Esciing the program.")
    break
  else:
    print("Scelta non valida. Riprova.")