class ValidationException(Exception):
    pass


class Table():

    def __init__(self, visible):
        self.__visible = visible
        self.__table = [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0]]
        self.__ship1 = []
        self.__ship2 = []
        self.__hits = 0


    def set_visible(self, value):
        self.__visible = value


    def get_ship1(self):
        return self.__ship1


    def get_ship2(self):
        return self.__ship2


    def __validate_ship(self, x1, y1, x2, y2, x3, y3):
        """
        a function that takes the coordinates of a ship, and checks if on the given positions,
        there are not already any ships
        """
        i = self.__ship1
        if (i[0][0] == x1 and i[0][1] == y1) or (i[1][0] == x1 and i[1][1] == y1) or (
                i[2][0] == x1 and i[2][1] == y1) or \
                (i[0][0] == x2 and i[0][1] == y2) or (i[1][0] == x2 and i[1][1] == y2) or (
                i[2][0] == x2 and i[2][1] == y2) or \
                (i[0][0] == x3 and i[0][1] == y3) or (i[1][0] == x3 and i[1][1] == y3) or (
                i[2][0] == x3 and i[2][1] == y3):
            raise ValidationException("overlapping ship")


    def __add_ship_on_map(self):
        """
        a function that adds two ships on the map
        the value 0 becomes 1
        """
        for i in self.__ship1:
            self.__table[i[0]][i[1]] = 1
        for i in self.__ship2:
            self.__table[i[0]][i[1]] = 1


    def __remove_ship_from_map(self, ship):
        """
        a function that removes a ship from the map
        the coordinates, which are 1, become 0
        """
        for i in ship:
            self.__table[i[0]][i[1]] = 0


    def add(self, x1, y1, x2, y2, x3, y3):
        """
        input: the coordinates of a ship
        the function checks if the ship1 is empty, the it will have these coordinates
        else checks if the ship2 is empty, if so ship2 will have the coordinates
        else ship1 will have the coordinates of ship2 and ship2 will get the new coordinates
        ;this happens only if the coordinates are valid, there is no other ship placed on
        some of the positions
        otherwise ships remain the same and an exception is being raised
        """
        if self.__ship1 == []:
            self.__ship1.append([x1, y1])
            self.__ship1.append([x2, y2])
            self.__ship1.append([x3, y3])
            self.__add_ship_on_map()
        elif self.__ship2 == []:
            try:
                self.__validate_ship(x1, y1, x2, y2, x3, y3)
                self.__ship2.append([x1, y1])
                self.__ship2.append([x2, y2])
                self.__ship2.append([x3, y3])
                self.__add_ship_on_map()
            except ValidationException:
                raise ValidationException("overlapping ship")
        else:
            try:
                self.__remove_ship_from_map(self.__ship1)
                self.__ship1.clear()
                self.__ship1.append(self.__ship2[0])
                self.__ship1.append(self.__ship2[1])
                self.__ship1.append(self.__ship2[2])
                self.__add_ship_on_map()
                self.__remove_ship_from_map(self.__ship2)
                self.__validate_ship(x1, y1, x2, y2, x3, y3)
                self.__ship2.clear()
                self.__ship2.append([x1, y1])
                self.__ship2.append([x2, y2])
                self.__ship2.append([x3, y3])
                self.__add_ship_on_map()
            except ValidationException:
                raise ValidationException("overlapping ship")


    def __str__(self):
        """

        :return: s - a string --> how the map will look like
        """
        litere = "ABCDEF"
        s = "  012345\n"
        for i in range(0, 6):
            s += litere[i] + " "
            for j in range(0, 6):
                if self.__visible == True:
                    if self.__table[i][j] == 0:
                        s += "."
                    elif self.__table[i][j] == 1:
                        s += "#"
                    elif self.__table[i][j] == -1:
                        s += "o"
                    elif self.__table[i][j] == 2:
                        s += "+"
                else:
                    if self.__table[i][j] == 0 or self.__table[i][j] == 1:
                        s += "."
                    elif self.__table[i][j] == -1:
                        s += "o"
                    elif self.__table[i][j] == 2:
                        s += "+"
            s += "\n"
        return s


    def attack(self, x, y):
        """
        input: coordinates of a cell
        :return: True if the position is 1, there is a ship on that coordinate
                 False if the position is different than 1
        """
        if self.__table[x][y] == 1:
            self.__table[x][y] = 2
            self.__hits += 1
            return True
        elif self.__table[x][y] != 2:
            self.__table[x][y] = -1
            return False
        return False


    def is_dead(self):
        """
        :return: True if all the parts of the ships have been hit, False otherwise
        """
        return self.__hits == 6


    def are_there_any_ships(self):
        """
        :return: True if there are two ships on the map, False otherwise
        """
        return self.__ship1 != [] and self.__ship2 != []
