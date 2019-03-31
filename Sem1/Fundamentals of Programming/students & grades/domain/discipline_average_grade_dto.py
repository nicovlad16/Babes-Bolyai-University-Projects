class DisciplineGradeDTO(object):

    def __init__(self, discipline, grade):
        self.__discipline = discipline
        self.__grade = grade


    def get_discipline(self):
        return self.__discipline


    def get_grade(self):
        return self.__grade


    def __str__(self):
        return "Discipline " + str(self.__discipline.get_ident()) + ": " \
               + self.__discipline.get_name() + ", having average grade " + \
               str(self.__grade)
