class GradeValidator(object):

    def validate(self, grade):
        errors = ""
        if grade.get_student_id() < 0:
            errors += "Invalid student id.\n"
        if grade.get_discipline_id() < 0:
            errors += "Invalid discipline id.\n"
        if grade.get_grade() < 0 or grade.get_grade() > 10:
            errors += "Invalid grade.\n"
        if len(errors):
            raise GradeValidatorException(errors)


class GradeValidatorException(Exception):
    pass
