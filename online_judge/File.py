import re
import os.path


__author__ = 'Flávio José Mendes Coelho'


class File:

    def __init__(self, file_name: str, path: str):
        self.name: str = file_name
        self.path: str = path
        self.id: str = self.extract_id(file_name)
        self.is_consistent: bool = self._update_consistency()
        self.text: str = ""
        # self.load_text()

    @staticmethod
    def extract_id(file_name: str) -> str:
        # Elimina a extensão do nome do arquivo
        return re.sub("\.[a-z]*", "", file_name)

    def load_text(self) -> str:
        try:
            if self.is_consistent:
                fr = open(self._path + self.name, 'r',encoding="utf-8")
                self.text = fr.read()
                fr.close()
        except (OSError, FileNotFoundError, PermissionError):
            print(f"File.load_text(): Erro ao manipular o arquivo '{self._path + self.name}'")

    def _update_consistency(self) -> bool:
        exists_and_noempty = False
        try:
            file_size = os.path.getsize(self.path + self.name)
            exists_and_noempty = file_size != 0
        except OSError:
            # print(f"File._update_consistency(): Arquivo '{self.path + self.name}' não existe ou está inacessível")
            pass
        return exists_and_noempty

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, file_id: str):
        self._id = file_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path: str):
        self._path = path

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

    @property
    def is_consistent(self):
        return self._is_consistent

    @is_consistent.setter
    def is_consistent(self, consistency: bool):
        self._is_consistent = consistency

