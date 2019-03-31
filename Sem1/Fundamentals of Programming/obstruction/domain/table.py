class ValidationException(Exception):
    pass


class Table(object):

    def __init__(self):
        self._table = [[-2, -2, -2, -2, -2, -2, -2, -2], \
                       [-2, -2, -2, -2, -2, -2, -2, -2], \
                       [-2, -2, -2, -2, -2, -2, -2, -2], \
                       [-2, -2, -2, -2, -2, -2, -2, -2], \
                       [-2, -2, -2, -2, -2, -2, -2, -2], \
                       [-2, -2, -2, -2, -2, -2, -2, -2], \
                       [-2, -2, -2, -2, -2, -2, -2, -2], \
                       [-2, -2, -2, -2, -2, -2, -2, -2]]
        self._player = 0
        self._empty_spaces = 64


    def get_table(self):
        return self._table


    def add(self, x, y):
        if self._table[x][y] != -2:
            raise ValidationException("Invalid position.")
        self._table[x][y] = self._player
        self._player = (self._player + 1) % 2
        self._empty_spaces -= 1
        self.__fill_spaces(x, y)


    def __fill_spaces(self, x, y):
        try:
            if self._table[x - 1][y - 1] == -2 and x - 1 >= 0 and y - 1 >= 0:
                self._table[x - 1][y - 1] = -1
                self._empty_spaces -= 1
        except IndexError:
            pass
        try:
            if self._table[x - 1][y] == -2 and x - 1 >= 0:
                self._table[x - 1][y] = -1
                self._empty_spaces -= 1
        except IndexError:
            pass
        try:
            if self._table[x - 1][y + 1] == -2 and x - 1 >= 0:
                self._table[x - 1][y + 1] = -1
                self._empty_spaces -= 1
        except IndexError:
            pass
        try:
            if self._table[x][y - 1] == -2 and y - 1 >= 0:
                self._table[x][y - 1] = -1
                self._empty_spaces -= 1
        except IndexError:
            pass
        try:
            if self._table[x][y + 1] == -2:
                self._table[x][y + 1] = -1
                self._empty_spaces -= 1
        except IndexError:
            pass
        try:
            if self._table[x + 1][y - 1] == -2 and y - 1 >= 0:
                self._table[x + 1][y - 1] = -1
                self._empty_spaces -= 1
        except IndexError:
            pass
        try:
            if self._table[x + 1][y] == -2:
                self._table[x + 1][y] = -1
                self._empty_spaces -= 1
        except IndexError:
            pass
        try:
            if self._table[x + 1][y + 1] == -2:
                self._table[x + 1][y + 1] = -1
                self._empty_spaces -= 1
        except IndexError:
            pass


    def is_full_table(self):
        return self._empty_spaces == 0


    def __str__(self):
        abc = "ABCDEFGH"
        s = "  "
        for i in range(0, 8):
            s += str(i) + " "
        s += '\n'
        s += "  "
        for i in range(0, 15):
            s += "_"
        s += " "
        s += "\n"
        for i in range(0, 8):
            s += abc[i]
            s += "|"
            for j in range(0, 8):
                if self._table[i][j] == -2:
                    s += "#"
                if self._table[i][j] == -1:
                    s += " "
                if self._table[i][j] == 0:
                    s += "O"
                if self._table[i][j] == 1:
                    s += "X"
                if j < 7:
                    s += " "
            s += "|"
            s += "\n"
        s += "  "
        for i in range(0, 15):
            s += "⎺"
        s += " "
        s += "\n"
        return s
