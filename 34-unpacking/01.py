my_list = [1, 2, 3]

first, second, third = my_list

print(first)
print(second)
print(third)

my_fruits = ['apple', 'banana', 'cherry']

my_apple, *other_fruits = my_fruits
print(my_apple)
print(other_fruits)
print(type(other_fruits))
