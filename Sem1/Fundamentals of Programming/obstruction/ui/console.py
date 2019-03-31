from service.game import Game
from domain.table import ValidationException
import random


class Console(object):

    def __init__(self, table):
        self.__table = table
        self.__game = Game(self.__table)
        self.__first_player = random.randint(0, 1)


    def __read_x(self, txt):
        x = input(txt)
        if not x:
            self.__read_x("Invalid coordinate.\nType again: ")
        return x


    def __read_y(self, txt):
        while True:
            try:
                y = int(input(txt))
                return y
            except:
                pass


    def __player_turn(self):
        try:
            print("You turn,\nmove: ")
            x = self.__read_x("X - coordinate (A-H): ")
            y = self.__read_y("Y - coordinate (0, 7): ")
            self.__game.player_moves(x, y)
            print(self.__table)
            if self.__game.is_game_ended():
                print("You won. Gj.")
        except ValidationException as ve:
            print(ve)
            self.__player_turn()


    def __computer_turn(self):
        print("Computer's turn.")
        self.__game.computer_moves()
        print(self.__table)
        if self.__game.is_game_ended():
            print("You lost.")


    def run(self):
        print(self.__table)
        while True:
            if self.__first_player == 0:
                self.__player_turn()
                if self.__game.is_game_ended():
                    break
                self.__computer_turn()
                if self.__game.is_game_ended():
                    break
            else:
                self.__computer_turn()
                if self.__game.is_game_ended():
                    break
                self.__player_turn()
                if self.__game.is_game_ended():
                    break
        exit(0)
