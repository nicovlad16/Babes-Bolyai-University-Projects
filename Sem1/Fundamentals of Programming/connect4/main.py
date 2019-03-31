'''
Created on Dec 21, 2017

@author: nvlad
'''
from domain.table import Table
from service.game import Game
from ui.console import Console

if __name__ == '__main__':
    table = Table()
    game = Game(table)
    cons = Console(table, game)
    cons.run()
