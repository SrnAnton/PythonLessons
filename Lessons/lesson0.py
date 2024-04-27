import math
from decimal import Decimal

print(f'Hi')

a = 23891471923807487.142352314353455
b = 23891471923807487.142352314356734
c = 23891471923843245.142352314334563
d = 23891471923843245.142352314334553

ac = a + c
bd = b + d
print(f'ac == {ac} , bd == {bd}')

more = ac > bd
less = ac < bd
equal = ac == bd
print(f'{a} + {c} > {b} + {d} is {more}')  # false
print(f'but {a} + {c} < {b} + {d} still {less}')  # false
print(f'so {a} + {c} == {b} + {d} is {equal}')  # true

print(f'correct with \'math.isclose\' {math.isclose(ac, bd, rel_tol=1e-30)}')

print(f'if we will use Decimal with string initialization, so')

da = Decimal("23891471923807487.142352314353455")
db = Decimal("23891471923807487.142352314356734")
dc = Decimal("23891471923843245.142352314334563")
dd = Decimal("23891471923843245.142352314334553")

dac = da + dc
dbd = db + dd

decimalDiff = dac - dbd
decimalMore = dac > dbd
decimalLess = dac < dbd
decimalEquals = dac == dbd

print(f'more is {decimalMore}')  # false
print(f'less is {decimalLess}')  # false
print(f'equal is {decimalLess}')  # false

print(f'diff is {decimalDiff}')

array = [da, db, dc, dd]
min_ = min(array)

print(f'minimum is {min_}')

for i in array:
    print(f"diff {i - min_}")
