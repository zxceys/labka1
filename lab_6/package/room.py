class Room:
    def __init__(self, dlina, shirina):
        self.dlina = dlina
        self.shirina = shirina
    
    def calculate_area(self):
        return self.dlina * self.shirina
    
    def calculate_heating_power(self):
        return self.calculate_area() * 100



