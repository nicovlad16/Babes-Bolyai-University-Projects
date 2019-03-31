import re

from domain.table import ValidException


class Valid():
    def validate_move(self, x, y, type):
        errors = ""
        match = re.match("[0-5]", x)
        if match == None:
            errors += "Invalid x. "
        match = re.match("[0-5]", y)
        if match == None:
            errors += "Invalid y. "
        match = re.match("[x,o]", type)
        if match == None:
            errors += "Invalid type. "
        if errors:
            raise ValidException(errors)
