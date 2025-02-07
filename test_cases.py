#!/usr/bin/python3

import unittest
from calc import calc  # calc関数をimport

class TestCalc(unittest.TestCase):
    def test_valid_values(self):
        self.assertEqual(calc(1, 1), 1)  
        self.assertEqual(calc(999, 999), 999 * 999)  
        self.assertEqual(calc(1, 500), 500)  
        self.assertEqual(calc(999, 1), 999)  
        self.assertEqual(calc(500, 500), 250000)  

    def test_out_of_range_values(self):
        self.assertEqual(calc(0, 500), -1)
        self.assertEqual(calc(1000, 1), -1)
        self.assertEqual(calc(1, 1000), -1)

    def test_float_values(self):
        self.assertEqual(calc(0.1, 999), -1)
        self.assertEqual(calc(999.9, 500), -1)

    def test_string_values(self):
        self.assertEqual(calc("100", 999), -1)
        self.assertEqual(calc(999, "abc"), -1)

    def test_negative_values(self):
        self.assertEqual(calc(-1, 500), -1)
        self.assertEqual(calc(999, -1), -1)

    def test_invalid_types(self):
        self.assertEqual(calc(None, 1), -1)
        self.assertEqual(calc([], 1), -1)
        self.assertEqual(calc(1, {}), -1)

if __name__ == "__main__":
    unittest.main()

