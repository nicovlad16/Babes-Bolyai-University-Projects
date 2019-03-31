import random

from domain.question import Question
from repo.repo import Repo, RepoException


class CtrlException(Exception):
    pass


class Ctrl(object):
    def __init__(self, repo, valid):
        self.__valid = valid
        self.__repo = repo
        self.__current_question = Question(1, "", "", "", "", "", "")
        self.__points = 0
        self.__questions = []
        self.__no = 0
        self.__total = 0


    def add(self, params):
        question_elems = self.__valid.validate_question_from_ui(params)
        idx = int(question_elems[0])
        q = question_elems[1]
        a1 = question_elems[2]
        a2 = question_elems[3]
        a3 = question_elems[4]
        right = question_elems[5]
        diff = question_elems[6]
        question = Question(idx, q, a1, a2, a3, right, diff)
        self.__valid.validate(question)
        self.__repo.add(question)


    def create_quiz(self, diff, no, file):
        self.__valid.validate_create_quiz(diff, no, file)
        no = int(no)
        elems = self.__repo.get_all()
        copy = elems.copy()
        elems = list(filter(lambda x: x.get_diff() == diff, elems))
        copy = [i for i in copy + elems if i not in copy or i not in elems]
        if len(elems) < no // 2:
            return False
        random.shuffle(copy)
        if len(copy) < no // 2:
            return False
        for i in range(no // 2):
            elems.append(copy[i])
        random.shuffle(elems)
        repo = Repo(file)
        for i in elems:
            try:
                repo.add(i)
            except RepoException:
                pass
        i = len(repo)
        while i > no:
            repo.remove_last_element()
            i = len(repo)
        return True


    def start(self, file):
        self.__points = 0
        self.__total = 0
        repo = Repo(file)
        self.__questions = repo.get_all()
        if not self.__questions:
            return False
        self.__question = self.__questions[0]
        self.__no = 1
        return True


    def is_game_ended(self):
        return self.__no == len(self.__questions)


    def get_score(self):
        return self.__points


    def get_possible_score(self):
        return self.__total


    def get_current_question(self):
        return self.__question


    def check_answer(self, answer):
        if not answer:
            return
        if answer == self.__question.get_right():

            if self.__question.get_diff() == "easy":
                self.__total += 1
            elif self.__question.get_diff() == "medium":
                self.__total += 2
            else:
                self.__total += 3

            if self.__question.get_diff() == "easy":
                self.__points += 1
                self.__question = self.__questions[self.__no]
                self.__no += 1
            elif self.__question.get_diff() == "medium":
                self.__points += 2
                self.__question = self.__questions[self.__no]
                self.__no += 1
            elif self.__question.get_diff() == "hard":
                self.__points += 3
                self.__question = self.__questions[self.__no]
                self.__no += 1
        else:
            self.__question = self.__questions[self.__no]
            self.__no += 1

            if self.__question.get_diff() == "easy":
                self.__total += 1
            elif self.__question.get_diff() == "medium":
                self.__total += 2
            else:
                self.__total += 3
