my_dict = {
    'a': 'abc',
    'b': 'bcd',
    'c': 'cde',
}

new_dict = {k: v.upper() for k, v in my_dict.items()}

print(my_dict)
print(new_dict)
