from abc import abstractmethod
from pokemon.name_service import NameService

class Pokemon(NameService):
    def __init__(self, name, type1, type2, hp):
        self._name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self._name = new_name

    @abstractmethod
    def attack(self):
        pass