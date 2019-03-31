'''
Created on Dec 12, 2017

@author: nvlad
'''
import unittest
from tests.test_student import StudentTest
from repository.repository import Repository
from domain.student import Student


class StudentRepositoryTest(StudentTest):

    def setUp(self):
        StudentTest.setUp(self)
        self.__repo = Repository()


    def tearDown(self):
        pass


    def testName(self):
        self.assertEqual(len(self.__repo), 0)
        self.__repo.add(self._student)
        self.assertEqual(len(self.__repo), 1)
        self.__repo[1] = Student(1, "gheorghe")
        self.assertEqual(self.__repo[1], Student(1, ""))
        del (self.__repo[1])
        self.assertEqual(len(self.__repo), 0)
        s1 = Student(1, "ion")
        s2 = Student(5, "ana")
        s3 = Student(3, "ionn")
        self.__repo.add(s1)
        self.__repo.add(s2)
        self.__repo.add(s3)
        self.assertEqual(len(self.__repo), 3)
        lst = self.__repo.sort(lambda x: x.get_name())
        self.assertEqual(lst, [self.__repo[5], self.__repo[1], self.__repo[3]])
        lst = self.__repo.sort(lambda x: x.get_ident())
        self.assertEqual(lst, [self.__repo[1], self.__repo[3], self.__repo[5]])
        students = self.__repo.filter(lambda x: x.get_ident() < 3)
        self.assertEqual(len(students), 1)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
