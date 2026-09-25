# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day30.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Click Counter App")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

# Counter Variable
counter = 0

# Increment Function
def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")

# Reset Function
def reset():
    global counter
    counter = 0
    counter_label.config(text="Clicks: 0")

# Title Label
title_label = tk.Label(root, text="Click Counter", font=("Arial", 20), bg="#e3f2fd")
title_label.pack(pady=20)

# Counter Label
counter_label = tk.Label(root, text="Clicks: 0", font=("Arial", 16), bg="#e3f2fd")
counter_label.pack(pady=10)

# Increment Button
increment_button = tk.Button(root, text="Click Me", command=increment, font=("Arial", 14), bg="#4caf50", fg="black")
increment_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 14), bg="#f44336", fg="black")
reset_button.pack(pady=10)

# Esci Button
Esci_button = tk.Button(root, text="Esci", command=root.destroy, font=("Arial", 14), bg="#607d8b", fg="black")
Esci_button.pack(pady=20)

# Run the App
root.mainloop()















