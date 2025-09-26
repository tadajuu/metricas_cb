import re
from online_judge.File import File

__author__ = 'Flávio José Mendes Coelho'


class ExecutionsFile(File):

    def __init__(self, file_name: str, path: str):
        super().__init__(file_name, path)

    def has_code_passed_all_CTs(self):
        self.load_text()
        PATTERN = '-- GRADE:\n100%'
        passed_all_CTs = bool(re.search(PATTERN, self.text))
        return passed_all_CTs
