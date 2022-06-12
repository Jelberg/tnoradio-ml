from abc import ABC, abstractclassmethod, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute():
        pass


