'''
Created on Nov 26, 2017

@author: nvlad
'''
import unittest
from domain.discipline import Discipline
from repository.repository import Repository, RepositoryException
from tests.test_discipline import DisciplineTest


class DisciplineRepositoryTest(DisciplineTest):

    def setUp(self):
        DisciplineTest.setUp(self)
        self._repo = Repository()


    def tearDown(self):
        pass


    def testAdd(self):
        self.assertEqual(len(self._repo), 0)
        self._repo.add(self._discipline)
        self.assertEqual(len(self._repo), 1)
        try:
            self._repo.add(self._discipline)
            self.assertEqual(True, False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Existing element.")


    def testUpdate(self):
        self._repo.add(self._discipline)
        self._repo.update(Discipline(1, "fp"))
        disc = self._repo.find(Discipline(1, ""))
        self.assertEqual(disc.get_name(), "fp")
        try:
            self._repo.update(Discipline(5, "math"))
            self.assertEqual(True, False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Inexisting element.")


    def testRemove(self):
        self._repo.add(self._discipline)
        self.assertEqual(len(self._repo), 1)
        self._repo.remove(self._discipline)
        self.assertEqual(len(self._repo), 0)
        try:
            self._repo.remove(self._discipline)
            self._assertEqual(True, False)
        except RepositoryException as re:
            self.assertEqual(str(re), "Inexisting element.")


    def testGetAll(self):
        self.assertEqual(self._repo.get_all(), [])
        self._repo.add(self._discipline)
        self.assertEqual(self._repo.get_all(), [self._discipline])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
