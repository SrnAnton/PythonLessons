# strings
messageTypeOne = 'message with "" '
messageTypeTwo = "message with '' "
messageTypeThree = 'message with \'\' '
messageTypeFour = "message with \"\" "

name_1 = 1  # this is work
# 1_name = 1 # doesn't work

name = "ada lovelace"
abc = "Abc"
print(name.title())  # Ada Lovelace
print(abc.upper())  # ABC
print(abc.lower())  # abc

# Concantenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + last_name  # ava lovelace

# \t - tabulation
# \n\t - end line

left_white_space = "  python"
right_white_space = "python  "
both_white_space = "  python  "

print(left_white_space.lstrip())  # "python"
print(right_white_space.rstrip())  # "python"
print(both_white_space.strip())  # "python"

user_name = input()

print(f"Hi, {user_name}!")

# numbers
result = (1 - 2 + 3) * 4 / 5
pow_2_2 = 2 ** 2
pow_10_10 = 10 ** 10

# float
float_ = 0.1
age = 18
message = "Happy " + str(age) + "rd Birthday!"

print(3 / 2)  # 1
print(3.0 / 2)  # 1.5
