from abc import abstractmethod


class Operation:

    @abstractmethod
    def execute(self):
        pass


    @abstractmethod
    def execute_oppsosite(self):
        pass


class ReverseAddOp(Operation):

    def __init__(self, repo, elem):
        self.__repo = repo
        self.__elem = elem


    @abstractmethod
    def execute(self):
        Operation.execute(self)
        self.__repo.remove(self.__elem)


    @abstractmethod
    def execute_oppsosite(self):
        Operation.execute_oppsosite(self)
        self.__repo.add(self.__elem)


class ReverseRemOp(Operation):

    def __init__(self, repo, elem):
        self.__repo = repo
        self.__elem = elem


    @abstractmethod
    def execute(self):
        Operation.execute(self)
        self.__repo.add(self.__elem)


    @abstractmethod
    def execute_oppsosite(self):
        Operation.execute_oppsosite(self)
        self.__repo.remove(self.__elem)


class ReverseUpdOp(Operation):

    def __init__(self, repo, new_elem, existing_elem):
        self.__repo = repo
        self.__new_elem = new_elem
        self.__existing_elem = existing_elem


    @abstractmethod
    def execute(self):
        Operation.execute(self)
        self.__repo.update(self.__existing_elem)


    @abstractmethod
    def execute_oppsosite(self):
        Operation.execute_oppsosite(self)
        self.__repo.update(self.__new_elem)


#         


class ComplexReverseRemOp(Operation):

    def __init__(self, repo, elems, undo_redo_ctrl):
        self.__undo_redo_ctrl = undo_redo_ctrl
        self.__repo = repo
        self.__elems = elems


    @abstractmethod
    def execute(self):
        Operation.execute(self)
        for i in self.__elems:
            self.__undo_redo_ctrl.add_op(ReverseRemOp(self.__repo, i))
        for i in range(0, len(self.__elems)):
            self.__undo_redo_ctrl.undo()
        self.__undo_redo_ctrl.undo()


    @abstractmethod
    def execute_oppsosite(self):
        Operation.execute_oppsosite(self)
        #         for i in self.__elems:
        #             self.__undo_redo_ctrl.add_op(ReverseAddOp(self.__repo, i))
        #         for i in range(0, len(self.__elems)):
        #             self.__undo_redo_ctrl.undo()
        #         self.__undo_redo_ctrl.redo()
        Operation.execute_oppsosite(self)
        i = 0
        while i < len(self.__elems):
            self.__undo_redo_ctrl.redo()
            i += 1
        self.__undo_redo_ctrl.redo()
