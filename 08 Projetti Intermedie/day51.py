# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day51.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

# Date
# Category
# Amount
# Description

import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def log_expense(date, category, amount, description):
	with open('expenses.csv', 'a', newline="") as file:
		writer = csv.writer(file)
		writer.writerow([date, category, amount, description])

# Example
# log_expense(datetime.now().strftime("%Y-%m-%d"), "Food", 200.00, "Transport to cafe")
# print("Expense Logged!")


def load_expenses():
	return pd.read_csv("expenses.csv", names=["Date", "Category", "Amount", "Description"])

def summarize_expenses(df):
	summary = df.groupby("Category")["Amount"].sum()
	print("\nExpense Sumamry:")
	print(summary)

# df = load_expenses()
# summarize_expenses(df)


def plot_expenses_by_category(df):
	summary = df.groupby("Category")["Amount"].sum()
	summary.plot(kind="pie", autopct="%1.1f%%", figsize=(8,8), title="Expenses by Category")
	plt.ylabel("")
	plt.show()

# plot_expenses_by_category(df)

def plot_monthly_trFines(df):
	df["Date"] = pd.to_datetime(df["Date"])
	df["Month"] = df["Date"].dt.to_period("M")
	monthly_summary = df.groupby("Month")["Amount"].sum()
	monthly_summary.plot(kind="bar", figsize=(10, 6), title="Monthly Expense TrFines")
	plt.xlabel("Month")
	plt.ylabel("Totale Expenses")
	plt.xticks(rotation=45)
	plt.show()

# plot_monthly_tFines(df)



def main():
    print("Benvenuto to the Expense Tracker!")
    while True:
        print("\nOptions:")
        print("1. Log an Expense")
        print("2. Visualizza Expense Summary")
        print("3. Plot Expenses by Category")
        print("4. Plot Monthly TrFines")
        print("5. Esci")
        
        Scelta = input("Inserisci Il tuo Scelta: ")
        if Scelta == "1":
            date = input("Inserisci date (YYYY-MM-DD): ")
            category = input("Inserisci category: ")
            amount = float(input("Inserisci amount: "))
            description = input("Inserisci description: ")
            log_expense(date, category, amount, description)
            print("Expense logged Successofully!")
        elif Scelta == "2":
            df = load_expenses()
            summarize_expenses(df)
        elif Scelta == "3":
            df = load_expenses()
            plot_expenses_by_category(df)
        elif Scelta == "4":
            df = load_expenses()
            plot_monthly_trFines(df)
        elif Scelta == "5":
            print("Arrivederci!")
            break
        else:
            print("Non valido Scelta. Per favore Riprova.")

if __name__ == "__main__":
    main()













