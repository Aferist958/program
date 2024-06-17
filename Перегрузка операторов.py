class Building:
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = 0
    def __eq__(self):
        self.numberOfFloors == self.buildingType

a = Building()
print(a.numberOfFloors == a.buildingType)

