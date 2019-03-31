from domain.table import ValidationException


class Game():

    def __init__(self, service):
        self.__service = service


    def start(self):
        while True:
            try:
                self.__show_ships()
                cmd = input("Insert command: ")
                cmd.strip()
                cmds = cmd.split(" ")
                if not cmds:
                    print("Invalid command.")
                elif len(cmds) > 2:
                    print("Invalid command.")
                elif len(cmds) == 1:
                    if cmds[0] == "start" and self.__service.player_ships_exist() == True:
                        self.__comp_add_ships()
                        self.__start()
                    else:
                        print("Invalid command.")
                else:
                    if cmds[0] == "ship":
                        self.__ship(cmds[1])
                    else:
                        print("Invalid command.")
            except ValidationException as e:
                print(e)


    def __start(self):
        while True:
            try:
                self.__show_ships()
                cmd = input("Insert command: ")
                cmd.strip()
                cmds = cmd.split(" ")
                if not cmds:
                    print("Invalid command.")
                elif len(cmds) > 2:
                    print("Invalid command.")
                elif len(cmds) == 1:
                    if cmds[0] == "cheat":
                        self.__cheat()
                    else:
                        print("Invalid command.")
                else:
                    if cmds[0] == "attack":
                        self.__attack(cmds[1])
                        if self.__service.player_won():
                            print("You won.")
                            exit(0)
                        self.__comp_attack()
                        if self.__service.computer_won():
                            print("You lost.")
                            exit(0)
                    else:
                        print("Invalid command.")
            except ValidationException as e:
                print(e)


    def __cheat(self):
        self.__service.cheat()


    def __attack(self, cell):
        if self.__service.player_attack(cell) == True:
            print("You hit.")
        else:
            print("You missed.")


    def __ship(self, ship):
        self.__service.add(ship)
        print("Succesfully added. ")


    def __show_ships(self):
        print(self.__service.ships())


    def __comp_attack(self):
        if self.__service.computer_attack() == True:
            "Computer hit."
        else:
            print("Computer missed.")


    def __comp_add_ships(self):
        self.__service.computer_ships()
