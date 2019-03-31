from domain.table import ValidationException


class Service():
    def __init__(self, table_player, table_computer, computer, valid):
        self.__computer = computer
        self.__table_computer = table_computer
        self.__table_player = table_player
        self.__valid = valid


    def ships(self):
        return "\nPlayer's map.\n" + str(self.__table_player) + "\n\nComputer's map.\n" + str(self.__table_computer)


    def cheat(self):
        self.__table_computer.set_visible(True)


    def __convert_letter(self, x):
        if x == 'A':
            return 0
        elif x == 'B':
            return 1
        elif x == 'C':
            return 2
        elif x == 'D':
            return 3
        elif x == 'E':
            return 4
        elif x == 'F':
            return 5
        else:
            raise ValidationException("Invalid cell position.")


    def add(self, ship):
        self.__valid.validate(ship)
        x1 = self.__convert_letter(ship[0])
        y1 = int(ship[1])
        x2 = self.__convert_letter(ship[2])
        y2 = int(ship[3])
        x3 = self.__convert_letter(ship[4])
        y3 = int(ship[5])
        self.__table_player.add(x1, y1, x2, y2, x3, y3)


    def player_attack(self, cell):
        if len(cell) != 2:
            raise ValidationException("Invalid cell position.")
        x = self.__convert_letter(cell[0])
        try:
            y = int(cell[1])
        except:
            raise ValidationException("Invalid cell position.")
        return self.__table_computer.attack(x, y)


    def computer_attack(self):
        x, y = self.__computer.get_next_attack()
        return self.__table_player.attack(x, y)


    def player_won(self):
        return self.__table_computer.is_dead()


    def computer_won(self):
        return self.__table_player.is_dead()


    def computer_ships(self):
        try:
            x1, y1, x2, y2, x3, y3 = self.__computer.get_ship()
            self.__table_computer.add(x1, y1, x2, y2, x3, y3)
            x1, y1, x2, y2, x3, y3 = self.__computer.get_ship()
            self.__table_computer.add(x1, y1, x2, y2, x3, y3)
        except ValidationException:
            self.computer_ships()


    def player_ships_exist(self):
        return self.__table_player.are_there_any_ships()
