def filter_list(list_to_filter, allowed_type):
    def check_element_type(element):
        return type(element) is allowed_type
    return list(filter(check_element_type, list_to_filter))
    # return list(filter(lambda element: type(element) is allowed_type,
    #                    list_to_filter))


print(filter_list(list_to_filter=['a', True, 3], allowed_type=int))
