import json

my_dict = {'a': 1, 'b': 'test', 'c': True, 'd': [1, 2, 3], 'e': 4.5}
my_json = json.dumps(my_dict, indent=2)
print(my_json)
print(type(my_json))
