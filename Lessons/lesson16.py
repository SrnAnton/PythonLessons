class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f"{self.name}, введен {new_floor} этаж")
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")


house = House('ЖК Эльбрус', 30)
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

house.go_to(1)
h1.go_to(5)
h2.go_to(10)
