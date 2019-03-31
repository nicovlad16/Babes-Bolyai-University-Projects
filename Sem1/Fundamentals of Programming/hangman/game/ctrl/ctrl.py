import random

from domain.sentence import Sentence


class Ctrl(object):
    def __init__(self, repo, valid):
        self.__valid = valid
        self.__repo = repo
        self.__hangman = "hangman"
        self.__letters = []
        self.__i = 0


    def add(self, sentence):
        self.__valid.validate(sentence)
        self.__repo.add(Sentence(sentence))


    def get_random_sentence(self):
        sentences = self.__repo.get_all()
        idx = random.randint(0, len(sentences) - 1)
        return sentences[idx]


    def add_letter(self, letter, sentence):
        add = sentence.add_letter(letter)
        if add == False:
            self.__i += 1
        return sentence


    def get_hangman(self):
        s = ""
        for i in range(0, self.__i):
            s += self.__hangman[i]
        return s


    def is_game_lost(self):
        return self.__i == 7


    def is_game_won(self, sentence):
        return sentence.is_ended()
