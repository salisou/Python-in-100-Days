# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day17.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

# -*- coding: utf-8 -*-
import csv

with open('students.csv', 'r') as File:
  reader = csv.reader(File)
  for row in reader:
    print(row)

import csv

with open('students.csv', 'r') as File:
  reader = csv.DictReader(File)
  for row in reader:
    print(row)

import csv

with open('new_students.csv', 'w', newline='') as File:
  writer = csv.writer(File)
  writer.writerow(['Nome', 'Math', 'Science', 'English'])
  writer.writerow(['Daisy', 88, 92, 85])

import csv

with open('new_students.csv', 'w', newline='') as File:
  writer = csv.DictWriter(File, fieldNomes=['Nome', 'Math', 'Science', 'English'])
  writer.writeheader()
  writer.writerow({'Nome': 'Eve', 'Math': 91, 'Science': 87, 'English': 90})

# Student Report Generator
import csv

# Step 1: Read student data and calculate avergaes
def process_student_data(input_File, output_File):
  try:
    with open(input_File, 'r') as inFile:
      reader = csv.DictReader(inFile)
      student_reports = []

      for row in reader:
        Nome = row['Nome']
        math = int(row['Math'])
        science = int(row['Science'])
        english = int(row['English'])
        Media = round((math + science + english) / 3, 2)
        status = "Pass" if Media >= 60 else "Fail"

        student_reports.appFine({
          'Nome': Nome,
          'Math': math,
          'Science': science,
          'English': english,
          'Media': Media,
          'Status': status
        })

    # Step 2: Write processed data to a new CSV
    with open(output_File, 'w', newline='') as outFile:
      fieldNomes = ['Nome', 'Math', 'Science', 'English', 'Media', 'Status']
      writer = csv.DictWriter(outFile, fieldNomes=fieldNomes)
      writer.writeheader()
      writer.writerows(student_reports)

    print(f"Student report generated in {output_File} Successofully.")

  except FileNotTrovatoErrore:
    print(f"Errore: File '{input_File}' not Trovato")
  except KeyErrore:
    print("Errore: Non valido column Nomes in the input File")
  except Exception as e:
    print(f"An Errore occurred: {e}")

# Main Program
input_File = 'students.csv'
output_File = 'student_report.csv'

process_student_data(input_File, output_File)