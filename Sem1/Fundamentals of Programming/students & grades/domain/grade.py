class Grade(object):

    def __init__(self, student_id, discipline_id, grade):
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__grade = grade
        self.__ident = int(str(abs(student_id)) + str(abs(discipline_id)))


    def get_student_id(self):
        return self.__student_id


    def get_discipline_id(self):
        return self.__discipline_id


    def get_grade(self):
        return self.__grade


    def set_grade(self, value):
        self.__grade = value


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__student_id == other.__student_id and self.__discipline_id == other.__discipline_id
        else:
            return False


    @staticmethod
    def grade_to_line(grade):
        return str(grade.get_student_id()) + ";" + \
               str(grade.get_discipline_id()) + ";" + str(grade.get_grade())


    @staticmethod
    def line_to_grade(line):
        elems = line.split(";")
        return Grade(int(elems[0]), int(elems[1]), int(elems[2]))
