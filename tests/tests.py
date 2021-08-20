import unittest
import sys, os

sys.path.append('..')

from main import *

class TestFoo(unittest.TestCase):
    def test_foo(self): # Returns m / 10
        self.assertEqual(foo(1000), 10)
        self.assertEqual(foo(2000), 20)

    def test_float(self):
        self.assertIsInstance(foo(1000), float)
        self.assertIsInstance(foo(1234), float)

if __name__ == '__main__':
    unittest.main()
