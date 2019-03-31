class DisciplineValidatorException(Exception):
    pass


class DisciplineValidator(object):

    def validate(self, discipline):
        errors = ""
        if discipline.get_ident() < 0:
            errors += "Invalid id.\n"
        if discipline.get_name() == "":
            errors += "Invalid name.\n"
        if len(errors) > 0:
            raise DisciplineValidatorException(errors)
