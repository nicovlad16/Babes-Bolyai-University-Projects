from domain.grade import Grade
from repository.repository import RepositoryException
from domain.student import Student
from domain.discipline import Discipline
from domain.student_plus_grade_dto import StudentGradeDTO
from domain import student
from domain import discipline
from domain.students_who_fails_dto import StudentsWhoFailDTO
from domain.discipline_average_grade_dto import DisciplineGradeDTO
from domain.operations import ReverseAddOp, ComplexReverseRemOp


class GradeController(object):

    def __init__(self, grade_repo, validator, stud_repo, disc_repo, undo_redo_ctrl):
        self.__grade_repo = grade_repo
        self.__validator = validator
        self.__stud_repo = stud_repo
        self.__disc_repo = disc_repo
        self.__undo_redo_ctrl = undo_redo_ctrl


    def __len__(self):
        return len(self.__grade_repo)


    def grade_student(self, student_id, discipline_id, grade_value):
        grade = Grade(student_id, discipline_id, grade_value)
        self.__validator.validate(grade)
        try:
            student = self.__stud_repo.find(Student(student_id, "name"))
        except RepositoryException:
            raise GradeControllerException("Inexisting student.")
        try:
            discipline = self.__disc_repo.find(Discipline(discipline_id, "name"))
        except RepositoryException:
            raise GradeControllerException("Inexisting discipline.")
        try:
            self.__grade_repo.add(grade)
        except RepositoryException:
            raise GradeControllerException("Existing grade.")
        self.__undo_redo_ctrl.add_op(ReverseAddOp(self.__grade_repo, grade))


    def get_grades_by_student(self, student_id):
        elems = []
        for i in self.__grade_repo.get_all():
            if i.get_student_id() == student_id:
                elems.append(i)
        return elems


    def get_grades_by_discipline(self, discipline_id):
        elems = []
        for i in self.__grade_repo.get_all():
            if i.get_discipline_id() == discipline_id:
                elems.append(i)
        return elems


    def delete_grades_by_discipline(self, discipline_id):
        elems = []
        for i in self.get_grades_by_discipline(discipline_id):
            elems.append(i)
            self.__grade_repo.remove(i)
        self.__undo_redo_ctrl.add_op(ComplexReverseRemOp(self.__grade_repo, elems, self.__undo_redo_ctrl))


    def delete_grades_by_student(self, student_id):
        elems = []
        for i in self.get_grades_by_student(student_id):
            elems.append(i)
            self.__grade_repo.remove(i)
        self.__undo_redo_ctrl.add_op(ComplexReverseRemOp(self.__grade_repo, elems, self.__undo_redo_ctrl))


    #     def get_students_by_grade_at_given_discipline(self, discipline_id):
    #         grades = self.get_grades_by_discipline(discipline_id)
    #         grades.sort(key=lambda x: x.get_grade(), reverse=True)
    #         students = []
    #         for grade in grades:
    #             student_id = grade.get_student_id()
    #             student = self.__stud_repo.find(Student(student_id, ""))
    #             students.append(student)
    #         return students
    #
    #     def get_students_by_name_at_given_discipline(self, discipline_id):
    #         grades = self.get_grades_by_discipline(discipline_id)
    #         students = []
    #         for grade in grades:
    #             student_id = grade.get_student_id()
    #             student = self.__stud_repo.find(Student(student_id, ""))
    #             students.append(student)
    #         students.sort(key=lambda x:x.get_name())
    #         return students

    def get_students_by_discipline_sorted_by_grade(self, discipline_id):
        result = []
        grades = self.get_grades_by_discipline(discipline_id)
        for grade in grades:
            student_id = grade.get_student_id()
            student = self.__stud_repo.find(Student(student_id, ""))
            result.append(StudentGradeDTO(student, grade.get_grade()))
        result.sort(key=lambda x: x.get_grade(), reverse=True)
        return result


    def get_students_by_discipline_sorted_by_name(self, discipline_id):
        result = []
        grades = self.get_grades_by_discipline(discipline_id)
        for grade in grades:
            ident = grade.get_student_id()
            student = self.__stud_repo.find(Student(ident, ""))
            result.append(StudentGradeDTO(student, grade.get_grade()))
        result.sort(key=lambda x: x.get_student().get_name())
        return result


    def get_students_who_fail(self):
        result = []
        grades = self.__grade_repo.get_all()
        grades.sort(key=lambda x: x.get_student_id())
        for grade in grades:
            value = grade.get_grade()
            if value < 5:
                student_id = grade.get_student_id()
                student = self.__stud_repo.find(Student(student_id, ""))
                discipline_id = grade.get_discipline_id()
                discipline = self.__disc_repo.find(Discipline(discipline_id, "")).get_name()
                result.append(StudentsWhoFailDTO(student, discipline, value))
        return result


    def get_top_n_students(self, n):
        result = []
        grades = self.__grade_repo.get_all()
        students = {}
        for grade in grades:
            key = grade.get_student_id()
            if key not in students:
                students[key] = [0, 0]
            students[key][0] += grade.get_grade()
            students[key][1] += 1
        for key in students:
            student = self.__stud_repo.find(Student(key, ""))
            grades_average = students[key][0] // students[key][1]
            result.append(StudentGradeDTO(student, grades_average))
        result.sort(key=lambda x: x.get_grade(), reverse=True)
        while len(result) > n:
            result.pop()
        return result


    def get_disciplines_average_grade(self):
        result = []
        grades = self.__grade_repo.get_all()
        disciplines = {}
        for grade in grades:
            key = grade.get_discipline_id()
            if key not in disciplines:
                disciplines[key] = [0, 0]
            disciplines[key][0] += grade.get_grade()
            disciplines[key][1] += 1
        for key in disciplines:
            discipline = self.__disc_repo.find(Discipline(key, ""))
            grades_average = disciplines[key][0] // disciplines[key][1]
            result.append(DisciplineGradeDTO(discipline, grades_average))
        result.sort(key=lambda x: x.get_grade(), reverse=True)
        return result


class GradeControllerException(Exception):
    pass
