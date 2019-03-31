from domain.valid import ValidException
from repo.repo import Repo


class CtrlException(Exception):
    pass


class Ctrl():
    def __init__(self, repo, valid):
        self.__repo = repo
        self.__valid = valid
        self.__grid = self.__repo.get_current_element()


    def get_grid(self):
        """
        :return: the current grid
        """
        return str(self.__grid)


    def save_file(self, filename):
        """
        :param filename:
        saves the current grid to a file
        """
        self.__repo.add(self.__grid)
        self.__repo.write_to_file(filename)


    def load_file(self, filename):
        """
        :param filename:
        gets the current grid from the file, and that file will be the current repo
        """
        self.__repo = Repo(filename)
        self.__grid = self.__repo.get_current_element()


    def place_pattern(self, pattern, location):
        """
        :param pattern: string
        :param location: string
        adds the given pattern at the given positions
        """
        self.__valid.validate(pattern, location)
        l = location.split(',')
        x = int(l[0])
        y = int(l[1])
        if pattern == "block":
            self.__add_block(x, y)
        if pattern == "tub":
            self.__add_tub(x, y)
        if pattern == "blinker":
            self.__add_blinker(x, y)
        if pattern == "beacon":
            self.__add_beacon(x, y)
        if pattern == "spaceship":
            self.__add_spaceship(x, y)


    def __add_block(self, x, y):
        """
        :param x:
        :param y:
        add block, else raise exception
        """
        try:
            self.__grid.add(x, y, 1)
            self.__grid.add(x, y + 1, 1)
            self.__grid.add(x + 1, y, 1)
            self.__grid.add(x + 1, y + 1, 1)
        except ValidException:
            raise CtrlException("block cannot be added")


    def __add_tub(self, x, y):
        try:
            self.__grid.add(x, y + 1, 1)
            self.__grid.add(x + 1, y, 1)
            self.__grid.add(x + 1, y + 2, 1)
            self.__grid.add(x + 2, y + 1, 1)
        except ValidException:
            raise CtrlException("tub cannot be added")


    def __add_blinker(self, x, y):
        try:
            self.__grid.add(x + 1, y, 1)
            self.__grid.add(x + 1, y + 1, 1)
            self.__grid.add(x + 1, y + 2, 1)
        except ValidException:
            raise CtrlException("blinker cannot be added")


    def __add_beacon(self, x, y):
        try:
            self.__grid.add(x, y, 1)
            self.__grid.add(x, y + 1, 1)
            self.__grid.add(x + 1, y, 1)
            self.__grid.add(x + 1, y + 1, 1)
            self.__grid.add(x + 2, y + 2, 1)
            self.__grid.add(x + 2, y + 3, 1)
            self.__grid.add(x + 3, y + 2, 1)
            self.__grid.add(x + 3, y + 3, 1)

        except ValidException:
            raise CtrlException("beacon cannot be added")


    def __add_spaceship(self, x, y):
        try:
            self.__grid.add(x, y + 1, 1)
            self.__grid.add(x + 1, y + 2, 1)
            self.__grid.add(x + 2, y, 1)
            self.__grid.add(x + 2, y + 1, 1)
            self.__grid.add(x + 2, y + 2, 1)

        except ValidException:
            raise CtrlException("spaceship cannot be added")


    def tick(self, n=None):
        """
        :param n: the number of generations created
        if n is none, it evolves only once, ele n times
        the current grid is added to the repo
        """
        if n:
            try:
                n = int(n)
            except:
                raise CtrlException("invalid number")
            if n <= 0:
                raise CtrlException("invalid number")
            for i in range(n):
                self.__grid.evolve()
            self.__repo.add(self.__grid)
        else:
            self.__grid.evolve()
            self.__repo.add(self.__grid)
