from apartment import Apartment

class Building(Apartment):
    def __init__(self, length, width, rooms, floors, flats_per_floor):
        super().__init__(length, width, rooms)
        self.floors = floors
        self.flats_per_floor = flats_per_floor

    @property
    def area(self):
        return super().area * self.floors * self.flats_per_floor

    def heating_power(self):
        return self.area * 13

    def __str__(self):
        return f"Дом на {self.floors} этажей по {self.flats_per_floor} квартир, {self.area} м²"
    
    def __len__(self):
        return int(self.area)
