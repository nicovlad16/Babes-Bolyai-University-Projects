'''
Created on Nov 27, 2017

@author: nvlad
'''
import unittest
from tests.test_grade import GradeTest
from repository.repository import Repository, RepositoryException
from domain.grade import Grade


class GradeRepositoryTest(GradeTest):

    def setUp(self):
        GradeTest.setUp(self)
        self._repo = Repository()


    def tearDown(self):
        pass


    def testAdd(self):
        self.assertEqual(len(self._repo), 0)
        self._repo.add(self._grade)
        self.assertEqual(len(self._repo), 1)
        try:
            self._repo.add(Grade(1, 2, 5))
            self.assertTrue(False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Existing element.")


    def testUpdate(self):
        self._repo.add(self._grade)
        self._repo.update(Grade(1, 2, 8))
        gr = self._repo.find(self._grade)
        self.assertEqual(gr.get_grade(), 8)
        try:
            self._repo.update(Grade(5, 1, 6))
            self.assertTrue(False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Inexisting element.")


    def testRemove(self):
        self._repo.add(Grade(1, 2, 8))
        self.assertEqual(len(self._repo), 1)
        self._repo.remove(Grade(1, 2, 8))
        self.assertEqual(len(self._repo), 0)
        try:
            self._repo.remove(self._grade)
            self._assertTrue(False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Inexisting element.")


    def testGetAll(self):
        self.assertEqual(self._repo.get_all(), [])
        self._repo.add(self._grade)
        self.assertEqual(self._repo.get_all(), [self._grade])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
