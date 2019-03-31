from domain.table import Table


class Repo():
    def __init__(self, filename):
        self.__filename = filename
        self.__elems = []
        self.__read_from_file()


    def __read_from_file(self):
        with open(self.__filename, "r") as f:
            table = Table()
            i = 0
            for line in f.readlines():
                line = line.strip()
                elems = line.split(";")
                z = int(elems[0])
                table.add(i, 0, z)
                a = int(elems[1])
                table.add(i, 1, a)
                b = int(elems[2])
                table.add(i, 2, b)
                c = int(elems[3])
                table.add(i, 3, c)
                d = int(elems[4])
                table.add(i, 4, d)
                e = int(elems[5])
                table.add(i, 5, e)
                i += 1
                if i == 6:
                    break
            self.__elems.append(table)


    def add(self, table):
        self.__elems.clear()
        self.__elems.append(table)
        with open(self.__filename, "w") as f:
            line = ""
            for i in range(0, 6):
                for j in range(0, 6):
                    e = self.__elems[0].get_element(i, j)
                    line += str(e) + ";"
                line += "\n"
            f.write(line)


    def get_table(self):
        return self.__elems[0]
