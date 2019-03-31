'''
Created on Jan 4, 2018

@author: nvlad
'''
import unittest
from domain.table import Table, ValidationException


class Test(unittest.TestCase):

    def setUp(self):
        self._table = Table()


    def tearDown(self):
        pass


    def testName(self):
        self._table.add(1, 3)
        self._table.add(5, 7)
        self._table.add(7, 7)
        self._table.add(5, 1)
        self.assertFalse(self._table.is_full_table())
        with self.assertRaises(ValidationException):
            self._table.add(1, 3)
        print(self._table)
        self._table.add(2, 0)
        self._table.add(6, 5)
        self._table.add(1, 6)
        self._table.add(0, 0)
        self.assertFalse(self._table.is_full_table())
        self._table.add(4, 4)
        self._table.add(7, 2)
        self._table.add(3, 2)
        self._table.add(3, 6)
        self.assertTrue(self._table.is_full_table())
        print(self._table)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
