from domain.student import Student
from domain.operations import ReverseAddOp, ReverseRemOp, ReverseUpdOp


class StudentController(object):

    def __init__(self, repo, validator, undo_redo_controller):
        self.__repo = repo
        self.__validator = validator
        self.__undo_redo_ctrl = undo_redo_controller


    def __len__(self):
        return len(self.__repo)


    def __str__(self):
        return "\nThe students are:\n" + str(self.__repo)


    def add_student(self, ident, name):
        student = Student(ident, name)
        self.__validator.validate(student)
        self.__repo.add(student)
        self.__undo_redo_ctrl.add_op(ReverseAddOp(self.__repo, student))


    def find_student_by_id(self, ident):
        return self.__repo.find(Student(ident, ""))


    def update_student(self, ident, name):
        existing_student = self.find_student_by_id(ident)
        new_student = Student(ident, name)
        self.__validator.validate(new_student)
        self.__repo.update(new_student)
        self.__undo_redo_ctrl.add_op(ReverseUpdOp(self.__repo, new_student, existing_student))


    def remove_student(self, ident):
        student = self.find_student_by_id(ident)
        self.__validator.validate(student)
        self.__repo.remove(student)
        self.__undo_redo_ctrl.add_op(ReverseRemOp(self.__repo, student))


    def get_all_students(self):
        return self.__repo.get_all()


    def find_student_by_name(self, name):
        elements = []
        for i in self.get_all_students():
            if name.lower() in i.get_name().lower():
                elements.append(i)
        return elements
