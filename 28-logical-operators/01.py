my_list = [1, 2, 3]

# print(not not my_list)

other_list = ['a', 'b']

print(my_list or other_list)
# [1, 2, 3]

print(len(my_list) > 0 or other_list)
# True

print(len(my_list) < 0 or other_list)
# ['a', 'b']
