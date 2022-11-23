class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def Pri(self):
        print('Vehicle name: ', self.name)
        print('Max_speed: ', self.max_speed)
        print('Mileage: ', self.mileage)

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity):
        super().__init__(name, max_speed, mileage)
        self.seating_capacity = seating_capacity
    def Bpri(self):
        print('Vehicle name: ', self.name)
        print('Max_speed: ', self.max_speed)
        print('Mileage: ', self.mileage)
        print('seating_capacity: ', self.seating_capacity)


A = Vehicle('Tayota Windom', 180, 300000)
A.Pri()
print('---------------------')
B = Bus(Gaz 124', 120, 20000, 50)
B.Bpri()
