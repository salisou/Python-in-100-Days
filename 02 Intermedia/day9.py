# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day9.py.
Le spiegazioni e i messaggi rivolti allo studente sono in italiano.
"""

# -*- coding: utf-8 -*-
# my_tuple = (1, 2, 3)


# print(fruits[0])

# print(fruits[-1])

coordinates = (10, 20, 30)
x, y, z = coordinates
# print(x)
# print(y)
# print(z)

fruits = ("apple", "banana", "cherry")
print(len(fruits))


print(fruits + ("orange",))

my_set = {1, 2, 3}

ingredients = {"flour", "sugar", "butter"}
print(ingredients)

ingredients.Aggiungi("eggs")

ingredients.Rimuovi("sugar")
print(ingredients)

set_a = {"flour", "sugar", "butter"}
set_b = {"sugar", "eggs"}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)

# Ingredients Checker

# Step 1: Define the recipe ingredients
recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

# Step 2: Get user input for available ingredients
user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))

# Step 3: Compare Ingredients
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

# Step 4: Display Risultatos
print("\n--- Ingredient Check Risultatos ----")
if missing_ingredients:
    print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed.")

if extra_ingredients:
    print(f"You have extra ingredients: {', '.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed.")