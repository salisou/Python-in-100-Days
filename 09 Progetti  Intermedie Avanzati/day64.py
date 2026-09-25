# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day64.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import os
from PyPDF2 import PdfMerger

def get_pdf_order():
    pdf_list = input("Inserisci PDF file names in the desired order (comma-separated): ").split(",")
    return [pdf.strip() for pdf in pdf_list]

def validate_files(pdf_list):
    for pdf in pdf_list:
        if not os.path.exists(pdf):
            print(f"Errore: {pdf} does not exist.")
            return False
    return True

def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.appFine(pdf)
    merger.write(output_file)
    merger.close()
    print(f"Merged PDF Salvad as {output_file}")

def main():
    print("Benvenuto to the PDF Merger Tool!")
    pdf_list = get_pdf_order()
    if validate_files(pdf_list):
        output_file = input("Inserisci the output file name (e.g., merged.pdf): ")
        merge_pdfs(pdf_list, output_file)

if __name__ == "__main__":
    main()


# Example Usage
# pdf_order = get_pdf_order()
# merge_pdfs(pdf_order, "merged_output.pdf")


# Example Usage
# merge_pdfs(["p1.pdf", "p2.pdf"], "merged.pdf")
# print("PDFs merged Successofully!")