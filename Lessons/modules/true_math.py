import math


def divide(first, second):
    if second == 0:
        return math.inf  # Бесконечность
    else:
        return first / second
