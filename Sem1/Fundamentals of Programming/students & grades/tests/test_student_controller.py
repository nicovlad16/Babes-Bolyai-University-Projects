'''
Created on Nov 26, 2017

@author: nvlad
'''
import unittest
from tests.test_student_repository import StudentRepositoryTest
from tests.test_student_validator import StudentValidatorTest
from validation.validator_student import StudentValidator
from domain.student import Student
from service.undo_redo_controller import UndoRedoController, UndoRedoException
from service.student_controller import StudentController


class StudentControllerTest(StudentRepositoryTest, StudentValidatorTest):

    def setUp(self):
        StudentRepositoryTest.setUp(self)
        StudentValidatorTest.setUp(self)
        self._validator = StudentValidator()
        self._undo_redo_ctrl = UndoRedoController()
        self._ctrl = StudentController(self._repo, self._validator, self._undo_redo_ctrl)


    def tearDown(self):
        pass


    def testAddStudent(self):
        self.assertEqual(len(self._ctrl), 0)
        self._ctrl.add_student(1, "Ion")
        self.assertEqual(len(self._ctrl), 1)
        self._undo_redo_ctrl.undo()
        self.assertEqual(len(self._ctrl), 0)
        with self.assertRaises(UndoRedoException):
            self._undo_redo_ctrl.undo()
        self._undo_redo_ctrl.redo()
        self.assertEqual(len(self._ctrl), 1)
        with self.assertRaises(UndoRedoException):
            self._undo_redo_ctrl.redo()


    def testUpdateStudent(self):
        self._ctrl.add_student(1, "Ion")
        self._ctrl.update_student(1, "Vasile")
        student = self._ctrl.find_student_by_id(1)
        self.assertEqual(student.get_name(), "Vasile")
        self._undo_redo_ctrl.undo()
        student = self._ctrl.find_student_by_id(1)
        self.assertEqual(student.get_name(), "Ion")
        self._undo_redo_ctrl.redo()
        student = self._ctrl.find_student_by_id(1)
        self.assertEqual(student.get_name(), "Vasile")


    def testRemoveStudent(self):
        self._ctrl.add_student(1, "Ion")
        self.assertEqual(len(self._ctrl), 1)
        self._ctrl.remove_student(1)
        self.assertEqual(len(self._ctrl), 0)
        self._undo_redo_ctrl.undo()
        self.assertEqual(len(self._ctrl), 1)
        self._undo_redo_ctrl.redo()
        self.assertEqual(len(self._ctrl), 0)


    def testGetAllStudents(self):
        self.assertEqual(self._ctrl.get_all_students(), [])
        self._ctrl.add_student(1, "Ion")
        student = self._ctrl.find_student_by_id(1)
        self.assertEqual(self._ctrl.get_all_students(), [student])


    def testFindStudentByName(self):
        self._ctrl.add_student(1, "Ion")
        self._ctrl.add_student(2, "Ionel")
        students = [Student(1, "Ion"), Student(2, "Ionel")]
        self.assertEqual(self._ctrl.find_student_by_name("ion"), students)
        self.assertEqual(self._ctrl.find_student_by_name("Alex"), [])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
