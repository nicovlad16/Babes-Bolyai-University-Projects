from ctrl.ctrl import Ctrl
from domain.grid import Grid
from domain.valid import Valid
from repo.repo import Repo
from ui.ui import Console

valid = Valid()
repo = Repo("file")
ctrl = Ctrl(repo, valid)
console = Console(ctrl)
console.run()
