'''
Created on Nov 27, 2017

@author: nvlad
'''
import unittest
from tests.test_grade_repository import GradeRepositoryTest
from tests.test_grade_validator import GradeValidatorTest
from validation.validate_grade import GradeValidator
from service.grade_controller import GradeController, GradeControllerException
from repository.repository import Repository
from domain.discipline import Discipline
from domain.student import Student
from domain.student_plus_grade_dto import StudentGradeDTO
from domain.students_who_fails_dto import StudentsWhoFailDTO
from domain.discipline_average_grade_dto import DisciplineGradeDTO
from service.undo_redo_controller import UndoRedoController


class GradeControllerTest(GradeRepositoryTest, GradeValidatorTest):

    def setUp(self):
        GradeValidatorTest.setUp(self)
        GradeRepositoryTest.setUp(self)
        self._validator = GradeValidator()
        self._stud_repo = Repository()
        self._disc_repo = Repository()
        self._grade_repo = Repository()
        self._stud_repo.add(Student(1, "ion"))
        self._disc_repo.add(Discipline(1, "fp"))
        self._undo_redo_ctrl = UndoRedoController()
        self._grade_ctrl = GradeController(self._grade_repo, self._validator, \
                                           self._stud_repo, self._disc_repo, self._undo_redo_ctrl)


    def tearDown(self):
        pass


    def testGradeStudent(self):
        self.assertEqual(len(self._grade_ctrl), 0)
        self._grade_ctrl.grade_student(1, 1, 8)
        self.assertEqual(len(self._grade_ctrl), 1)
        try:
            self._grade_ctrl.grade_student(8, 1, 5)
            self.assertTrue(False)
        except GradeControllerException as gce:
            self.assertEqual(str(gce), "Inexisting student.")
        try:
            self._grade_ctrl.grade_student(1, 5, 9)
            self.assertTrue(False)
        except GradeControllerException as gce:
            self.assertEqual(str(gce), "Inexisting discipline.")
        self._undo_redo_ctrl.undo()
        self.assertEqual(len(self._grade_ctrl), 0)
        self._undo_redo_ctrl.redo()
        self.assertEqual(len(self._grade_ctrl), 1)


    def testDeleteGradesIfDisciplineIsRemoved(self):
        discipline = Discipline(1, "fp")
        self._grade_ctrl.grade_student(1, 1, 8)
        self.assertEqual(len(self._grade_ctrl), 1)
        self._disc_repo.remove(discipline)
        self._grade_ctrl.delete_grades_by_discipline(discipline.get_ident())
        self.assertEqual(len(self._grade_ctrl), 0)
        self._undo_redo_ctrl.undo()


    #         self.assertEqual(len(self._grade_ctrl), 1)
    #         self._undo_redo_ctrl.redo()
    #         self.assertEqual(len(self._grade_ctrl), 0)

    def testDeleteGradesIfStudentIsRemoved(self):
        self._grade_ctrl.grade_student(1, 1, 8)
        self.assertEqual(len(self._grade_ctrl), 1)
        self._stud_repo.remove(Student(1, ""))
        self._grade_ctrl.delete_grades_by_student(1)
        self.assertEqual(len(self._grade_ctrl), 0)
        self._undo_redo_ctrl.undo()


    #         self.assertEqual(len(self._grade_ctrl), 1)
    #         self._undo_redo_ctrl.redo()
    #         self.assertEqual(len(self._grade_ctrl), 0)

    #     def testGetStudentsByGradeAtGivenDiscipline(self):
    #         self._stud_repo.add(Student(2, "Andrei"))
    #         self._grade_ctrl.grade_student(1, 1, 7)
    #         self._grade_ctrl.grade_student(2, 1, 9)
    #         discipline_id = 1
    #         elems = self._grade_ctrl.get_students_by_grade_at_given_discipline(discipline_id)
    #         self.assertEqual(elems[1], Student(1, ""))
    #         self.assertEqual(elems[0], Student(2, ""))
    #
    #     def testGetStudentsByNameAtGivenDiscipline(self):
    #         self._stud_repo.add(Student(2, "Andrei"))
    #         self._grade_ctrl.grade_student(1, 1, 8)
    #         self._grade_ctrl.grade_student(2, 1, 2)
    #         discipline_id = 1
    #         elems = self._grade_ctrl.get_students_by_name_at_given_discipline(discipline_id)
    #         self.assertEqual(elems[0], Student(2, ""))
    #         self.assertEqual(elems[1], Student(1, ""))

    def testStudentsDisciplinesSortedByGrade(self):
        self._stud_repo.add(Student(2, "Vasile"))
        self._grade_ctrl.grade_student(1, 1, 8)
        self._grade_ctrl.grade_student(2, 1, 6)
        elems = self._grade_ctrl.get_students_by_discipline_sorted_by_grade(1)
        ion = StudentGradeDTO(Student(1, "ion"), 8)
        vasile = StudentGradeDTO(Student(2, "Vasile"), 6)
        self.assertEqual(str(elems[0]), str(ion))
        self.assertEqual(str(elems[1]), str(vasile))
        self._disc_repo.add(Discipline(2, "math"))
        elems = self._grade_ctrl.get_students_by_discipline_sorted_by_grade(2)
        self.assertEqual(elems, [])


    def testStudentDisciplinesByName(self):
        self._stud_repo.add(Student(2, "andrei"))
        self._grade_ctrl.grade_student(1, 1, 6)
        self._grade_ctrl.grade_student(2, 1, 8)
        self._disc_repo.add(Discipline(2, "info"))
        elems = self._grade_ctrl.get_students_by_discipline_sorted_by_name(1)
        ion = StudentGradeDTO(Student(1, "ion"), 6)
        andrei = StudentGradeDTO(Student(2, "andrei"), 8)
        self.assertEqual(str(elems[0]), str(andrei))
        self.assertEqual(str(elems[1]), str(ion))
        elems = self._grade_ctrl.get_students_by_discipline_sorted_by_name(2)
        self.assertEqual(elems, [])


    def testStudentsWhoFail(self):
        self._stud_repo.add(Student(2, 'andrei'))
        self._grade_ctrl.grade_student(1, 1, 7)
        self._grade_ctrl.grade_student(2, 1, 4)
        elems = self._grade_ctrl.get_students_who_fail()
        andrei = StudentsWhoFailDTO(Student(2, 'andrei'), "fp", 4)
        self.assertEqual(len(elems), 1)
        self.assertEqual(str(elems[0]), str(andrei))


    def testTopNStudents(self):
        stud1 = Student(2, "andrei")
        stud2 = Student(3, "vasile")
        self._stud_repo.add(stud1)
        self._stud_repo.add(stud2)
        self._disc_repo.add(Discipline(2, "math"))
        self._grade_ctrl.grade_student(1, 1, 4)
        self._grade_ctrl.grade_student(2, 1, 9)
        self._grade_ctrl.grade_student(2, 2, 9)
        elems = self._grade_ctrl.get_top_n_students(1)
        andrei = StudentGradeDTO(stud1, 9)
        self.assertEqual(len(elems), 1)
        self.assertEqual(str(elems[0]), str(andrei))


    def testDisciplinesAverageGrade(self):
        stud1 = Student(2, "andrei")
        stud2 = Student(3, "vasile")
        self._stud_repo.add(stud1)
        self._stud_repo.add(stud2)
        self._disc_repo.add(Discipline(2, "math"))
        self._grade_ctrl.grade_student(1, 1, 6)
        self._grade_ctrl.grade_student(2, 1, 7)
        self._grade_ctrl.grade_student(3, 1, 8)
        elems = self._grade_ctrl.get_disciplines_average_grade()
        fp = DisciplineGradeDTO(Discipline(1, "fp"), 7)
        self.assertEqual(len(elems), 1)
        self.assertEqual(str(elems[0]), str(fp))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
