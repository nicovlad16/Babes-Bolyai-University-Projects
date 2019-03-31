class Sentence(object):
    def __init__(self, sentence):
        self.__sentence = sentence
        self.__letters = []
        words = sentence.split(" ")
        self.__letters.append(" ")
        for i in words:
            letter = i[0]
            self.__letters.append(letter)
            letter = i[-1]
            self.__letters.append(letter)


    def get_sentence(self):
        return self.__sentence


    def set_sentence(self, value):
        self.__sentence = value


    def __eq__(self, other):
        return isinstance(self, other.__class__) and self.__sentence == other.__sentence


    def __str__(self):
        s = ""
        for i in self.__sentence:
            if i in self.__letters:
                s += i
            else:
                s += "_"
        return s


    def add_letter(self, l):
        if l in self.__letters:
            return False
        if l in self.__sentence:
            self.__letters.append(l)
            return True
        return False


    def is_ended(self):
        for i in self.__sentence:
            if i not in self.__letters:
                return False
        return True
