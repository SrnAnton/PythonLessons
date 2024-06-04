class Building:
    def __init__(self, number_of_floors, building_type):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return NotImplemented


building1 = Building(4, "жилой дом")
building2 = Building(4, "жилой дом")

print(building1 == building2)

building3 = Building(5, "офисное здание")
building4 = Building(5, "жилой дом")
print(building1 != building3)
print(building1 == building4)
