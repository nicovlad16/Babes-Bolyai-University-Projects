class StudentGradeDTO(object):

    def __init__(self, student, grade):
        self.__student = student
        self.__grade = grade


    def get_student(self):
        return self.__student


    def get_grade(self):
        return self.__grade


    def __str__(self):
        return "Student " + str(self.__student.get_ident()) + ": " \
               + self.__student.get_name() + ", having grade " + str(self.__grade)
