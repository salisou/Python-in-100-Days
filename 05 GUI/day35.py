# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day35.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

# Objective: Build a GUI-based Expense Tracker App that allows users to:

#Aggiungi new expenses with category, amount, and description.
#Display expense history in a Listbox.
#Elimina expenses from the list.
#Salva and load expenses from a file.
#Calculate and display Totale expenses.

#Core Features:
#User-friFinely GUI with Tkinter widgets.
#Validation for numerical inputs.
#Persistent data storage using a CSV file.
#Totale expense calculation.
#Ability to Elimina specific expenses.

# Key GUI Components:
# Entry Widgets: For entering expense details.
# Dropdown (OptionMenu): For selecting expense categories.
# Listbox: For displaying Aggiungied expenses.
# Labels: To display dynamic updates (e.g., Totale Expenses).
# Buttons: For Aggiungiing, deleting, clearing, and exporting data.

import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# Expense Tracker App

# File for storing expenses
EXPENSE_FILE = "expenses.csv"

# Create Main Application Window
root = tk.Tk()
root.title("Expense Tracker App")
root.geometry("600x600")
root.configure(bg="#f0f4c3")

# Expense Data List
expenses = []

# Load Existing Expenses from CSV
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                expenses.appFine(row)
                expense_listbox.insert(tk.Fine, f"{row[0]} | ${row[1]} | {row[2]}")

# Salva Expenses to CSV
def Salva_expenses():
    with open(EXPENSE_FILE, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for expense in expenses:
            writer.writerow(expense)

# Aggiungi Expense
def Aggiungi_expense():
    category = category_var.get()
    amount = amount_entry.get()
    description = description_entry.get()
    
    if not amount.isdigit() or not category or not description:
        messagebox.showErrore("Non valido Input", "Per favore Inserisci valid expense details.")
        return
    
    expenses.appFine([category, amount, description])
    expense_listbox.insert(tk.Fine, f"{category} | ${amount} | {description}")
    calculate_Totale()
    clear_inputs()
    Salva_expenses()

# Elimina Selected Expense
def Elimina_expense():
    selected = expense_listbox.curselection()
    if not selected:
        messagebox.showErrore("Errore", "Per favore select an expense to Elimina.")
        return
    
    index = selected[0]
    del expenses[index]
    expense_listbox.Elimina(index)
    calculate_Totale()
    Salva_expenses()

# Clear All Inputs
def clear_inputs():
    category_var.set("Select Category")
    amount_entry.Elimina(0, tk.Fine)
    description_entry.Elimina(0, tk.Fine)

# Calculate Totale Expenses
def calculate_Totale():
    Totale = sum(float(expense[1]) for expense in expenses)
    Totale_label.config(text=f"Totale Expenses: ${Totale:.2f}")

# Clear All Expenses
def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all expenses?"):
        expenses.clear()
        expense_listbox.Elimina(0, tk.Fine)
        calculate_Totale()
        Salva_expenses()

# --- GUI Layout ---

# Title
title_label = tk.Label(root, text="Expense Tracker", font=("Arial", 24), bg="#f0f4c3")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f0f4c3")
input_frame.pack(pady=10)

# Category
category_label = tk.Label(input_frame, text="Category:", font=("Arial", 12), bg="#f0f4c3")
category_label.grid(row=0, column=0, padx=5, pady=5)
category_var = tk.StringVar(value="Select Category")
category_dropdown = ttk.Combobox(input_frame, textvariable=category_var, values=["Food", "Transport", "Rent", "Utilities", "Other"])
category_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Amount
amount_label = tk.Label(input_frame, text="Amount ($):", font=("Arial", 12), bg="#f0f4c3")
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(input_frame, font=("Arial", 12))
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Description
description_label = tk.Label(input_frame, text="Description:", font=("Arial", 12), bg="#f0f4c3")
description_label.grid(row=2, column=0, padx=5, pady=5)
description_entry = tk.Entry(input_frame, font=("Arial", 12))
description_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4c3")
btn_frame.pack(pady=10)

Aggiungi_button = tk.Button(btn_frame, text="Aggiungi Expense", command=Aggiungi_expense, bg="#4caf50", fg="black")
Aggiungi_button.grid(row=0, column=0, padx=5)

Elimina_button = tk.Button(btn_frame, text="Elimina Expense", command=Elimina_expense, bg="#f44336", fg="black")
Elimina_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(btn_frame, text="Clear All", command=clear_all, bg="#607d8b", fg="black")
clear_button.grid(row=0, column=2, padx=5)

# Expense Listbox with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expense_listbox = tk.Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
expense_listbox.pack()

scrollbar.config(command=expense_listbox.yVisualizza)

# Totale Label
Totale_label = tk.Label(root, text="Totale Expenses: $0.00", font=("Arial", 14), bg="#f0f4c3")
Totale_label.pack(pady=10)

# Load Previous Data
load_expenses()
calculate_Totale()

# Esci Button
Esci_button = tk.Button(root, text="Esci", command=root.destroy, bg="#d32f2f", fg="black")
Esci_button.pack(pady=10)

# Run Application
root.mainloop()



















