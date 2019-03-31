'''
Created on Dec 21, 2017

@author: nvlad
'''


class ValidationException(Exception):
    pass


class Table():
    """
    a class for the table of the game, an 8*8 matrix
    """


    def __init__(self):
        self.__table = [[-1, -1, -1, -1, -1, -1, -1, -1], \
                        [-1, -1, -1, -1, -1, -1, -1, -1], \
                        [-1, -1, -1, -1, -1, -1, -1, -1], \
                        [-1, -1, -1, -1, -1, -1, -1, -1], \
                        [-1, -1, -1, -1, -1, -1, -1, -1], \
                        [-1, -1, -1, -1, -1, -1, -1, -1], \
                        [-1, -1, -1, -1, -1, -1, -1, -1], \
                        [-1, -1, -1, -1, -1, -1, -1, -1]]
        self.__player = 0
        self.__filled_spaces = 0
        self.__filled_cols = [0, 0, 0, 0, 0, 0, 0, 0]
        self.__last_element = {"x": -1, "y": -1}


    def get_player(self):
        return self.__player


    def get_filled_spaces(self):
        return self.__filled_spaces


    def get_filled_cols(self, y):
        return self.__filled_cols[y]


    def get_last_element(self):
        return self.__last_element


    def set_player(self, value):
        self.__player = value


    def set_filled_cols(self, y, value):
        self.__filled_cols[y] = value


    def set_last_element(self, value):
        self.__last_element = value


    def add_move(self, y):
        """
        :param y: the move, the position that should be added to the table, the index of column
        a function that adds a move on the table, checking if it is a valid move, it has to be a number between 0 and 7
        and the column on which it will be put must have an empty space, if not it will raise ValidationException
        if the move is valid it will be added to the table, the player will be changed and the number of moves on
        that column will increase, as well as the number of all moves on the table
        also, the last element will be set with the indeces of this move
        """
        if y < 0 or y > 7:
            raise ValidationException("Invalid position. It should be an integer between 0 and 7.")
        elif self.is_filled_col(y):
            raise ValidationException("Invalid position.")
        x = 8 - self.__filled_cols[y] - 1
        self.__table[x][y] = self.__player
        self.__player = (1 + self.__player) % 2
        self.__filled_spaces += 1
        self.__filled_cols[y] += 1
        self.set_last_element({"x": x, "y": y})


    def change_element(self, x, y, value):
        """
        a function that changes an element of the matrix, having x and y as coordinates, with the value
        (this is used by the AI)
        :param x:
        :param y:
        :param value:
        """
        self.__table[x][y] = value


    def __str__(self):
        """
        how the table will be printed
        :return: a string - s
        """
        s = " "
        for i in range(0, 8):
            s += str(i)
            s += " "
        s += "\n"
        s += " "
        for i in range(0, 16):
            s += "_"
        s += " "
        s += "\n"
        for i in range(0, 8):
            s += "|"
            for j in range(0, 8):
                if self.__table[i][j] == -1:
                    s += " "
                elif self.__table[i][j] == 0:
                    s += "●"
                else:
                    s += "◯"
                s += " "
            s += "|"
            s += "\n"
        s += " "
        for i in range(0, 16):
            s += "⎺"
        s += " "
        s += "\n"
        return s


    def is_full_table(self):
        """
        :return: True if all the -1s in the table have been changed with another value, False otherwise
        """
        if self.__filled_spaces == 64:
            return True
        else:
            return False


    def is_filled_col(self, y):
        """
        :param y: the column
        :return: True if all the -1s on the respective column have been changed with another value, False otherwise
        """
        return self.__filled_cols[y] > 7


    def is_four_on_line(self):
        """
        :return: True if there is a line having four elements of the same type, False otherwise
        """
        return self.get_number_of_same_elements_on_line() >= 4


    def is_four_on_column(self):
        """
        :return: True if there is a column having four elements of the same type, False otherwise
        """
        return self.get_number_of_same_elements_on_column() >= 4


    def is_four_on_diagonal(self):
        """
        :return: True if there is a diagonal having four elements of the same type, False otherwise
        """
        return self.get_number_of_same_elements_on_diagonal() >= 4


    def get_number_of_same_elements_on_line(self):
        """
        a function that numbers the same consecutive elements on a line, near the last element; it goes right and left
        :return: p - the number of such elements, it is at least 1
        """
        x = self.__last_element["x"]
        y = self.__last_element["y"]
        c = self.__table[x][y]
        p = 1
        ycpy = y
        while y < 7 and self.__table[x][y + 1] == c and c != -1:
            p += 1
            y += 1
        y = ycpy
        while y > 0 and self.__table[x][y - 1] == c and c != -1:
            p += 1
            y -= 1
        return p


    def get_number_of_same_elements_on_column(self):
        """
        a function that numbers the same consecutive elements on a column, near the last element; it goes up and down
        :return: p - the number of such elements, it is at least 1
        """
        x = self.__last_element["x"]
        y = self.__last_element["y"]
        c = self.__table[x][y]
        p = 1
        xcpy = x
        while x < 7 and self.__table[x + 1][y] == c and c != -1:
            p += 1
            x += 1
        x = xcpy
        while x > 0 and self.__table[x - 1][y] == c and c != -1:
            p += 1
            x -= 1
        return p


    def get_number_of_same_elements_on_diagonal(self):
        """
        a function that numbers the same consecutive elements on both diagonals, near the last element
        :return: p - the number of such elements, it is at least 1
        """
        x = self.__last_element["x"]
        y = self.__last_element["y"]
        c = self.__table[x][y]
        p1 = 1
        xcpy = x
        ycpy = y
        while x < 7 and y < 7 and self.__table[x + 1][y + 1] == c and c != -1:
            p1 += 1
            x += 1
            y += 1
        x = xcpy
        y = ycpy
        while x > 0 and y > 0 and self.__table[x - 1][y - 1] == c and c != -1:
            p1 += 1
            x -= 1
            y -= 1
        p2 = 1
        x = xcpy
        y = ycpy
        while x < 7 and y > 0 and self.__table[x + 1][y - 1] == c and c != -1:
            p2 += 1
            x += 1
            y -= 1
        x = xcpy
        y = ycpy
        while x > 0 and y < 7 and self.__table[x - 1][y + 1] == c and c != -1:
            p2 += 1
            x -= 1
            y += 1
        if p1 > p2:
            return p1
        else:
            return p2
