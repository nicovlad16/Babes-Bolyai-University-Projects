'''
Created on Jan 4, 2018

@author: nvlad
'''
from domain.table import Table
from ui.console import Console

if __name__ == '__main__':
    table = Table()
    cons = Console(table)
    cons.run()
