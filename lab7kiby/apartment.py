from room import Room

class Apartment(Room):
    def __init__(self, length, width, rooms):
        super().__init__(length, width)
        self.rooms = rooms

    @property
    def area(self):
        return super().area * self.rooms

    def heating_power(self):
        return self.area * 13

    def __str__(self):
        return f"Апартамент с {self.rooms} комнатами, площадью {self.area} м²"
    
    def __len__(self):
        return int(self.area)
