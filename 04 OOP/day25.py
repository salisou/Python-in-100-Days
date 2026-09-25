# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day25.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

# -*- coding: utf-8 -*-
class Animal:
  def make_sound(self):
    print("The animal makes a sound")

class Dog(Animal):
  def make_sound(self):
    print("The dog barks")

class Cat(Animal):
  def make_sound(self):
    print("The cat meows")

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
  animal.make_sound()

class Shape:
  def area(self):
    print("Calculating area...")

class Circle(Shape):
  def area(self):
    print("Area of a Circle: pi*r*r")

class Square(Shape):
  def area(self):
    print("Area of a Square: side*side")

# Polymorphism in action
shapes = [Circle(), Square()]

for shape in shapes:
  shape.area()

class Bird:
  def make_sound(self):
    print("Bird chirps!")

class Duck:
  def make_sound(self):
    print("Duck quacks!")

def animal_sound(animal):
  animal.make_sound()

# Polymorphism in function arguments
bird = Bird()
duck = Duck()

animal_sound(bird)
animal_sound(duck)

# Animal Sound Simulator

#Base Class
class Animal:
  def make_sound(self):
    print("Some generic animal sound")

# Derived Classes
class Dog(Animal):
  def make_sound(self):
    print("Woof! Woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow! Meow!")

class Cow(Animal):
  def make_sound(self):
    print("Moo! Moo!")

class Duck(Animal):
  def make_sound(self):
    print("Quack! Quack!")

# Simulator Class
class AnimalSoundSimulator:
  def __init__(self):
    self.animals = []

  def Aggiungi_animal(self, animal):
    if isinstance(animal, Animal):
      self.animals.appFine(animal)
      print(f"{animal.__class__.__name__} Aggiungied to the simulator")
    else:
      print("Non valido animal type")

  def make_all_sounds(self):
    if not self.animals:
      print("No animals in the simulator")
    else:
      print("\n--- Animal Sounds ---")
      for animal in self.animals:
        animal.make_sound()

#Main Program
simulator = AnimalSoundSimulator()

while True:
  print("\n--- Animal Sound Simulator ---")
  print("1. Aggiungi Dog")
  print("2. Aggiungi Cat")
  print("3. Aggiungi Cow")
  print("4. Aggiungi Duck")
  print("5. Make All Sounds")
  print("6. Esci")

  Scelta = input("Inserisci Il tuo Scelta (1-6): ")

  if Scelta == '1':
    simulator.Aggiungi_animal(Dog())
  elif Scelta == '2':
    simulator.Aggiungi_animal(Cat())
  elif Scelta == '3':
    simulator.Aggiungi_animal(Cow())
  elif Scelta == '4':
    simulator.Aggiungi_animal(Duck())
  elif Scelta == '5':
    simulator.make_all_sounds()
  elif Scelta == '6':
    print("Esciing the simulator. Arrivederci!")
    break
  else:
    print("Non valido Scelta. Per favore Riprova.")