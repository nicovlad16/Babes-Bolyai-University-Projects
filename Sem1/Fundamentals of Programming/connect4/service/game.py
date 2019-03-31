'''
Created on Dec 21, 2017

@author: nvlad
'''
from domain.computer import Computer


class Game():

    def __init__(self, table):
        self.__table = table
        self.__computer = Computer(self.__table)
        self.__last_move = [-1][-1]


    def is_draw(self):
        """
        a function that checks if the game ended in a draw; if the table is full and the last move was not a winning one
        :return: True or False
        """
        if self.__table.is_full_table() and not self.is_game_won():
            return True
        else:
            return False


    def is_game_won(self):
        """
        a fucntion that checks if there are four consecutive elements of the same type on line or column or diagonal
        :return: True or False
        """
        return self.__table.is_four_on_line() or self.__table.is_four_on_column() or self.__table.is_four_on_diagonal()


    def player_moves(self, y):
        """
        a function that adds a move to the table
        :param y: the column
        """
        self.__table.add_move(y)


    def computer_moves(self):
        """
        a function that gets the move from the computer, then adds it to the table
        """
        y = self.__computer.get_next_move()
        self.__table.add_move(y)
