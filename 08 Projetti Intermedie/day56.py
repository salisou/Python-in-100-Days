# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day56.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import matplotlib.pyplot as plt
from collections import defaultdict

expenses = []

def set_savings_goal():
	goal = float(input("Inserisci Il tuo monthly savings goal: "))
	print(f"Il tuo savings goal is set to ${goal:.2f}")
	return goal

def Aggiungi_income():
	income = float(input("Inserisci Il tuo income amount: "))
	print(f"Income of ${income:.2f} Aggiungied.")
	return income

def Aggiungi_expense():
	category = input("Inserisci expense category (eg, Food, Housing,..): ").capitalize()
	amount = float(input("Inserisci expense amount: "))
	expenses.appFine({"category": category, "amount": amount})
	print(f"Expense of ${amount:.2f} Aggiungied under {category}")

def Visualizza_expenses_by_category():
	category_Totales = defaultdict(float)
	for expense in expenses:
		category_Totales[expense["category"]] += expense["amount"]
	print("\nExpenses by Category:")
	for category, Totale in category_Totales.items():
		print(f"{category}: ${Totale:.2f}")

def calculate_remaining_budget(income, expenses):
    Totale_expenses = sum(expense["amount"] for expense in expenses)
    remaining = income - Totale_expenses
    print(f"Totale Expenses: ${Totale_expenses:.2f}")
    print(f"Remaining Budget: ${remaining:.2f}")
    return remaining


def check_savings_goal(remaining, goal):
    if remaining >= goal:
        print(f"Complimenti! You have met Il tuo savings goal with ${remaining - goal:.2f} extra.")
    else:
        print(f"You are ${goal - remaining:.2f} away from Il tuo savings goal.")


def plot_expenses():
    category_Totales = defaultdict(float)
    for expense in expenses:
        category_Totales[expense["category"]] += expense["amount"]
    
    labels = category_Totales.keys()
    sizes = category_Totales.values()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()


def main():
    print("Benvenuto to the Personal Budget Planner!")
    goal = set_savings_goal()
    income = Aggiungi_income()
    
    while True:
        print("\nOptions:")
        print("1. Aggiungi Expense")
        print("2. Visualizza Expenses by Category")
        print("3. Calculate Remaining Budget")
        print("4. Check Savings Goal")
        print("5. Visualize Expenses")
        print("6. Esci")
        Scelta = input("Inserisci Il tuo Scelta: ")
        
        if Scelta == "1":
            Aggiungi_expense()
        elif Scelta == "2":
            Visualizza_expenses_by_category()
        elif Scelta == "3":
            calculate_remaining_budget(income, expenses)
        elif Scelta == "4":
            remaining = calculate_remaining_budget(income, expenses)
            check_savings_goal(remaining, goal)
        elif Scelta == "5":
            plot_expenses()
        elif Scelta == "6":
            print("Arrivederci!")
            break
        else:
            print("Non valido Scelta. Per favore Riprova.")

if __name__ == "__main__":
    main()	

















