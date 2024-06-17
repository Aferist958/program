class Building:
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = ''
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors

a = Building()
b = Building()
print(a.numberOfFloors == b.numberOfFloors)
print(a.buildingType == b.buildingType)
