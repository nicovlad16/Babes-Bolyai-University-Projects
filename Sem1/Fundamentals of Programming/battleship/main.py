from domain.computer import Computer
from domain.table import Table
from domain.valid import Validate
from service.service import Service
from ui.game import Game

table_player = Table(True)
table_computer = Table(False)
computer = Computer(table_computer)
valid = Validate()
service = Service(table_player, table_computer, computer, valid)
game = Game(service)
game.start()
