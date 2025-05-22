from base import Space

class Room(Space):
    def __init__(self, length, width):
        super().__init__(length, width)

    def heating_power(self):
        return self.area * 13

    def __eq__(self, other):
        return self.area == other.area

    def __len__(self):
        return int(self.area)
