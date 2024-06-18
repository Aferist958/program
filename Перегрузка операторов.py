class Building:
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = ''
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

a = Building()
b = Building()
print(a == b)

