class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000
    def horse_powers(self):
        return 100


class Nissan(Vehicle, Car):
    vehicle_type = 'Yes'
    price = 2000000

    def horse_powers(self):
        return 200

a = Nissan()
print(a.vehicle_type)
print(a.price)