class Discipline(object):
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
    def discipline_to_line(discipline):
        return str(discipline.get_ident()) + ";" + discipline.get_name()


    @staticmethod
    def line_to_discipline(line):
        elems = line.split(";")
        return Discipline(int(elems[0]), elems[1])
