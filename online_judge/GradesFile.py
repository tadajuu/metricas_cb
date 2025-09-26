import re
from online_judge.File import File

__author__ = 'Flávio José Mendes Coelho'


class GradesFile(File):

    def __init__(self, file_name: str, path: str):
        super().__init__(file_name, path)


    @staticmethod
    # def extract_gradesfile_id(file_id: str) -> str:
    def extract_id(file_id: str) -> str:
        # O executionsfile_id tem a forma NNNN_MMMM.extensão, onde N e M são números.
        # O procedimento abaixo extrai somente NNNN que será o gradesfile_id.
        return re.sub("_[a-z0-9\.]*", "", file_id)


