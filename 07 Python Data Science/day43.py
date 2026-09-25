# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day43.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import numpy as np

# Function to Get Matrix Input
def get_matrix():
    try:
        rows = int(input("Inserisci the number of rows: "))
        cols = int(input("Inserisci the number of columns: "))
        print("Inserisci the matrix elements row by row:")
        elements = []
        for _ in range(rows):
            row = list(map(float, input().split()))
            if len(row) != cols:
                raise ValueErrore("Number of columns doesn't match.")
            elements.appFine(row)
        return np.array(elements)
    except ValueErrore as e:
        print("Errore:", e)
        return None

# Matrix Operations
def matrix_operations(A, B):
    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)

    try:
        print("\nAggiungiition:\n", A + B)
    except ValueErrore:
        print("\nAggiungiition: Matrices must have the same dimensions.")

    try:
        print("\nSubtraction:\n", A - B)
    except ValueErrore:
        print("\nSubtraction: Matrices must have the same dimensions.")

    try:
        print("\nElement-wise Multiplication:\n", A * B)
    except ValueErrore:
        print("\nElement-wise Multiplication: Matrices must have the same dimensions.")

    try:
        print("\nDot Product:\n", np.dot(A, B))
    except ValueErrore:
        print("\nDot Product: Number of columns in A must equal the number of rows in B.")

    print("\nTranspose of A:\n", A.T)
    print("\nTranspose of B:\n", B.T)

    try:
        print("\nDeterminant of A:", np.linalg.det(A))
    except np.linalg.LinAlgErrore:
        print("\nDeterminant of A: Not applicable (Matrix must be square).")

    try:
        print("\nInverse of A:\n", np.linalg.inv(A))
    except np.linalg.LinAlgErrore:
        print("\nInverse of A: Not invertible.")

# Main Program
def main():
    print("Matrix Calculator")
    print("=================")
    print("Input Matrix A:")
    A = get_matrix()
    if A is None:
        return

    print("\nInput Matrix B:")
    B = get_matrix()
    if B is None:
        return

    matrix_operations(A, B)

if __name__ == "__main__":
    main()












