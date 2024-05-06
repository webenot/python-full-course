from sys import getsizeof

squares_gen = (num * num for num in range(10000))

print(getsizeof(squares_gen))
# 200

print(type(squares_gen))
# <class 'generator'>

print(squares_gen)

squares_list = [num * num for num in range(10000)]

print(getsizeof(squares_list))
# 85176

print(type(squares_list))
# <class 'list'>
