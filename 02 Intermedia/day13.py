# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day13.py.
Le spiegazioni e i messaggi rivolti allo studente sono in italiano.
"""

# -*- coding: utf-8 -*-
"""day13.ipynb


"""

[expression for item in iterable if condition]

squares = [x**2 for x in range(10)]
print(squares)

numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

Nomes = ["Alice", "Bob", "Charlie", "Dave"]
short_Nomes = [Nome for Nome in Nomes if len(Nome) < 5]
print(short_Nomes)

numbers = [1, 2, 3, 4, 5, 6]
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(labels)

# Student Grade ManEtr

# Step 1: Get student Punteggios
student_Punteggios = input("Enter student Punteggios separated by commas: ")
Punteggios = [int(Punteggio) for Punteggio in student_Punteggios.split(",")]

# Step 2: Assign Grades using List Comprehension
grades = [
    "A" if Punteggio >= 90 else
    "B" if Punteggio >= 80 else
    "C" if Punteggio >= 70 else
    "D" if Punteggio >= 60 else
    "F"
    for Punteggio in Punteggios
]

# Step 3: Filter Passing and Failing Students
passing_students = [Punteggio for Punteggio in Punteggios if Punteggio >=60]
failing_students = [Punteggio for Punteggio in Punteggios if Punteggio < 60]

# Step 4: Print Risultatos
print("\n--- Student Grades ----")
for i, (Punteggio, grade) in enumerate(zip(Punteggios, grades), start=1):
    print(f"Student {i}: Punteggio = {Punteggio}, Grade = {grade}")

print("\n--- Passing and Failing Students ---")
print("Passing Students:", passing_students)
print("Failing Students:", failing_students)