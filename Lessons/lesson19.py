class Building:
    total = 0

    def __init__(self):
        Building.total += 1

    def __repr__(self):
        return f"Object #{Building.total}"


buildings = [Building() for _ in range(40)]
for building in buildings:
    print(building)

one_other_building = Building()

print(Building.total)
