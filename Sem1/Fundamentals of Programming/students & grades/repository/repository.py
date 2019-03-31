import pickle


class Repository(object):
    def __init__(self):
        self._elems = []
        self.__index = 0


    def __len__(self):
        return len(self._elems)


    def __str__(self):
        s = ""
        for i in self.get_all():
            if i != self.get_all()[-1]:
                s += str(i) + "\n"
            else:
                s += str(i)
        return s


    def add(self, element):
        if element not in self._elems:
            self._elems.append(element)
        else:
            raise RepositoryException("Existing element.")


    def find(self, element):
        if element in self._elems:
            i = self._elems.index(element)
            return self._elems[i]
        else:
            raise RepositoryException("Inexisting element.")


    def update(self, element):
        if element in self._elems:
            i = self._elems.index(element)
            self._elems[i] = element
        else:
            raise RepositoryException("Inexisting element.")


    def remove(self, element):
        if element in self._elems:
            self._elems.remove(element)
        else:
            raise RepositoryException("Inexisting element.")


    def get_all(self):
        return self._elems


    def __getitem__(self, key):
        for i in self._elems:
            if key == i.get_ident():
                return i
        return None


    def __setitem__(self, key, item):
        for i in range(len(self._elems)):
            if key == self._elems[i].get_ident():
                self._elems[i] = item


    def __delitem__(self, key):
        pos = -1
        for i in range(len(self._elems)):
            if key == self._elems[i].get_ident():
                pos = i
                break
        del self._elems[pos]


    def __iter__(self):
        return self


    def __next__(self):
        self.__index += 1
        if self.__index >= len(self._elems):
            raise StopIteration
        return self._elems[self.__index]


    def filter(self, f):
        return [x for x in self._elems if f(x)]


    @staticmethod
    def __gnomesort(l, f):
        i = 0
        n = len(l)
        while i < n:
            if i and f(l[i]) < f(l[i - 1]):
                l[i], l[i - 1] = l[i - 1], l[i]
                i -= 1
            else:
                i += 1
        return l


    def sort(self, f):
        return self.__gnomesort(self._elems, f)


class RepositoryException(Exception):
    pass


class FileRepository(Repository):

    def __read_all_from_file(self):
        with open(self.__filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if len(line):
                    obj = self.__line_to_object(line)
                    self._elems.append(obj)


    def __init__(self, filename, line_to_object, object_to_line):
        Repository.__init__(self)
        self.__filename = filename
        self.__line_to_object = line_to_object
        self.__object_to_line = object_to_line
        self.__read_all_from_file()


    def __append_element_to_file(self, element):
        with open(self.__filename, "a") as f:
            line = self.__object_to_line(element)
            f.write(line + "\n")


    def add(self, element):
        Repository.add(self, element)
        self.__append_element_to_file(element)


    def __write_all_to_file(self):
        with open(self.__filename, "w") as f:
            for elem in self._elems:
                line = self.__object_to_line(elem)
                f.write(line + "\n")


    def update(self, element):
        Repository.update(self, element)
        self.__write_all_to_file()


    def remove(self, element):
        Repository.remove(self, element)
        self.__write_all_to_file()


class BinaryRepository(Repository):

    def __read_binary_file(self):
        with open(self.__filename, "rb") as f:
            self._elems = pickle.load(f)


    def __init__(self, filename):
        Repository.__init__(self)
        self.__filename = filename
        self.__read_binary_file()


    def __write_binary_file(self):
        with open(self.__filename, "wb") as f:
            pickle.dump(self._elems, f)
            f.close()


    def add(self, element):
        Repository.add(self, element)
        self.__write_binary_file()


    def update(self, element):
        Repository.update(self, element)
        self.__write_binary_file()


    def remove(self, element):
        Repository.remove(self, element)
        self.__write_binary_file()
