import random

from domain.table import ValidException


class Computer():
    def __init__(self, table):
        self.__table = table


    def get_next_move(self):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        type = random.randint(0, 1)
        if type == 1:
            type = -1
        elif type == 0:
            type = 1
        return x, y, type
    #     possible_moves = [[0, 0, 0],  [0, 0, 0], [0, 0, 0], [0, 0,0], [0, 0,0], [0, 0,0]]
    #     for i in range(0, 6):
    #         for j in range(0, 6):
    #             if self.__table.get_element(i, j) == 0:
    #                 self.__table.add(i, j, 1)
    #                 line = self.__table.get_number_of_same_elements_on_line()
    #                 column = self.__table.get_number_of_same_elements_on_column()
    #                 diagonal = self.__table.get_number_of_same_elements_on_diagonal()
    #                 maxim1 = max(line, column, diagonal)
    #                 print("1:   " + str(i) + " "+str(j) + "\n" +str(self.__table) + "\n")
    #                 self.__table.set_element_to_zero(i, j)
    #                 self.__table.add(i, j, -1)
    #                 line = self.__table.get_number_of_same_elements_on_line()
    #                 column = self.__table.get_number_of_same_elements_on_column()
    #                 diagonal = self.__table.get_number_of_same_elements_on_diagonal()
    #                 maxim2 = max(line, column, diagonal)
    #                 print("-1:   " + str(i) + " "+str(j) + "\n" +str(self.__table) + "\n")
    #
    #                 self.__table.set_element_to_zero(i, j)
    #
    #                 maxim = max(maxim1, maxim2)
    #                 if maxim > possible_moves[i][1]:
    #                     possible_moves[i][0] = j
    #                     possible_moves[i][1] = maxim
    #                     if maxim1 > maxim2:
    #                         possible_moves[i][2] = 1
    #                     else:
    #                         possible_moves[i][2] = -1
    #
    #     maxim = [0, 0, 0]  # i, j, type
    #     for i in range(0, 6):
    #         if possible_moves[i][1] > maxim[2]:
    #             maxim[0] = i
    #             maxim[1] = possible_moves[i][0]
    #             maxim[2] = possible_moves[i][2]
    #
    #     return maxim[0], maxim[1], maxim[2]
