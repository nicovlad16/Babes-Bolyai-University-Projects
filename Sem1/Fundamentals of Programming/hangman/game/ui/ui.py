import re
from domain.valid import ValidException
from repo.repo import RepositoryException


class Console(object):

    def __init__(self, ctrl):
        self.__ctrl = ctrl


    def run(self):
        while True:
            try:
                print("\n1.Add sentence.\n2.Start game.\n0.Exit\n")
                cmd = input(">>  ")
                if not cmd:
                    print("Invalid command. ")
                elif cmd == "0":
                    exit(0)
                elif cmd == "1":
                    self.__ui_add()
                elif cmd == "2":
                    self.__ui_start()
                else:
                    print("Invalid command. ")
            except ValidException as e:
                print(e)
            except RepositoryException as e:
                print(e)


    def __ui_add(self):
        sentence = input("sentence: ")
        self.__ctrl.add(sentence)
        print("successfully added")


    def __ui_start(self):
        sentence = self.__ctrl.get_random_sentence()
        while True:
            self.__print(sentence)
            letter = self.__read_letter("letter: ")
            sentence = self.__ctrl.add_letter(letter, sentence)
            if self.__ctrl.is_game_won(sentence):
                self.__print(sentence)
                print("\nyou won. gj.")
                exit(0)
            if self.__ctrl.is_game_lost():
                self.__print(sentence)
                print("\nyou lost. :(")
                exit(0)


    def __print(self, sentence):
        print("sentence: " + str(sentence))
        hangman = self.__ctrl.get_hangman()
        print("game over in: " + hangman)


    def __read_letter(self, txt):
        while True:
            letter = input(txt)
            match = re.match("[a-z]", letter)
            if match != None and len(letter) == 1:
                return letter
