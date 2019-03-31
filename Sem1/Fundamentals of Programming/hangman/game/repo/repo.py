from domain.sentence import Sentence


class RepositoryException(Exception):
    pass


class Repo(object):
    def __init__(self):
        self.__elems = []
        self.__filename = "words"
        self.__read_from_file()


    def __read_from_file(self):
        with open(self.__filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line:
                    sentence = Sentence(line)
                    self.__elems.append(sentence)


    def add(self, sentence):
        if sentence in self.__elems:
            raise RepositoryException("existing sentence")
        self.__elems.append(sentence)
        with open(self.__filename, "a") as f:
            f.write("\n" + sentence.get_sentence())


    def get_all(self):
        return self.__elems
