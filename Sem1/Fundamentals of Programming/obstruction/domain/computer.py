import random


class Computer(object):

    def __init__(self, table):
        self.__table = table


    def get_next_move(self):
        while True:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if self.__table.get_table()[x][y] == -2:
                return [x, y]
