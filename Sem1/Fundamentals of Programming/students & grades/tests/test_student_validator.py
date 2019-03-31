'''
Created on Nov 26, 2017

@author: nvlad
'''
import unittest
from domain.student import Student
from tests.test_student import StudentTest
from validation.validator_student import StudentValidator, StudentValidatorException


class StudentValidatorTest(StudentTest):

    def setUp(self):
        StudentTest.setUp(self)
        self._validator_student = StudentValidator()


    def tearDown(self):
        pass


    def testStudentValidator(self):
        self._validator_student.validate(self._student)
        try:
            self._validator_student.validate(Student(1, ""))
            self.assertEqual(True, False)
        except StudentValidatorException as sve:
            self.assertEqual(str(sve), "Invalid name.\n")
        try:
            self._validator_student.validate(Student(-5, "Andrei"))
            self.assertEqual(True, False)
        except StudentValidatorException as sve:
            self.assertEqual(str(sve), "Invalid id.\n")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
