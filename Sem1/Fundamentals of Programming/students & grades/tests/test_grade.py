'''
Created on Nov 27, 2017

@author: nvlad
'''
import unittest
from domain.grade import Grade


class GradeTest(unittest.TestCase):

    def setUp(self):
        self._grade = Grade(1, 2, 9)


    def tearDown(self):
        pass


    def testGrade(self):
        self.assertEqual(self._grade.get_student_id(), 1)
        self.assertEqual(self._grade.get_discipline_id(), 2)
        self.assertEqual(self._grade.get_grade(), 9)
        gr = Grade(1, 2, 5)
        self.assertEqual(self._grade, gr)
        grad = Grade(1, 3, 9)
        self.assertNotEqual(self._grade, grad)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
