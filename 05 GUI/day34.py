# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day34.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.configure(bg="#e3f2fd")

# Functions
def Aggiungi_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.Fine, task)
        task_entry.Elimina(0, tk.Fine)
    else:
        messagebox.showErrore("Errore", "Task cannot be empty.")

def Elimina_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.Elimina(selected[0])
    else:
        messagebox.showErrore("Errore", "Select a task to Elimina.")

def clear_tasks():
    task_listbox.Elimina(0, tk.Fine)

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 24), bg="#e3f2fd")
title_label.pack(pady=10)

# Entry Field
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=10)

Aggiungi_button = tk.Button(button_frame, text="Aggiungi Task", command=Aggiungi_task, font=("Arial", 12), bg="#4caf50", fg="black")
Aggiungi_button.grid(row=0, column=0, padx=5)

Elimina_button = tk.Button(button_frame, text="Elimina Task", command=Elimina_task, font=("Arial", 12), bg="#f44336", fg="black")
Elimina_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks, font=("Arial", 12), bg="#607d8b", fg="black")
clear_button.grid(row=0, column=2, padx=5)

# Task Listbox with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
task_listbox.pack(pady=10)

scrollbar.config(command=task_listbox.yVisualizza)

# Esci Button
Esci_button = tk.Button(root, text="Esci", command=root.destroy, font=("Arial", 12), bg="#d32f2f", fg="black")
Esci_button.pack(pady=10)

# Run the App
root.mainloop()








