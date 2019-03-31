import random


class Computer():

    def __init__(self, table):
        self.__table = table


    def get_ship(self):
        """a function that return the coordinates of a ship, chosed randomly"""
        k = random.randint(0, 1)
        i = random.randint(0, 5)
        j = random.randint(0, 5)
        if j >= 3 and k == 0:
            return i, j - 2, i, j - 1, i, j
        elif j >= 3 and k == 1:
            return j - 2, i, j - 1, i, j, i
        elif k == 0:
            return i, j, i, j + 1, i, j + 2
        else:
            return j, i, j + 1, i, j + 2, i


    def get_next_attack(self):
        """a function that returns a cell of the map, randomly"""
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        return x, y
