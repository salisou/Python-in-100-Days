# -*- coding: utf-8 -*-
"""Day 94 — Testing.

Materiale didattico in italiano.
"""

import unittest

def somma(a, b):
    return a + b

class TestSomma(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(somma(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
