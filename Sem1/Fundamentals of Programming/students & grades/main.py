from service.discipline_controller import DisciplineController
from repository.repository import Repository
from repository.repository import FileRepository
from repository.repository import BinaryRepository
from validation.validator_student import StudentValidator
from service.student_controller import StudentController
from validation.validate_discipline import DisciplineValidator
from UI.console import Console
from service.grade_controller import GradeController
from validation.validate_grade import GradeValidator
from service.undo_redo_controller import UndoRedoController
from domain.student import Student
from domain.discipline import Discipline
from domain.grade import Grade

if __name__ == "__main__":

    def get_filename_from_line(line):
        if line1:
            line = line.strip()
            elems = line.split(" ")
            filename = elems[2]
        return filename


    try:
        with open("settings.properties", "r") as f:
            line = f.readline()
            if line:
                line = line.strip()
                elems = line.split(" ")
                repository_type = elems[2]
                if repository_type == "inmemory":
                    stud_repo = Repository()
                    disc_repo = Repository()
                    grade_repo = Repository()
                elif repository_type == "textfile":
                    line1 = f.readline()
                    filename = get_filename_from_line(line1)
                    stud_repo = FileRepository(filename, Student.line_to_student, Student.student_to_line)
                    line2 = f.readline()
                    filename = get_filename_from_line(line2)
                    disc_repo = FileRepository(filename, Discipline.line_to_discipline, Discipline.discipline_to_line)
                    line3 = f.readline()
                    filename = get_filename_from_line(line3)
                    grade_repo = FileRepository(filename, Grade.line_to_grade, Grade.grade_to_line)
                elif repository_type == "binaryfile":
                    line1 = f.readline()
                    filename = get_filename_from_line(line1)
                    stud_repo = BinaryRepository(filename)
                    line2 = f.readline()
                    filename = get_filename_from_line(line2)
                    disc_repo = BinaryRepository(filename)
                    line3 = f.readline()
                    filename = get_filename_from_line(line3)
                    grade_repo = BinaryRepository(filename)
    except FileNotFoundError as fnfe:
        print(fnfe)

    undo_redo_ctrl = UndoRedoController()
    stud_valid = StudentValidator()
    stud_ctrl = StudentController(stud_repo, stud_valid, undo_redo_ctrl)
    disc_valid = DisciplineValidator()
    disc_ctrl = DisciplineController(disc_repo, disc_valid, undo_redo_ctrl)
    grade_valid = GradeValidator()
    grade_ctrl = GradeController(grade_repo, grade_valid, stud_repo, disc_repo, undo_redo_ctrl)

    cons = Console(stud_ctrl, disc_ctrl, grade_ctrl, undo_redo_ctrl)
    if repository_type == "inmemory":
        cons.initialize_repositories()
    cons.run()
