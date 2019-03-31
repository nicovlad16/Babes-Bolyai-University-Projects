from domain.grid import Grid


class RepoException(Exception):
    pass


class Repo():
    def __init__(self, filename):
        self.__elems = []
        self.__filename = filename
        try:
            self.__read_from_file()
        except FileNotFoundError as e:
            raise RepoException("inexisting file")


    def __read_from_file(self):
        """
        reads a file, and adds a grid to the repository
        """
        with open(self.__filename, "r") as f:
            i = 0
            grid = Grid()
            for line in f.readlines():
                line = line.strip()
                if line:
                    a = line.split(";")
                    grid.add(i, 0, int(a[0]))
                    grid.add(i, 1, int(a[1]))
                    grid.add(i, 2, int(a[2]))
                    grid.add(i, 3, int(a[3]))
                    grid.add(i, 4, int(a[4]))
                    grid.add(i, 5, int(a[5]))
                    grid.add(i, 6, int(a[6]))
                    grid.add(i, 7, int(a[7]))
                i += 1
            self.add(grid)


    def add(self, elem):
        """
        :param elem:
        adds an element to the repository
        """
        self.__elems.append(elem)


    def write_to_file(self, filename):
        """
        :param filename:
        creates a new file with given name, having as stored information the last grid added in repo
        """
        grid = self.__elems[-1]
        line = ""
        for i in range(0, 8):
            for j in range(0, 8):
                line += str(grid.get_element(i, j)) + ";"
            line += "\n"
        with open(filename, "w")as f:
            f.write(line)


    def get_current_element(self):
        """
        :return: the last element from repo
        """
        return self.__elems[-1]
