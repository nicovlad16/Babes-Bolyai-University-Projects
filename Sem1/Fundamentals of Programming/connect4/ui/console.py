'''
Created on Dec 21, 2017

@author: nvlad
'''
import random

from domain.table import ValidationException


class Console():

    def __init__(self, table, game):
        self.__table = table
        self.__game = game


    def __read_int(self, txt):
        """
        a function that reads a number
        :param txt: what is printed on screen
        :return: the number that has been read if it is correct,
                 else it prints a message and does the reading again
        """
        while True:
            try:
                y = int(input(txt))
                return y
            except:
                print("Invalid position. It should be an integer between 0 and 7. ")


    def __players_turn(self):
        """
        a function that prints the table, then reads the next move of the player,
        checks if the game was won by the player or if it was draw
        :return: if ValidationException was raised, it repeats the function until
                 the human will input a valid position for the game
        """
        try:
            print(self.__table)
            y = self.__read_int("Your turn,\nmove: ")
            self.__game.player_moves(y)
            if self.__game.is_game_won():
                print(self.__table)
                print("Well done, human.")
            elif self.__game.is_draw():
                print(self.__table)
                print("Draw.")
        except ValidationException as ve:
            print(ve)
            self.__players_turn()


    def __computers_turn(self):
        """
        a function that prints the table, then it computes a move for the computer,
        checks if the game was won by the computer or if it was draw
        """
        print(self.__table)
        print("Computer's turn.")
        self.__game.computer_moves()
        if self.__game.is_game_won():
            print(self.__table)
            print("Loser.")
        elif self.__game.is_draw():
            print(self.__table)
            print("Draw.")


    def run(self):
        """
        a function that runs the game in a loop until there is a winner or it is draw
        the game starts random, the first player being either human or computer
        """
        player = random.randint(0, 1)
        print("Game started...\n")
        if player == 0:
            while True:
                self.__players_turn()
                if self.__game.is_game_won() or self.__game.is_draw(): break
                self.__computers_turn()
                if self.__game.is_game_won() or self.__game.is_draw(): break
        else:
            while True:
                self.__computers_turn()
                if self.__game.is_game_won() or self.__game.is_draw(): break
                self.__players_turn()
                if self.__game.is_game_won() or self.__game.is_draw(): break
