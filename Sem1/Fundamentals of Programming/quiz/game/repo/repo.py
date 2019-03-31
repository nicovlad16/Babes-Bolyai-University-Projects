from domain.question import Question


class Repo(object):
    def __init__(self, filename):
        self.__elems = []
        self.__filename = filename
        try:
            self.__read_from_file()
        except FileNotFoundError:
            with open(self.__filename, "w") as f:
                f.write("")


    def __append_elem_to_file(self, question):
        with open(self.__filename, "a") as f:
            line = "\n" + str(question.get_id()) + ";" + question.get_q() + ";" + question.get_a1() + ";" + \
                   question.get_a2() + ";" + question.get_a3() + ";" + question.get_right() + \
                   ";" + question.get_diff()
            f.write(line)


    def __read_from_file(self):
        with open(self.__filename, "r+") as f:
            for line in f.readlines():
                line = line.strip()
                if line:
                    elems = line.split(";")
                    idx = int(elems[0])
                    q = elems[1]
                    a1 = elems[2]
                    a2 = elems[3]
                    a3 = elems[4]
                    right = elems[5]
                    diff = elems[6]
                    question = Question(idx, q, a1, a2, a3, right, diff)
                    self.__elems.append(question)


    def add(self, question):
        if question in self.__elems:
            raise RepoException("existing question")
        self.__elems.append(question)
        self.__append_elem_to_file(question)


    def get_all(self):
        return self.__elems[:]


    def __len__(self):
        return len(self.__elems)


    def remove_last_element(self):
        if self.__elems:
            self.__elems.pop(-1)
        self.__write_all_to_file()


    def __write_all_to_file(self):
        with open(self.__filename, "w") as f:
            f.write("")
        for elem in self.__elems:
            self.__append_elem_to_file(elem)


class RepoException(Exception):
    pass
