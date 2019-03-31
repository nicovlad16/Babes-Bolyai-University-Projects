'''
Created on Nov 26, 2017

@author: nvlad
'''
import unittest
from tests.test_discipline import DisciplineTest
from validation.validate_discipline import DisciplineValidator, DisciplineValidatorException
from domain.discipline import Discipline


class DisciplineValidatorTest(DisciplineTest):

    def setUp(self):
        DisciplineTest.setUp(self)
        self._validator = DisciplineValidator()


    def tearDown(self):
        pass


    def testDisciplineValidator(self):
        self._validator.validate(Discipline(1, "info"))
        try:
            self._validator.validate(Discipline(-5, "math"))
            self.assertEqual(True, False)
        except DisciplineValidatorException as dve:
            self.assertEqual(str(dve), "Invalid id.\n")
        try:
            self._validator.validate(Discipline(5, ""))
            self.assertEqual(True, False)
        except DisciplineValidatorException as dve:
            self.assertEqual(str(dve), "Invalid name.\n")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
