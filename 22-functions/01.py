def merge_lists_to_dict(list1, list2):
    return dict(zip(list1, list2))


print(merge_lists_to_dict(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5]))
