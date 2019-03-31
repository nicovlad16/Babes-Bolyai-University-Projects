import re

from domain.table import ValidationException


class Validate():
    """
    a function that checks if a given string has valid positions to form a ship
    if not, raises an exception
    """


    def validate(self, ship):
        errors = ""
        if len(ship) != 6:
            errors += "invalid lenght of the ship. "
        else:
            match_obj = re.match("[A-F][0-5][A-F][0-5][A-F][0-5]", ship)
            if match_obj == None:
                errors += "Invalid positions. "
            else:
                if (ship[0] == ship[2] and ship[2] == ship[4] and int(ship[1]) == int(ship[3]) - 1 and int(
                        ship[3]) == int(ship[5]) - 1) and int(ship[3]) <= 5 \
                        or (ship[1] == ship[3] and ship[3] == ship[5] and (
                        (ship[0] == 'A' and ship[2] == 'B' and ship[4] == 'C') \
                        or (ship[0] == 'B' and ship[2] == 'C' and ship[4] == 'D') or (
                                ship[0] == 'C' and ship[2] == 'D' and ship[4] == 'E') \
                        or (ship[0] == 'D' and ship[2] == 'E' and ship[4] == 'F'))):
                    errors += ""
                else:
                    errors += "Invalid positions. "
        if errors:
            raise ValidationException(errors)
