from abc import ABC, abstractmethod

class Space(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @abstractmethod
    def heating_power(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} площадью {self.area} м²"

    def __repr__(self):
        return self.__str__()
