# classes of transports
class PassengerCar():
    def __init__(self):
        self.maneuverability = 3
        self.consumption = 10
        self.id = 1
        self.passability = self.get_passability()

    def gasoline_consumption(self, road_complexity):
        return self.passability * road_complexity
    
    def __str__(self):
        return (
        f'Type of transport is the {self.get_class()}, '
        f'maneuverability = {self.maneuverability}, '
        f'consumption = {self.consumption}, '
        f'id = {self.id}'
    )
    
    def get_passability(self):
        return self.consumption/100/self.maneuverability
    
    def __add__(self, obj): 
        if isinstance(obj, int) and obj > 0:
            self.maneuverability += obj
            self.consumption += obj
        return self
    
    def get_class(self):
        return self.__class__.__name__

class Bus(PassengerCar):
    def __init__(self):
        super().__init__()
        self.maneuverability = 1
        self.consumption = 15
        self.id = 2
        self.passability = self.get_passability()

class Truck(PassengerCar):
    def __init__(self):
        super().__init__()
        self.maneuverability = 2
        self.consumption = 12
        self.id = 3
        self.passability = self.get_passability()

class SUV(PassengerCar):
    def __init__(self):
        super().__init__()
        self.maneuverability = 6
        self.consumption = 18
        self.id = 4
        self.passability = self.get_passability()