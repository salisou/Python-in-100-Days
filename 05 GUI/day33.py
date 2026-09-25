# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day33.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Simple Login System")
root.geometry("400x300")
root.configure(bg="#f0f4c3")

# Predefined Credentials
USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "user123"
}

# Title Label
title_label = tk.Label(root, text="Login System", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

# Username Input
username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="#f0f4c3")
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

# Password Input
password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="#f0f4c3")
password_label.pack()
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Successo", f"Benvenuto, {username}!")
    else:
        messagebox.showErrore("Login Failed", "Non valido username or password.")

# Clear Function
def clear():
    username_entry.Elimina(0, tk.Fine)
    password_entry.Elimina(0, tk.Fine)

# Buttons
login_button = tk.Button(root, text="Login", command=login, font=("Arial", 12), bg="#4CAF50", fg="black")
login_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear, font=("Arial", 12), bg="#f44336", fg="black")
clear_button.pack(pady=5)

# Esci Button
Esci_button = tk.Button(root, text="Esci", command=root.destroy, font=("Arial", 12), bg="#607d8b", fg="black")
Esci_button.pack(pady=10)

# Run the App
root.mainloop()











