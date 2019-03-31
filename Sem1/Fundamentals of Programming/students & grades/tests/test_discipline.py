'''
Created on Nov 26, 2017

@author: nvlad
'''
import unittest
from domain.discipline import Discipline


class DisciplineTest(unittest.TestCase):

    def setUp(self):
        self._discipline = Discipline(1, "info")


    def tearDown(self):
        pass


    def testDiscipline(self):
        self.assertEqual(self._discipline.get_ident(), 1)
        self.assertEqual(self._discipline.get_name(), "info")
        disc = Discipline(1, "english")
        self.assertEqual(self._discipline, disc)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
