'''
Created on Nov 25, 2017

@author: nvlad
'''
import unittest
from repository.repository import Repository, RepositoryException
from tests.test_student import StudentTest
from domain.student import Student


class StudentRepositoryTest(StudentTest):

    def setUp(self):
        StudentTest.setUp(self)
        self._repo = Repository()


    def tearDown(self):
        pass


    def testAdd(self):
        self.assertEqual(len(self._repo), 0)
        self._repo.add(self._student)
        self.assertEqual(len(self._repo), 1)
        try:
            self._repo.add(Student(1, "Ana"))
            self.assertEquals(True, False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Existing element.")


    def testUpdate(self):
        self._repo.add(self._student)
        stud = self._repo.find(Student(1, ""))
        self.assertEqual(self._student, stud)
        self._repo.update(Student(1, "Vasile"))
        stud = self._repo.find(Student(1, ""))
        self.assertEqual(stud.get_name(), "Vasile")
        try:
            self._repo.update(Student(5, "Ana"))
            self.assertEquals(True, False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Inexisting element.")


    def testRemove(self):
        self.assertEqual(len(self._repo), 0)
        self._repo.add(self._student)
        self.assertEqual(len(self._repo), 1)
        self._repo.remove(Student(1, ""))
        self.assertEqual(len(self._repo), 0)
        try:
            self._repo.remove(Student(2, ""))
            self.assertEquals(True, False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Inexisting element.")


    def testGetAll(self):
        self._repo.add(self._student)
        self.assertEqual(self._repo.get_all(), [self._student])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
