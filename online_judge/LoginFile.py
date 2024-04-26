
__author__ = 'Flávio José Mendes Coelho'


class LoginFile:

    def __init__(self, datetime_str: str, file_name: str, file_path: str):
        # @todo: transformar date_time: str em objeto datetime
        self.date_time: str = datetime_str
        self.name: str = file_name
        self.path: str = file_path
        self._status = ""
        self.set_status_to_undefined()

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time: str):
        self._date_time = date_time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, path: str):
        self._path = path

    @property
    def status(self) -> str:
        return self._status

    # Uso privado
    @status.setter
    def status(self, status: str):
        self._status = status

    def set_status_to_login(self):
        self._status = "login"

    def set_status_to_logout(self):
        self._status = "logout"

    def set_status_to_undefined(self):
        self._status = "undefined"

