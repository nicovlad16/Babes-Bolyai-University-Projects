from domain.discipline import Discipline
from domain.operations import ReverseAddOp, ReverseUpdOp, ReverseRemOp


class DisciplineController(object):

    def __init__(self, repo, validator, undo_redo_ctrl):
        self.__repo = repo
        self.__validator = validator
        self.__undo_redo_ctrl = undo_redo_ctrl


    def __len__(self):
        return len(self.__repo)


    def __str__(self):
        return "\nThe disciplines are:\n" + str(self.__repo)


    def add_discipline(self, ident, name):
        discipline = Discipline(ident, name)
        self.__validator.validate(discipline)
        self.__repo.add(discipline)
        self.__undo_redo_ctrl.add_op(ReverseAddOp(self.__repo, discipline))


    def find_discipline_by_id(self, ident):
        return self.__repo.find(Discipline(ident, ""))


    def update_discipline(self, ident, name):
        existing_discipline = self.__repo[ident]
        new_discipline = Discipline(ident, name)
        self.__validator.validate(new_discipline)
        self.__repo.update(new_discipline)
        self.__undo_redo_ctrl.add_op(ReverseUpdOp(self.__repo, new_discipline, existing_discipline))


    def remove_discipline(self, ident):
        discipline = self.__repo[ident]
        self.__repo.remove(discipline)
        self.__undo_redo_ctrl.add_op(ReverseRemOp(self.__repo, discipline))


    def get_all_disciplines(self):
        return self.__repo.get_all()


    def find_discipline_by_name(self, name):
        elements = []
        for i in self.get_all_disciplines():
            if name.lower() in i.get_name().lower():
                elements.append(i)
        return elements
