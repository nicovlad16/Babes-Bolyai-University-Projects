class Valid(object):
    def validate(self, question):
        errors = ""
        if question.get_id() < 0:
            errors += "invalid id. "
        if question.get_q() == "":
            errors += "invalid question. "
        if question.get_a1() == "":
            errors += "invalid answer1. "
        if question.get_a2() == "":
            errors += "invalid answer2. "
        if question.get_a3() == "":
            errors += "invalid answer3. "
        ok = False
        if question.get_a1() == question.get_right():
            ok = True
        if question.get_a2() == question.get_right():
            ok = True
        if question.get_a3() == question.get_right():
            ok = True
        if question.get_right() == "" or ok == False:
            errors += "invalid right answer. "
        if question.get_diff() == "":
            errors += "invalid difficulty. "
        if errors:
            raise ValidException(errors)


    def validate_create_quiz(self, diff, no, file):
        errors = ""
        if diff not in ["easy", "medium", "hard"]:
            errors += "invalid difficulty\n"
        try:
            no = int(no)
        except:
            errors += "invalid number of questions\n"
        if file == "":
            errors += "invalid filename\n"
        if errors:
            raise ValidException(errors)


    def validate_question_from_ui(self, params):
        question = ""
        for i in range(len(params)):
            if i >= 1 and i <= len(params) - 1:
                question += " "
            question += params[i]
        elems = question.split(";")
        if len(elems) != 7:
            raise ValidException("invalid question format")
        return elems


class ValidException(Exception):
    pass
