from ctrl.game import Game
from domain.valid import Valid
from repo.repo import Repo
from ui.ui import Console

repo = Repo("game")
valid = Valid()
game = Game(valid, repo)
console = Console(game)
console.run()
