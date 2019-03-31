import unittest

from domain.table import ValidationException
from domain.valid import Validate


class TestValid(unittest.TestCase):

    def setUp(self):
        self._valid = Validate()


    def test_valid(self):
        self._valid.validate("A1B1C1")
        self._valid.validate("B1B2B3")
        with self.assertRaises(ValidationException):
            self._valid.validate("")
        with self.assertRaises(ValidationException):
            self._valid.validate("dsjhdjsd")
        with self.assertRaises(ValidationException):
            self._valid.validate("35646545d")
        with self.assertRaises(ValidationException):
            self._valid.validate("ddh dd")
        with self.assertRaises(ValidationException):
            self._valid.validate("A1A2D4")
        with self.assertRaises(ValidationException):
            self._valid.validate("A1B3E6")


if __name__ == '__main__':
    unittest.main()
