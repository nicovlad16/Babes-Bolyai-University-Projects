'''
Created on Dec 27, 2017

@author: nvlad
'''
import unittest
from domain.table import Table
from domain.computer import Computer


class Test(unittest.TestCase):

    def setUp(self):
        self._table = Table()
        self._computer = Computer(self._table)


    def tearDown(self):
        pass


    def testName(self):
        self._table.add_move(self._computer.get_next_move())
        self._table.add_move(4)
        self._table.add_move(self._computer.get_next_move())
        self._table.add_move(4)
        self._table.add_move(self._computer.get_next_move())
        self._table.add_move(4)
        self._table.add_move(self._computer.get_next_move())
        self._table.add_move(4)

        print(self._table)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
