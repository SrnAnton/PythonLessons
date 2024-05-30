# [1] - first element of array
# [-1] - last element of array . '-' from right to left
array = [1, 2, 3, 4, 5, 6, 7, 8]
print(array)

print("index")
print(array[0])  # 1
print(array[-0])  # 1

print()
print(array[1])  # 2
print(array[-1])  # 8

print()
print(array[3])  # 4
print(array[-3])  # 6

print()
array[1] = 999
print(array[1])  # 999

print("\nappend")
array.append(123)
print(array)

print("\ninsert")
array.insert(3, 888)
print(array)

print("\ndel")
del array[0]
print(array)

print("\npop")
popped_element = array.pop()
print(array)
print(popped_element)

print("\npop from index")
popped_element = array.pop(3)
print(array)
print(popped_element)

print("\nappend")
array.append(7777)
array.append(1)
array.append(7777)
array.append(2)
array.append(7777)
array.append(3)
print(array)

print("\nremove")
array.remove(7777)
print(array)

print("\nsorted")
print(sorted(array))
print(array)

print("\nreverse sorted")
print(sorted(array, reverse=True))
print(array)

print("\nsort")
array.sort()
print(array)

print("\nreverse sort")
array.sort(reverse=True)
print(array)

print("\nreverse")
array.reverse()
print(array)

print("\nlen")
print(len(array))
