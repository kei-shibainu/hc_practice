from abc import ABC, abstractmethod

class NameService(ABC):
    @abstractmethod
    def name(self, new_name):
        pass

    @abstractmethod
    def name(self):
        pass
