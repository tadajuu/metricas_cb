from abc import ABCMeta, abstractmethod
from online_judge.User import User
from multipledispatch import dispatch

__author__ = 'Flávio José Mendes Coelho'


class Metric(object, metaclass=ABCMeta):

    def __init__(self, user: User):
        pass

    @abstractmethod
    def calculate(self):
        pass
