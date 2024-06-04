class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        print(f"Новое количество этажей: {floors}")
        self.numberOfFloors = floors


house = House()
house.setNewNumberOfFloors(5)
