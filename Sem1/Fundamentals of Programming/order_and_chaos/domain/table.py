class ValidException(Exception):
    pass


class Table():
    def __init__(self):
        self.__table = [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0]]
        self.__last_element = [0, 0]
        self.__is_filled_table = 0


    def add(self, x, y, type):
        if self.__table[x][y] == 0:
            self.__table[x][y] = type
            self.__is_filled_table += 1
            self.__last_element = [x, y]
        else:
            raise ValidException("existing element")


    def set_element_to_zero(self, x, y):
        self.__table[x][y] = 0


    def get_last_element(self):
        x = self.__last_element[0]
        y = self.__last_element[1]
        return x, y, self.__table[x][y]


    def set_last_element(self, x, y, value):
        self.__table[x][y] = value


    def __str__(self):
        s = ""
        for i in range(0, 6):
            for j in range(0, 6):
                if self.__table[i][j] == 1:
                    s += "x"
                elif self.__table[i][j] == -1:
                    s += "o"
                elif self.__table[i][j] == 0:
                    s += "."
            s += "\n"
        return s


    def get_element(self, x, y):
        return self.__table[x][y]


    def order_starts(self):
        return self.__is_filled_table % 2 == 0


    def is_five_on_line(self):
        return self.get_number_of_same_elements_on_line() >= 5


    def is_five_on_column(self):
        return self.get_number_of_same_elements_on_column() >= 5


    def is_five_on_diagonal(self):
        return self.get_number_of_same_elements_on_diagonal() >= 5


    def get_number_of_same_elements_on_line(self):
        x = self.__last_element[0]
        y = self.__last_element[1]
        c = self.__table[x][y]
        p = 1
        ycpy = y
        while y < 5 and self.__table[x][y + 1] == c and c != 0:
            p += 1
            y += 1
        y = ycpy
        while y > 0 and self.__table[x][y - 1] == c and c != 0:
            p += 1
            y -= 1
        return p


    def get_number_of_same_elements_on_column(self):
        x = self.__last_element[0]
        y = self.__last_element[1]
        c = self.__table[x][y]
        p = 1
        xcpy = x
        while x < 5 and self.__table[x + 1][y] == c and c != 0:
            p += 1
            x += 1
        x = xcpy
        while x > 0 and self.__table[x - 1][y] == c and c != 0:
            p += 1
            x -= 1
        return p


    def get_number_of_same_elements_on_diagonal(self):
        x = self.__last_element[0]
        y = self.__last_element[1]
        c = self.__table[x][y]
        p1 = 1
        xcpy = x
        ycpy = y
        while x < 5 and y < 5 and self.__table[x + 1][y + 1] == c and c != 0:
            p1 += 1
            x += 1
            y += 1
        x = xcpy
        y = ycpy
        while x > 0 and y > 0 and self.__table[x - 1][y - 1] == c and c != 0:
            p1 += 1
            x -= 1
            y -= 1
        p2 = 1
        x = xcpy
        y = ycpy
        while x < 5 and y > 0 and self.__table[x + 1][y - 1] == c and c != 0:
            p2 += 1
            x += 1
            y -= 1
        x = xcpy
        y = ycpy
        while x > 0 and y < 5 and self.__table[x - 1][y + 1] == c and c != 0:
            p2 += 1
            x -= 1
            y += 1
        if p1 > p2:
            return p1
        else:
            return p2


    def is_full_table(self):
        return self.__is_filled_table == 36
