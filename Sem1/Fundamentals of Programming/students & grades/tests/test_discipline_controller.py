'''
Created on Nov 26, 2017

@author: nvlad
'''
import unittest
from tests.test_discipline_repository import DisciplineRepositoryTest
from tests.test_discipline_validator import DisciplineValidatorTest
from validation.validate_discipline import DisciplineValidator
from service.discipline_controller import DisciplineController
from service.undo_redo_controller import UndoRedoController


class DisciplineControllerTest(DisciplineRepositoryTest, DisciplineValidatorTest):

    def setUp(self):
        DisciplineRepositoryTest.setUp(self)
        DisciplineValidatorTest.setUp(self)
        self._validator = DisciplineValidator()
        self._undo_redo_controller = UndoRedoController()
        self._ctrl = DisciplineController(self._repo, self._validator, self._undo_redo_controller)


    def tearDown(self):
        pass


    def testAddDiscipline(self):
        self.assertEqual(len(self._ctrl), 0)
        self._ctrl.add_discipline(1, "fp")
        self.assertEqual(len(self._ctrl), 1)
        self._undo_redo_controller.undo()
        self.assertEqual(len(self._ctrl), 0)
        self._undo_redo_controller.redo()
        self.assertEqual(len(self._ctrl), 1)


    def testUpdateDiscipline(self):
        self._ctrl.add_discipline(1, "fp")
        self._ctrl.update_discipline(1, "math")
        disc = self._ctrl.find_discipline_by_id(1)
        self.assertEqual(disc.get_name(), "math")
        self._undo_redo_controller.undo()
        disc = self._ctrl.find_discipline_by_id(1)
        self.assertEqual(disc.get_name(), "fp")
        self._undo_redo_controller.redo()
        disc = self._ctrl.find_discipline_by_id(1)
        self.assertEqual(disc.get_name(), "math")


    def testRemoveDiscipline(self):
        self._ctrl.add_discipline(1, "asc")
        self.assertEqual(len(self._ctrl), 1)
        self._ctrl.remove_discipline(1)
        self.assertEqual(len(self._ctrl), 0)
        self._undo_redo_controller.undo()
        self.assertEqual(len(self._ctrl), 1)
        self._undo_redo_controller.redo()
        self.assertEqual(len(self._ctrl), 0)


    def testGetAllDiscipines(self):
        self.assertEqual(self._ctrl.get_all_disciplines(), [])
        self._ctrl.add_discipline(1, "info")
        self.assertEqual(self._ctrl.get_all_disciplines(), [self._discipline])


    def testFindDisciplineByName(self):
        self._ctrl.add_discipline(1, "info")
        self.assertEqual(self._ctrl.find_discipline_by_name("INfo"), [self._discipline])
        self.assertEqual(self._ctrl.find_discipline_by_name("fp"), [])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
