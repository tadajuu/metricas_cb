from online_judge.File import File

__author__ = 'Flávio José Mendes Coelho'


class CodeFile(File):

    def __init__(self, file_name: str, path: str, exercise_have_start_code: bool):
        super().__init__(file_name, path)
        self.exercise_have_start_code: bool = exercise_have_start_code

    @property
    def exercise_have_start_code(self):
        return self._exercise_have_start_code

    @exercise_have_start_code.setter
    def exercise_have_start_code(self, exercise_have_start_code: bool):
        self._exercise_have_start_code = exercise_have_start_code

