my_dict = {
    'a': True,
    'b': 10,
}

del my_dict['a']

my_dict.__delitem__('b')

print(my_dict)
# {}

print(my_dict.__delitem__)
# <method-wrapper '__delitem__' of dict object at 0x0000020D007CF600>
