my_list = [1, 2, 3]

my_dict = {}

print(my_list and my_dict)
# {}

print(bool(my_list and my_dict))
# False

my_dict2 = {'a': 1, 'b': 2, 'c': 3}
print(bool(my_list and my_dict2))
# True

print(my_list and my_dict2)
# {'a': 1, 'b': 2, 'c': 3}

my_list and print('List is not empty')
# List is not empty

my_list2 = []
my_list2 and print('List is not empty')
#

