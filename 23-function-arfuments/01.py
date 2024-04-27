def merge_lists_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))


print(merge_lists_to_dict(list_one=['a', 'b', 'c', 'd', 'e'], list_two=[1, 2, 3, 4, 5]))
print(merge_lists_to_dict(['a', 'b', 'c', 'd', 'e'], list_two=[1, 2, 3, 4, 5]))
