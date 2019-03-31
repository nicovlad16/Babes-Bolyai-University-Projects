import random


class Computer(object):
    """
    a class for the AI, a super smart computer who doesn't win all the games,
    but a good part of them, "an entertaining opponent for the human player"
    """


    def __init__(self, table):
        self.__table = table


    def get_next_move(self):
        """
        a function that checks the best move he could do in order to win the game or not to lose:
            it first checks if he could win, making 4 moves in a row, if so returns the position
            if not such move found, it checks if the other player could make a winning move, then it returns that position
            elif it checks if he could make 3 moves in a row, returning the position
            elif it checks for the opponent, then returns the position
            else returns almost a random position
            (the position is a number between 0-7)
        """
        if self.__table.get_filled_spaces() == 0 or self.__table.get_filled_spaces() == 1:
            return random.randint(2, 5)

        comp = [0, 0, 0, 0, 0, 0, 0, 0]
        last = self.__table.get_last_element()
        player = self.__table.get_player()
        for y in range(0, 8):
            if not self.__table.is_filled_col(y):
                self.__table.add_move(y)
                line = self.__table.get_number_of_same_elements_on_line()
                column = self.__table.get_number_of_same_elements_on_column()
                diagonal = self.__table.get_number_of_same_elements_on_diagonal()
                comp[y] = max(line, column, diagonal)
                #                 print("comp", player, "y: ", y, " max: ", comp[y], "diagonal: ", diagonal, "column: ", column, "line: ", line)
                self.__table.set_player(player)
                self.__table.change_element(self.__table.get_last_element()["x"], y, -1)
                self.__table.set_filled_cols(y, self.__table.get_filled_cols(y) - 1)
        self.__table.set_last_element(last)

        for y in range(len(comp)):
            if comp[y] >= 4:
                return y

        self.__table.set_player((player + 1) % 2)
        human = [0, 0, 0, 0, 0, 0, 0, 0]
        last = self.__table.get_last_element()
        player = self.__table.get_player()
        for y in range(0, 8):
            if not self.__table.is_filled_col(y):
                self.__table.add_move(y)
                line = self.__table.get_number_of_same_elements_on_line()
                column = self.__table.get_number_of_same_elements_on_column()
                diagonal = self.__table.get_number_of_same_elements_on_diagonal()
                human[y] = max(line, column, diagonal)
                #                 print("human", player, "y: ", y, " max: ", human[y], "diagonal: ", diagonal, "column: ", column, "line: ", line)
                self.__table.set_player(player)
                self.__table.change_element(self.__table.get_last_element()["x"], y, -1)
                self.__table.set_filled_cols(y, self.__table.get_filled_cols(y) - 1)
        self.__table.set_last_element(last)
        self.__table.set_player((player + 1) % 2)

        for y in range(len(human)):
            if human[y] >= 4:
                return y

        for y in range(len(comp)):
            if comp[y] == 3:
                return y

        for y in range(len(human)):
            if human[y] == 3:
                return y

        for y in range(len(comp)):
            maxim = max(comp)
            return comp.index(maxim)
