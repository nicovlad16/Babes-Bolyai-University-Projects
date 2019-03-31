from domain.student import Student
from domain.discipline import Discipline
from domain.grade import Grade
import random


class InitializeRepositories(object):

    def initialize_student_repo(self):
        elems = []
        #         students = ["ion", "andrei", "ana", "alexandru", "ana maria",\
        #              "andreea", "iuliana", "alexandra", "vlad"]
        for i in range(0, 100):
            student_id = i
            student_name = "student" + str(i)
            student = Student(student_id, student_name)
            elems.append(student)
        return elems


    def initialize_disciplines_repo(self):
        elems = []
        disciplines = ["math", "history", "fp", "info", "geography", \
                       "english", "economics", "asc", "algebra", "trigonometry", \
                       "sport", "logics", "psychology", "finance", "marketing"]
        for i in range(0, len(disciplines)):
            discipline = Discipline(i, disciplines[i])
            elems.append(discipline)
        return elems


    def initiallize_grade_repo(self):
        elems = []
        for i in range(0, 100):
            disc_nr = len(self.initialize_disciplines_repo()) - 1
            grade = Grade(i, random.randint(0, disc_nr), random.randint(1, 10))
            elems.append(grade)
        for i in range(0, 100):
            stud_nr = len(self.initialize_student_repo()) - 1
            grade = Grade(random.randint(0, stud_nr), random.randint(0, disc_nr), random.randint(5, 10))
            if grade not in elems:
                elems.append(grade)
        return elems
