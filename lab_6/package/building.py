from package.apartment import Apartment

class Building(Apartment):
    def __init__(self, dlina, shirina, etazhi, komnaty_na_etazh):
        super().__init__(dlina, shirina, komnaty_na_etazh)
        self.etazhi = etazhi
    
    def calculate_area(self):
        return super().calculate_area() * self.etazhi
    
    def calculate_heating_power(self):
        return super().calculate_heating_power() * self.etazhi





