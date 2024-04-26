from os import listdir
from online_judge.Class import Class

__author__ = 'Flávio José Mendes Coelho'


class Semester:

    def __init__(self, semester_id: str, codebench_log_path: str):
        self.semester_id: str = semester_id
        #self.semester_path: str = codebench_log_path + '/' + self.semester_id
        self.semester_path: str = codebench_log_path + '\\' + self.semester_id
        self.classes: dict = self._load_classes()

    def _load_classes(self) -> dict:
        class_ids: list = listdir(self.semester_path)
        classes = {}
        try:
            index = class_ids.index('.DS_Store')
            del class_ids[index]
        except ValueError:
            # print("ValueError: That item does not exist")
            pass
        finally:
            class_ids.sort()
            for class_id in class_ids:
                cls = Class(class_id, self.semester_path)
                classes[class_id] = cls
        return classes

    @property
    def semester_id(self):
        return self._semester_id

    @semester_id.setter
    def semester_id(self, semester_id: str):
        self._semester_id = semester_id

    @property
    def semester_path(self):
        return self._semester_path

    @semester_path.setter
    def semester_path(self, semester_path: str):
        self._semester_path = semester_path

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, classes: list):
        self._classes = classes

