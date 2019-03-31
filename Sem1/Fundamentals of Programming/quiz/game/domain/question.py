class Question():
    def __init__(self, idx, q, a1, a2, a3, right, diff):
        self.__diff = diff
        self.__right = right
        self.__a3 = a3
        self.__a2 = a2
        self.__a1 = a1
        self.__q = q
        self.__idx = idx


    def get_id(self):
        return self.__idx


    def get_diff(self):
        return self.__diff


    def get_right(self):
        return self.__right


    def get_a1(self):
        return self.__a1


    def get_a2(self):
        return self.__a2


    def get_a3(self):
        return self.__a3


    def get_q(self):
        return self.__q


    def __eq__(self, other):
        return isinstance(self, other.__class__) and self.__idx == other.__idx


    def __str__(self):
        return self.__q + "\n" + self.__a1 + "\n" + self.__a2 + "\n" + self.__a3 + "\n"
