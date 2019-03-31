from service.ctrl import Controller
from repo.repository import Repository
from UI.ui import Console

repo = Repository("empty_graph", "modified")
ctrl = Controller(repo)
console = Console(ctrl)
console.run()
