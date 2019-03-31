from domain.table import ValidationException


class Validator():

    @staticmethod
    def validate(x, y):
        errors = ""
        p = False
        moves = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in moves:
            if x.lower() == i:
                p = True
        if not p:
            errors += "Invalid position. It should be A-H.\n"
        if y < 0 or y > 7:
            errors += "Invalid position. It should be 0-7.\n"
        if errors:
            raise ValidationException(errors)
