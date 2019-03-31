from repository.repository import RepositoryException
from validation.validator_student import StudentValidatorException
from validation.validate_discipline import DisciplineValidatorException
from validation.validate_grade import GradeValidatorException
from service.grade_controller import GradeControllerException
from utils.initialize_repositories import InitializeRepositories
from domain import student
from service.undo_redo_controller import UndoRedoException


class Console(object):

    def __init__(self, stud_ctrl, disc_ctrl, grade_ctrl, undo_redo_ctrl):
        self.__stud_ctrl = stud_ctrl
        self.__disc_ctrl = disc_ctrl
        self.__grade_ctrl = grade_ctrl
        self.__undo_redo_ctrl = undo_redo_ctrl
        self.__undo_list = []
        self.__redo_list = []
        self.__commands = {
            1: [self.__ui_add_student, "1.Add student."],
            2: [self.__ui_update_student, "2.Update student."],
            3: [self.__ui_remove_student, "3.Remove student."],
            4: [self.__ui_list_all_students, "4.List all students."],
            5: [self.__ui_list_student_by_id, "5.Search student by id."],
            6: [self.__ui_list_students_by_name, "6.Search students by name."],
            7: [self.__ui_add_discipline, "7.Add discipline."],
            8: [self.__ui_update_discipline, "8.Update discipline."],
            9: [self.__ui_remove_discipline, "9.Remove discipline."],
            10: [self.__ui_list_all_disciplines, "10.List all disciplines."],
            11: [self.__ui_list_discipline_by_id, "11.Search discipline by id."],
            12: [self.__ui_list_disciplines_by_name, "12.Search disciplines by name."],
            13: [self.__ui_grade_student, "13.Grade student."],
            14: [self.__ui_list_students_enrolled_at_given_discipline_by_grade, \
                 "14.List students (enrolled at a discipline) by descending average grade."],
            15: [self.__ui_list_students_enrolled_at_given_discipline_by_name, \
                 "15.List students (enrolled at a discipline) by alphabet. "],
            16: [self.__ui_list_students_who_fail, "16.List students who fail."],
            17: [self.__ui_list_top_n_students, "17.List top 'n' students."],
            18: [self.__ui_list_disciplines_average_grades, "18.List disciplines average grades."],
            19: [self.__ui_undo, "19.Undo."],
            20: [self.__ui_redo, "20.Redo.\n"]
        }


    def initialize_repositories(self):
        repo = InitializeRepositories()
        for student in repo.initialize_student_repo():
            ident = student.get_ident()
            name = student.get_name()
            self.__stud_ctrl.add_student(ident, name)
        for discipline in repo.initialize_disciplines_repo():
            ident = discipline.get_ident()
            name = discipline.get_name()
            self.__disc_ctrl.add_discipline(ident, name)
        for grade in repo.initiallize_grade_repo():
            stud_id = grade.get_student_id()
            disc_id = grade.get_discipline_id()
            grade_value = grade.get_grade()
            self.__grade_ctrl.grade_student(stud_id, disc_id, grade_value)


    def __print_list(self, entities):
        for entity in entities:
            print(entity)


    def __read_int(self, text):
        while True:
            try:
                return int(input(text))
            except:
                print("Invalid number.")


    def __read_command(self, text):
        while True:
            try:
                return int(input(text))
            except:
                print("Invalid command.")


    def __show_menu(self):
        print("\n0.Exit")
        for command in self.__commands.values():
            print(command[1])


    def run(self):
        while True:
            self.__show_menu()
            try:
                cmd = self.__read_command("Input command:")
                if cmd == 0:
                    return
                elif cmd in self.__commands:
                    self.__commands[cmd][0]()
                else:
                    print("Please write a valid command.")
            except RepositoryException as re:
                print(re)
            except StudentValidatorException as sve:
                print(sve)
            except DisciplineValidatorException as dve:
                print(dve)
            except GradeValidatorException as gve:
                print(gve)
            except GradeControllerException as gce:
                print(gce)
            except UndoRedoException as ure:
                print(ure)


    def __ui_list_all_students(self):
        if len(self.__stud_ctrl.get_all_students()):
            print(self.__stud_ctrl)
        else:
            print("404: No students.")


    def __ui_list_student_by_id(self):
        student_id = self.__read_int("Insert student id: ")
        print(self.__stud_ctrl.find_student_by_id(student_id))


    def __ui_list_students_by_name(self):
        student_name = input("Insert student name: ")
        students = self.__stud_ctrl.find_student_by_name(student_name)
        if students:
            self.__print_list(students)
        else:
            print("404. Students not found.")


    def __ui_add_student(self):
        student_id = self.__read_int("Insert student id: ")
        student_name = input("Insert student name: ")
        self.__stud_ctrl.add_student(student_id, student_name)
        print("Succesfully added.")
        self.__undo_list.append("__ui_add_student")


    def __ui_update_student(self):
        student_id = self.__read_int("Insert student id: ")
        student_name = input("Insert new student name: ")
        self.__stud_ctrl.update_student(student_id, student_name)
        print("Succesfully updated.")
        self.__undo_list.append("__ui_update_student")


    def __ui_remove_student(self):
        student_id = self.__read_int("Insert student id: ")
        self.__stud_ctrl.remove_student(student_id)
        self.__grade_ctrl.delete_grades_by_student(student_id)
        print("Succesfully removed.")
        self.__undo_list.append("__ui_remove_student")


    def __ui_list_all_disciplines(self):
        if len(self.__disc_ctrl.get_all_disciplines()):
            print(self.__disc_ctrl)
        else:
            print("404: No disciplines.")


    def __ui_list_discipline_by_id(self):
        discipline_id = self.__read_int("Insert discipline id: ")
        print(self.__disc_ctrl.find_discipline_by_id(discipline_id))


    def __ui_list_disciplines_by_name(self):
        discipline_name = input("Insert discipline name: ")
        disciplines = self.__disc_ctrl.find_discipline_by_name(discipline_name)
        if disciplines:
            self.__print_list(disciplines)
        else:
            print("404: Disciplines not found.")


    def __ui_add_discipline(self):
        discipline_id = self.__read_int("Insert discipline id: ")
        discipline_name = input("Insert discipline name: ")
        self.__disc_ctrl.add_discipline(discipline_id, discipline_name)
        print("Succesfully added.")
        self.__undo_list.append("__ui_add_discipline")


    def __ui_update_discipline(self):
        discipline_id = self.__read_int("Insert discipline id: ")
        discipline_name = input("Insert new discipline name: ")
        self.__disc_ctrl.update_discipline(discipline_id, discipline_name)
        print("Succesfully updated.")
        self.__undo_list.append("__ui_update_discipline")


    def __ui_remove_discipline(self):
        discipline_id = self.__read_int("Insert discipline id: ")
        self.__disc_ctrl.remove_discipline(discipline_id)
        self.__grade_ctrl.delete_grades_by_discipline(discipline_id)
        print("Succesfully removed.")
        self.__undo_list.append("__ui_remove_discipline")


    def __ui_grade_student(self):
        student_id = self.__read_int("Insert student id: ")
        discipline_id = self.__read_int("Insert discipline id: ")
        grade_value = self.__read_int("Insert grade: ")
        self.__grade_ctrl.grade_student(student_id, discipline_id, grade_value)
        print("Succesfully added.")
        self.__undo_list.append("__ui_grade_student")


    def __ui_list_students_enrolled_at_given_discipline_by_grade(self):
        discipline_id = self.__read_int("Insert discipline id: ")
        students = self.__grade_ctrl.get_students_by_discipline_sorted_by_grade(discipline_id)
        if students:
            print("The students are:")
            self.__print_list(students)
        else:
            print("404: No students found.")


    def __ui_list_students_enrolled_at_given_discipline_by_name(self):
        discipline_id = self.__read_int("Insert discipline id: ")
        students = self.__grade_ctrl.get_students_by_discipline_sorted_by_name(discipline_id)
        if students:
            print("The students are:")
            self.__print_list(students)
        else:
            print("404: No students found.")


    def __ui_list_students_who_fail(self):
        students = self.__grade_ctrl.get_students_who_fail()
        if students:
            print("The students are:")
            self.__print_list(students)
        else:
            print("404: No students found.")


    def __ui_list_top_n_students(self):
        number_of_students = self.__read_int("Insert number of students: ")
        students = self.__grade_ctrl.get_top_n_students(number_of_students)
        if students:
            print("The students are:")
            self.__print_list(students)
        else:
            print("404: No students found.")


    def __ui_list_disciplines_average_grades(self):
        disciplines = self.__grade_ctrl.get_disciplines_average_grade()
        if disciplines:
            print("The disciplines are:")
            self.__print_list(disciplines)
        else:
            print("404: No disciplines or grades found.")


    def __ui_undo(self):
        #         if self.__undo_list:
        #             last = self.__undo_list[-1]
        #             if last == "__ui_remove_discipline" or "__ui_remove_student":
        #                 self.__undo_redo_ctrl.undo()
        #                 self.__redo_list.append(last)
        #                 self.__undo_list.pop()
        #             last = self.__undo_list[-1]
        #             self.__undo_redo_ctrl.undo()
        #             self.__redo_list.append(last)
        #             self.__undo_list.pop()
        #         self.__print_list(self.__undo_list)
        self.__undo_redo_ctrl.undo()
        print("Undo successfully.")


    def __ui_redo(self):
        #         if self.__redo_list:
        #             last = self.__redo_list[-1]
        #             if last == "__ui_remove_discipline" or "__ui_remove_student":
        #                 self.__undo_redo_ctrl.redo()
        #                 self.__undo_list.append(last)
        #                 self.__redo_list.pop()
        #             last = self.__undo_list[-1]
        #             self.__undo_redo_ctrl.redo()
        #             self.__undo_list.append(last)
        #             self.__redo_list.pop()
        #         print(self.__redo_list)
        self.__undo_redo_ctrl.redo()
        print("Redo succesfully.")
