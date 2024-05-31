import math
from itertools import chain


def find_divisors(n):
    divisors = []

    for i in range(1, int(math.sqrt(n)) + 1):

        if n % i == 0:
            divisors.append(i)

            if i != n // i:
                divisors.append(n // i)

    return divisors


def find_combinations(target):
    combinations = []

    for i in range(1, int(target / 2) + target % 2):
        j = target - i

        if i + j == target:
            combinations.append([i, j])

    return combinations


def find_password(target):
    divisors = find_divisors(target)
    divisors = sorted(divisors)

    password = []
    for i in divisors:
        for n in find_combinations(i):
            password = list(chain(password, n))

    return "".join(map(str, password))


test = {
    4: 13,
    5: 1423,
    6: 121524,
    7: 162534,
    8: 13172635,
    9: 1218273645,
    10: 141923283746,
    11: 11029384756,
    12: 12131511124210394857,
    13: 112211310495867,
    14: 1611325212343114105968,
    15: 1214114232133124115106978,
    16: 1317115262143531341251161079,
    17: 11621531441351261171089,
    18: 12151811724272163631545414513612711810,
    19: 118217316415514613712811910,
    20: 13141911923282183731746416515614713812911
}

for key, value in test.items():
    result = find_password(key)
    print(f"{key} is {result == str(value)} {result} : {value}")
