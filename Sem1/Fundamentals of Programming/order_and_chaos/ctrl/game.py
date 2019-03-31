import copy

from domain.computer import Computer
from domain.table import ValidException, Table


class Game:
    def __init__(self, valid, repo):
        self.__repo = repo
        self.__valid = valid
        self.__table = self.__repo.get_table()


    def player_add_move(self, x, y, type):
        self.__valid.validate_move(x, y, type)
        x = int(x)
        y = int(y)
        if type == "x":
            type = 1
        elif type == "o":
            type = -1
        self.__table.add(x, y, type)
        self.__repo.add(self.__table)


    def computer_add_move(self):
        try:
            computer = Computer(self.__table)
            x, y, type = computer.get_next_move()
            self.__table.add(x, y, type)
            self.__repo.add(self.__table)
        except ValidException:
            self.computer_add_move()


    def chaos_won(self):
        return self.__table.is_full_table()


    def order_won(self):
        return self.__table.is_five_on_column() or self.__table.is_five_on_line() or \
               self.__table.is_five_on_diagonal()


    def start_new_game(self):
        self.__table = Table()
        self.__repo.add(self.__table)


    def order_starts(self):
        return self.__table.order_starts()


    def get_table(self):
        return str(self.__table)


    def start_saved_game(self):
        self.__table = self.__repo.get_table()
