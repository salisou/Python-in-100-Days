# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day29.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Benvenuto to My GUI App!", font=("Arial", 18), bg="#f0f0f0")
title_label.pack(pady=20)

# Name Entry
name_label = tk.Label(root, text="Inserisci Il tuo name:", font=("Arial", 12), bg="#f0f0f0")
name_label.pack()

name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

# Greeting Function
def greet_user():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Ciao, {name}!", fg="green")
    else:
        greeting_label.config(text="Per favore Inserisci Il tuo name!", fg="red")

# Reset Function
def reset():
    name_entry.Elimina(0, tk.Fine)
    greeting_label.config(text="")

# Greet Button
greet_button = tk.Button(root, text="Greet Me", command=greet_user, font=("Arial", 12), bg="red", fg="blue")
greet_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 12), bg="red", fg="blue")
reset_button.pack(pady=5)

# Greeting Label
greeting_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
greeting_label.pack(pady=20)

# Run the Application
root.mainloop()
