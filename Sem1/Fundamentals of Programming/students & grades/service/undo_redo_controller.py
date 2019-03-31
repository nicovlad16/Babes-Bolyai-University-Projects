class UndoRedoException(Exception):
    pass


class UndoRedoController(object):

    def __init__(self):
        self.__undo_list = []
        self.__redo_list = []


    def add_op(self, operation):
        self.__redo_list.clear()
        self.__undo_list.append(operation)


    def undo(self):
        if self.__undo_list:
            last = self.__undo_list[-1]
            self.__undo_list.pop()
            last.execute()
            self.__redo_list.append(last)
        else:
            raise UndoRedoException("Nothing to undo.")


    def redo(self):
        if self.__redo_list:
            last = self.__redo_list[-1]
            self.__redo_list.pop()
            last.execute_oppsosite()
            self.__undo_list.append(last)
        else:
            raise UndoRedoException("Nothing to redo.")
