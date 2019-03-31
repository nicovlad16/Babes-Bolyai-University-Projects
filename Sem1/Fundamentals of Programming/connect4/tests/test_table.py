'''
Created on Dec 23, 2017

@author: nvlad
'''
import unittest
from domain.table import Table, ValidationException


class TestTable(unittest.TestCase):

    def setUp(self):
        self._table = Table()


    def tearDown(self):
        pass


    def testTableAddAndValidation(self):
        with self.assertRaises(ValidationException):
            self._table.add_move(8)
        with self.assertRaises(ValidationException):
            self._table.add_move(-5)
        self._table.add_move(5)
        self.assertEqual(self._table.get_last_element(), {"x": 7, "y": 5})
        self._table.add_move(5)
        self.assertEqual(self._table.get_last_element(), {"x": 6, "y": 5})
        self._table.add_move(5)
        self._table.add_move(5)
        self._table.add_move(5)
        self._table.add_move(5)
        self._table.add_move(5)
        self._table.add_move(5)
        self.assertEqual(self._table.is_four_on_line(), False)
        self.assertEqual(self._table.is_four_on_column(), False)
        self.assertEqual(self._table.is_filled_col(5), True)
        self.assertEqual(self._table.is_full_table(), False)
        with self.assertRaises(ValidationException):
            self._table.add_move(5)
        self._table.add_move(2)
        self._table.add_move(4)
        self._table.add_move(2)
        self._table.add_move(3)
        self._table.add_move(3)
        self._table.add_move(4)
        self._table.add_move(4)
        self._table.add_move(4)
        self._table.add_move(3)
        self._table.add_move(4)
        self._table.add_move(2)
        self.assertEqual(self._table.is_four_on_line(), True)
        self._table.add_move(7)
        self._table.add_move(2)
        self.assertEqual(self._table.is_four_on_column(), True)
        self.assertEqual(self._table.is_four_on_diagonal(), False)
        self._table.add_move(1)
        self._table.add_move(1)
        self._table.add_move(1)
        self._table.add_move(1)
        self._table.add_move(1)
        self._table.add_move(0)
        self._table.add_move(0)
        self._table.add_move(0)
        self._table.add_move(0)
        self._table.add_move(0)
        self.assertEqual(self._table.is_four_on_diagonal(), True)
        print(self._table)
        self._table.add_move(0)
        self._table.add_move(0)
        self._table.add_move(0)
        self._table.add_move(1)
        self._table.add_move(1)
        self._table.add_move(1)
        self._table.add_move(2)
        self._table.add_move(2)
        self._table.add_move(2)
        self._table.add_move(2)
        self._table.add_move(3)
        self._table.add_move(3)
        self._table.add_move(3)
        self._table.add_move(3)
        self._table.add_move(3)
        self._table.add_move(4)
        self._table.add_move(4)
        self._table.add_move(4)
        self._table.add_move(6)
        self._table.add_move(6)
        self._table.add_move(6)
        self._table.add_move(6)
        self._table.add_move(6)
        self._table.add_move(6)
        self._table.add_move(6)
        self._table.add_move(6)
        self._table.add_move(7)
        self._table.add_move(7)
        self._table.add_move(7)
        self._table.add_move(7)
        self._table.add_move(7)
        self._table.add_move(7)
        self._table.add_move(7)
        print(self._table)
        self.assertEqual(self._table.is_full_table(), True)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
