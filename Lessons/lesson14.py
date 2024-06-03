import modules.fake_math as fm
import modules.true_math as tm

divide_fake = fm.divide
divide_true = tm.divide

print(divide_fake(10, 0))
print(divide_true(10, 0))
