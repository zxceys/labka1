from package.room import Room

class Apartment(Room):
    def __init__(self, dlina, shirina, komnaty):
        super().__init__(dlina, shirina)
        self.komnaty = komnaty
    
    def calculate_area(self):
        return super().calculate_area() * self.komnaty
    
    def calculate_heating_power(self):
        return super().calculate_heating_power() * self.komnaty





