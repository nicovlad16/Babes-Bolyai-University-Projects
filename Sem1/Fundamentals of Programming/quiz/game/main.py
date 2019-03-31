from ctrl.ctrl import Ctrl
from domain.valid import Valid
from repo.repo import Repo
from ui.ui import Console

repo = Repo("questions")
valid = Valid()
ctrl = Ctrl(repo, valid)
console = Console(ctrl)
console.run()
