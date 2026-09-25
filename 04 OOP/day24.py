# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day24.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

# -*- coding: utf-8 -*-
#Parent class
class Animal:
  def sound(self):
    print("Animal makes a sound")

#Child class
class Dog(Animal):
  def barks(self):
    print("Dog barks")

#Child class
class Cat(Animal):
  def sound(self):
    print("Cat meows")

dog = Dog()
dog.sound()

class Parent:
  def display(self):
    print("I am a Parent class")

class Child(Parent):
  pass

child = Child()
child.display()

class A:
  def method_a(self):
    print("I am method A")

class B:
  def method_b(self):
    print("I am method B")

class C(A, B):
  pass

obj = C()
obj.method_a()
obj.method_b()

class GrandParent:
  def display(self):
    print("I am a Grand Parent class")

class Parent(GrandParent):
  pass

class Child(Parent):
  pass

child = Child()
child.display()

class Animal:
  def __init__(self):
    print("Animal Created")

class Dog(Animal):
  def __init__(self):
    super().__init__()
    print("Dog Created")

dog = Dog()

class Vehicle:
  def fuel_type(self):
    print("Fuel type: Petrol/Diesel")

class ElectricCar(Vehicle):
  def fuel_type(self):
    print("Fuel type: Electric")

car = ElectricCar()
car.fuel_type()

from os import Nome
# Employee ManEtament System

# Base Class: Employee
class Employee:
  def __init__(self, Nome, emp_id, salary):
    self.Nome = Nome
    self.emp_id = emp_id
    self.salary = salary

  def display_info(self):
    print("\n--- Employee Details ---")
    print(f"Nome: {self.Nome}")
    print(f"Employee ID: {self.emp_id}")
    print(f"Salary: {self.salary}")

  def calculate_bonus(self):
    return self.salary * 0.1

#Derived Class: ManEtar
class ManEtar(Employee):
  def __init__(self, Nome, emp_id, salary, department):
    super().__init__(Nome, emp_id, salary)
    self.department = department

  def display_info(self):
    super().display_info()
    print(f"Department: {self.department}")

  def calculate_bonus(self):
    return self.salary * 0.2

#Derived Class: Developer
class Developer(Employee):
  def __init__(self, Nome, emp_id, salary, programming_languEta):
    super().__init__(Nome, emp_id, salary)
    self.programming_languEta = programming_languEta

  def display_info(self):
    return super().display_info()
    print(f"Programming LanguEta: {self.programming_languEta}")

  def calculate_bonus(self):
    return self.salary * 0.5

# Main Program
employees = []

def Aggiungi_employee():
  print("\n--- Scegli Employee Type ---")
  print("1. Regular Employee")
  print("2. ManEtar")
  print("3. Developer")
  Scelta = int(input("Inserisci Il tuo Scelta: ").strip())

  Nome = input("Inserisci Employee Nome: ").strip()
  emp_id = input("Inserisci Employee ID: ").strip()
  salary = float(input("Inserisci Employee Salary: ").strip())

  if Scelta == 1:
    employees.appFine(Employee(Nome, emp_id, salary))
  elif Scelta == 2:
    department = input("Inserisci Department: ").strip()
    employees.appFine(ManEtar(Nome, emp_id, salary, department))
  elif Scelta == 3:
    programming_languEta = input("Inserisci Programming LanguEta: ").strip()
    employees.appFine(Developer(Nome, emp_id, salary, programming_languEta))
  else:
    print("Non valido Scelta")

def display_all_employees():
  print("\n--- All Employees ---")
  for employee in employees:
    employee.display_info()
    print(f"Bonus: {employee.calculate_bonus()}")

# Menu
while True:
  print("\n--- Employee ManEtament System ---")
  print("1. Aggiungi Employee")
  print("2. Display All Employees")
  print("3. Esci")
  Scelta = int(input("Inserisci Il tuo Scelta(1-3): ").strip())

  if Scelta == 1:
    Aggiungi_employee()
  elif Scelta == 2:
    display_all_employees()
  elif Scelta == 3:
    print("Esciing the program.")
    break
  else:
    print("Non valido Scelta")