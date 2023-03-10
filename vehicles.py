class Vehicle:
    def __init__(self, make, model, Milage, price):
        self.make = make
        self.model = model
        self.Milage = Milage
        self.price = price
    def __str__(self):
        return f'Make : {self.make}  Model : {self.model} Milage {self.Milage} Pris :{self.price}'
class Car(Vehicle):
    def __init__(self,make, model, Milage, price,doors):
        super().__init__(make, model, Milage, price)
        self.doors = doors
    def __str__(self):
        return f'Make : {self.make}  Model : {self.model} Milage {self.Milage} Price :{self.price} doors:{self.doors}'
class  Truck(Vehicle):
    def __init__(self,make, model, Milage, price, drivetype):
        super().__init__(make, model, Milage, price)
        self.drivetype = drivetype

    def __str__(self):
        return f'Make : {self.make}  Model : {self.model} Milage : {self.Milage} Price :{self.price} drivetype:{self.drivetype}'
class SUV(Vehicle):
    def __init__(self,make, model, Milage, price, numberOfPassengers):
        super().__init__(make, model, Milage, price)  
        self.numberOfPassengers = numberOfPassengers
    def __str__(self):
        return f'Make : {self.make}  Model : {self.model} Milage : {self.Milage} Price :{self.price} numberOfPassengers:{self.numberOfPassengers}'