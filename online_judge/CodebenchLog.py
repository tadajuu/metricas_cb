"""
@auhor: Flávio José Mendes Coelho.
@date: 24/12/2022.
@class: CodebenchLog.
Fornece funcionalidades de recuperação de dados dos arquivos de log do Codebench.
"""
from os import listdir
from online_judge.Semester import Semester


class CodebenchLog:

    def __init__(self):
        self.codebench_log_path: str = self._load_codebench_dataset_path()
        self.semesters: dict = self._load_semesters()

    def _load_codebench_dataset_path(self) -> str:
        path = "../online_judge/"
        name = "codebench_dataset_path.txt"
        codebench_dataset_path = None
        try:
            fr = open(path + name, 'r', encoding="utf-8")
            codebench_dataset_path = fr.read()
            fr.close()
        except (OSError, FileNotFoundError, PermissionError):
            print(f"CodebenchLog._load_codebench_dataset_path(): Erro ao manipular o arquivo '{path + name}'")
        return codebench_dataset_path

    def _load_semesters(self) -> list:
        semester_ids: list = listdir(self.codebench_log_path)
        semesters = {}
        try:
            index = semester_ids.index('.DS_Store')
            del semester_ids[index]
        except ValueError:
            # print("ValueError: That item does not exist")
            pass
        finally:
            semester_ids.sort()
            for semester_id in semester_ids:
                sem = Semester(semester_id, self.codebench_log_path)
                semesters[semester_id] = sem
        return semesters

    @property
    def semesters(self):
        return self._semesters

    @semesters.setter
    def semesters(self, semesters: list):
        self._semesters = semesters

    @property
    def codebench_log_path(self):
        return self._codebench_log_path

    @codebench_log_path.setter
    def codebench_log_path(self, codebench_log_path: list):
        self._codebench_log_path = codebench_log_path




