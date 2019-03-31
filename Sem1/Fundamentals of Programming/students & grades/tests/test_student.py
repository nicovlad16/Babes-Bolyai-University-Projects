'''
Created on Nov 25, 2017

@author: nvlad
'''
import unittest
from domain.student import Student


class StudentTest(unittest.TestCase):

    def setUp(self):
        self._student = Student(1, "Ion")


    def tearDown(self):
        pass


    def testStudent(self):
        self.assertEqual(self._student.get_name(), "Ion")
        self.assertEqual(self._student.get_ident(), 1)
        stud = Student(1, "Gheorghe")
        self.assertEqual(stud, self._student)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
