import unittest
from domain.table import Table, ValidationException


class TestTable(unittest.TestCase):

    def setUp(self):
        self._table = Table(True)


    def test_something(self):
        self._table.add(0, 1, 0, 2, 0, 3)
        self.assertEqual(self._table.get_ship1(), [[0, 1], [0, 2], [0, 3]])
        self._table.add(4, 2, 4, 3, 4, 4)
        self.assertEqual(self._table.get_ship2(), [[4, 2], [4, 3], [4, 4]])
        print(self._table)
        self._table.add(0, 1, 1, 1, 2, 1)
        self.assertEqual(self._table.get_ship2(), [[0, 1], [1, 1], [2, 1]])
        self.assertEqual(self._table.get_ship1(), [[4, 2], [4, 3], [4, 4]])
        print(self._table)
        with self.assertRaises(ValidationException):
            self._table.add(2, 1, 2, 2, 2, 3)
        print(self._table)


if __name__ == '__main__':
    unittest.main()
