from domain.computer import Computer
from domain.table import ValidationException
from validation.validate import Validator


class Game(object):

    def __init__(self, table):
        self.__table = table
        self.__computer = Computer(self.__table)


    def is_game_ended(self):
        return self.__table.is_full_table()


    def player_moves(self, x, y):
        moves = ["a", "b", "c", "d", "e", "f", "g", "h"]
        Validator.validate(x, y)
        x = moves.index(x.lower())
        self.__table.add(x, y)


    def computer_moves(self):
        xy = self.__computer.get_next_move()
        self.__table.add(xy[0], xy[1])
