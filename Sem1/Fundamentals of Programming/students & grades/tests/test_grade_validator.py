'''
Created on Nov 27, 2017

@author: nvlad
'''
import unittest
from tests.test_grade import GradeTest
from domain.grade import Grade
from validation.validate_grade import GradeValidator, GradeValidatorException


class GradeValidatorTest(GradeTest):

    def setUp(self):
        GradeTest.setUp(self)
        self.__valid = GradeValidator()


    def tearDown(self):
        pass


    def testName(self):
        self.__valid.validate(Grade(1, 1, 9))
        try:
            self.__valid.validate(Grade(-1, -1, 15))
            self.assertTrue(False)
        except GradeValidatorException as gve:
            self.assertEqual(str(gve), "Invalid student id.\nInvalid discipline id.\nInvalid grade.\n")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
