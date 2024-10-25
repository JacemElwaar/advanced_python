class Vehicle:
    def __init__(self, distance_traveled=0, unit='miles'):
        print(f"this is the Vehicle and the distance traveled is {distance_traveled}")
        self.distance_traveled = distance_traveled
        self.unit = unit
    
    def description(self):
        return f"Vehicle has traveled {self.distance_traveled} {self.unit}"
    


class Car(Vehicle):
    default_tire = 'tire' 


    def __init__(self,engine, distance_traveled=0, unit='miles', tires=[]):
        print(f"this is the Car and the distance traveled is {distance_traveled}")
        super().__init__(distance_traveled=distance_traveled, unit=unit)
        if not tires: 
            tires = [self.default_tire, self.default_tire]
        
        self.tires = tires
        self.engine = engine 

    def drive(self,  distance): 
        self.distance_traveled += distance 

    

class Boat(Vehicle):
    def __init__(self, boat_type= 'sail',  distance_traveled=0, unit='miles'):
        print(f"this is the Boat and the distance traveled is {distance_traveled}")
        super().__init__(distance_traveled=distance_traveled, unit=unit)
        self.boat_type = boat_type

    def sail(self, distance):
        self.distance_traveled += distance  

    def description(self):
        initial = super().description()
        return f"{initial} on a {self.boat_type} boat" 
    

class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires= [], distance_traveled=0 , unit='miles'):
        super().__init__(engine=engine, distance_traveled=distance_traveled, unit=unit, tires=tires) 
        self.boat_type = 'motor'
    
    def travel(self, land_distance, water_distance):
        self.drive(land_distance)
        self.sail(water_distance)





# how the issue have been fixed 