magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print()

for i in list(range(0, 10, 3)):
    print(i)
print()

for i in range(5):
    print(i)
print()

for i in range(1, 5):
    print(i)
print()

squares = [value ** 2 for value in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)
print()

# slices -  срезы

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # ['charles', 'martina', 'michael']
print(players[2:4])  # ['michael', 'florence']
print(players[-1])  # eli
print(players[-2])  # florence
print(players[::2])  # ['charles', 'michael', 'eli']
print(players[2::2])  # ['michael', 'eli']
print(players[::-1])  # ['eli', 'florence', 'michael', 'martina', 'charles']
print(players[:3])  # ['charles', 'martina', 'michael']
print(players[2:])  # ['michael', 'florence', 'eli']
print()

copy_of_players = players[:]
print(copy_of_players)
print()

dimensions = (200, 50)
immutable_var = 0, 'Anton', 1.5, [1, 2, 3], 3 / 12  # Кортежи неизменяемы, но элементы кортежа нет
print(immutable_var)

# immutable_var[0] = 123 # кортежи являются неизменяемыми типами данных
print(immutable_var[3][0])
immutable_var[3][0] = 123  # НО!
print(immutable_var[3][0])
