def dict_to_list(dictionary):
    my_list = []
    for key, value in dictionary.items():
        my_list.append((key, value * 2 if (type(value) is int) else value))
    return my_list


def filter_list(list_to_filter, allowed_type):
    filtered_list = []
    for element in list_to_filter:
        if type(element) is allowed_type:
            filtered_list.append(element)
        # # Not recommend because bool is subclass of int
        # if isinstance(element, allowed_type):
        #     filtered_list.append(element)
    return filtered_list


print(dict_to_list({'a': 1, 'b': 2, 'c': 3}))
print(filter_list(list_to_filter=['a', True, 3], allowed_type=int))
print(isinstance(True, int))
# True
print(isinstance(True, bool))
# True
print(isinstance(True, object))
# True
