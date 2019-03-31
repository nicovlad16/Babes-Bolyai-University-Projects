from ctrl.ctrl import CtrlException
from domain.valid import ValidException
from repo.repo import RepoException


class Console(object):
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        self.__commands = {"create": [self.__ui_create],
                           "add": [self.__ui_add],
                           "start": [self.__ui_start]}


    def run(self):
        while True:
            cmd = input(">>")
            cmd.strip()
            cmds = cmd.split(" ")
            try:
                if not cmds:
                    print("Invalid command.")
                elif len(cmds) == 1 and cmds[0] == "exit":
                    exit(0)
                elif cmds[0] in self.__commands:
                    self.__commands[cmds[0]][0](cmds[1:])
                else:
                    print("Invalid command.")
            except Exception as e:
                print(e)


    def __ui_create(self, params):
        if len(params) != 3:
            print("Invalid command.")
            return
        difficulty = params[0]
        no = params[1]
        file = params[2]
        if not self.__ctrl.create_quiz(difficulty, no, file):
            print("quiz cannot be created")
            return
        print("Succesfully created.")


    def __ui_add(self, params):
        self.__ctrl.add(params)
        print("Succesfully added.")


    def __ui_start(self, params):
        if len(params) != 1:
            print("Invalid command.")
            return
        file = params[0]
        if not self.__ctrl.start(file):
            print("inexistent quiz.")
            return
        while True:
            if self.__ctrl.is_game_ended():
                score = self.__ctrl.get_score()
                possible = self.__ctrl.get_possible_score()
                print("your final score is " + str(score) + " out of " + str(possible))
                return
            score = self.__ctrl.get_score()
            print("Your current score is: " + str(score))
            question = self.__ctrl.get_current_question()
            print(question)
            answer = input("answer: ")
            self.__ctrl.check_answer(answer.strip())
            print("\n")
