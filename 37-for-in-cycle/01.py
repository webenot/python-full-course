my_list = [1, 'abc', 3.14]

for element in my_list:
    print(type(element))
    print(element)

my_tuple = (1, 'abc', 3.14)

for element in my_tuple:
    print(type(element))
    print(element)

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(type(key))
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)
