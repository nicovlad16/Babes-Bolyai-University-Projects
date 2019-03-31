from domain.table import ValidException


class Console:
    def __init__(self, game):
        self.__game = game


    def run(self):
        while True:
            cmd = input("1.Start new game.\n2.Start saved game.\n3.Exit.")
            if not cmd:
                print("Invalid command:")
            elif cmd == "0":
                exit(0)
            elif cmd == "1":
                self.__start_new_game()
            elif cmd == "2":
                self.__start_saved_game()


    def __start_game(self):
        if self.__game.order_starts():
            while True:
                if self.__is_ended():
                    return
                print(self.__game.get_table())
                print("Order's turn.\n")
                self.__computer_moves()
                if self.__is_ended():
                    return
                print(self.__game.get_table())
                print("Chaos's turn\n")
                self.__player_moves()

        else:
            while True:
                if self.__is_ended():
                    return
                print(self.__game.get_table())
                print("Chaos's turn\n")
                self.__player_moves()
                if self.__is_ended():
                    return
                print(self.__game.get_table())
                print("Order's turn.\n")


    def __computer_moves(self):
        self.__game.computer_add_move()


    def __player_moves(self):
        try:
            x = input("x coordinate: ")
            y = input("y coordiante: ")
            type = input("type (x or o): ")
            self.__game.player_add_move(x, y, type)
        except ValidException as ve:
            print(ve)
            self.__player_moves()


    def __is_ended(self):
        if self.__game.chaos_won():
            print(self.__game.get_table())
            print("Chaos won.\n")
            return True
        elif self.__game.order_won():
            print(self.__game.get_table())
            print("Order won.\n")
            return True
        return False


    def __start_new_game(self):
        self.__game.start_new_game()
        self.__start_game()


    def __start_saved_game(self):
        self.__game.start_saved_game()
        self.__start_game()
