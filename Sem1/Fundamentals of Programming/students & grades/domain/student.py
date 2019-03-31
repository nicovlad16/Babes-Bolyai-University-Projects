class Student(object):

    def __init__(self, ident, name):
        self.__ident = ident
        self.__name = name


    def get_ident(self):
        return self.__ident


    def get_name(self):
        return self.__name


    def set_name(self, value):
        self.__name = value


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__ident == other.__ident
        else:
            return False


    def __str__(self):
        return str(self.get_ident()) + "  " + self.get_name()


    @staticmethod
    def student_to_line(student):
        return str(student.get_ident()) + ";" + student.get_name()


    @staticmethod
    def line_to_student(line):
        elems = line.split(";")
        return Student(int(elems[0]), elems[1])
