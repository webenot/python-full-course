my_list = [0, 'abc', 1.5, {'foo': 'bar'}, True]

del my_list[2]

print(len(my_list))

my_list.reverse()

my_second_list = [1, 2]

my_list.extend(my_second_list)

print(my_list)
