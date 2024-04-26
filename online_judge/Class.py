from os import listdir
from online_judge.User import User

__author__ = 'Flávio José Mendes Coelho'


class Class:

    def __init__(self, class_id: str, semester_path: str):
        self.class_id = class_id
        self.class_path: str = semester_path + "/" + self.class_id + "/users"
        self.class_path_assessments: str = semester_path + "/" + self.class_id + "/assessments"
        self.users: dict = self._load_users()

    def _load_users(self) -> dict:
        user_ids: list = listdir(self.class_path)
        users = {}
        try:
            index = user_ids.index('.DS_Store')
            del user_ids[index]
        except ValueError:
            # print("ValueError: That item does not exist")
            pass
        finally:
            user_ids.sort()
            for user_id in user_ids:
                # if user_id == "7568":
                user = User(user_id, self.class_path)
                users[user_id] = user
        return users

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, class_id: str):
        self._class_id = class_id

    @property
    def class_path(self):
        return self._class_path

    @class_path.setter
    def class_path(self, class_path: str):
        self._class_path = class_path

    @property
    def class_path_assessments(self):
        return self._class_path_assessments

    @class_path_assessments.setter
    def class_path_assessments(self, class_path_assessments: str):
        self._class_path_assessments = class_path_assessments

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users: list):
        self._users = users

