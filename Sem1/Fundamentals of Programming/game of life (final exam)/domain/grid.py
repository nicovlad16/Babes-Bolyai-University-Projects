from domain.valid import ValidException


class Grid():
    def __init__(self):
        self.__grid = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]
        self.__new_generation = [[0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0]]


    def add(self, x, y, elem):
        """
        :param x:
        :param y:
        :param elem:
        adds an element to the grid, on the cell x, y
        elem is the type: 0 or 1
        """
        if self.__grid[x][y] == 1:
            raise ValidException("existing life there")
        else:
            self.__grid[x][y] = elem


    def __str__(self):
        s = "  0 1 2 3 4 5 6 7\n"
        for i in range(0, 8):
            s += str(i) + " "
            for j in range(0, 8):
                if self.__grid[i][j] == 0:
                    s += "."
                elif self.__grid[i][j] == 1:
                    s += "o"
                s += " "
            s += "\n"
        return s


    def get_element(self, x, y):
        """
        :param x:
        :param y:
        :return: the type of element on the i, j cell
        """
        return self.__grid[x][y]


    def get_grid(self):
        return self.__grid


    def evolve(self):
        """
        checks how many neighbors every cell from the grid has
        if it has less that two, it dies, 0
        else it will evolve to 1
        """
        for i in range(0, 8):
            for j in range(0, 8):
                neighbors = self.__count_neightbors(i, j)
                if self.__grid[i][j] == 1:
                    if neighbors < 2:
                        self.__new_generation[i][j] = 0
                    elif neighbors == 2 or neighbors == 3:
                        self.__new_generation[i][j] = 1
                    else:
                        self.__new_generation[i][j] = 0
                elif neighbors == 3:
                    self.__new_generation[i][j] = 1
                else:
                    self.__new_generation[i][j] = 0

        self.__grid = self.__new_generation
        self.__new_generation = [[0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0]]


    def __count_neightbors(self, i, j):
        """
        :param i:  the indecses of a cell
        :param j:
        :return: c -  the number of neighbors from line, column and diagonal
        """
        c = 0
        try:
            if self.__grid[i - 1][j - 1] == 1:
                c += 1
        except IndexError:
            pass
        try:
            if self.__grid[i - 1][j] == 1:
                c += 1
        except IndexError:
            pass
        try:
            if self.__grid[i - 1][j + 1] == 1:
                c += 1
        except IndexError:
            pass
        try:
            if self.__grid[i][j - 1] == 1:
                c += 1
        except IndexError:
            pass
        try:
            if self.__grid[i][j + 1] == 1:
                c += 1
        except IndexError:
            pass
        try:
            if self.__grid[i + 1][j - 1] == 1:
                c += 1
        except IndexError:
            pass
        try:
            if self.__grid[i + 1][j] == 1:
                c += 1
        except IndexError:
            pass
        try:
            if self.__grid[i + 1][j + 1] == 1:
                c += 1
        except IndexError:
            pass
        return c
