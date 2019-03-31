class StudentsWhoFailDTO(object):

    def __init__(self, student, discipline, value):
        self.__student = student
        self.__discipline = discipline
        self.__value = value


    def get_student(self):
        return self.__student


    def get_discipline(self):
        return self.__discipline


    def get_value(self):
        return self.__value


    def __str__(self):
        return "Student " + str(self.__student.get_ident()) + ": " \
               + self.__student.get_name() + " is failing at " + self.__discipline \
               + ", having grade " + str(self.__value)
