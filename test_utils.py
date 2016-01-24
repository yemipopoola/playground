#!/usr/bin/env python

from utils import simple_maths
import unittest

class TestUtils(unittest.TestCase):

    def test_simple_maths(self):
        self.assertEqual(simple_maths(1,1), 2)

if __name__ == '__main__':
    unittest.main()


