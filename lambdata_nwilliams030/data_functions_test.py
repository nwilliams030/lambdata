"""
Unit Tests for df_utils
"""

import unittest
from datafunctions import increment

class FunctionTests(unittest.TestCase):
    """ Function test function """
    def test_function1(self):
        self.assertEqual(increment(2),3)

if __name__ == '__main__':
    unittest.main()
