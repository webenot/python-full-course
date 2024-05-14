from array import array
from pathlib import Path

print(dir(array))

my_int_array = array('i', [1, 2, 3])
print(my_int_array)
print(type(my_int_array))

my_int_array.append(15)
print(my_int_array)

# my_int_array.append('abc')
# TypeError: 'str' object cannot be interpreted as an integer

my_int_array.append(1)
my_int_array.append(1)
my_int_array.append(1)
print(my_int_array.count(1))

my_int_array.pop()
print(my_int_array)

print(len(my_int_array))

for x in my_int_array:
    print(x)

print(my_int_array[0])

with open('my_array.bin', 'wb') as f:
    my_int_array.tofile(f)

imported_array = array('i')

with open('my_array.bin', 'rb') as f:
    imported_array.fromfile(f, 3)
    print(imported_array)

imported_array.reverse()
print(imported_array)

Path('my_array.bin').unlink()
