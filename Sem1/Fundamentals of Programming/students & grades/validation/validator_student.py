class StudentValidatorException(Exception):
    pass


class StudentValidator(object):

    def validate(self, student):
        errors = ""
        if student.get_ident() < 0:
            errors += "Invalid id.\n"
        if student.get_name() == "":
            errors += "Invalid name.\n"
        if len(errors) > 0:
            raise StudentValidatorException(errors)
