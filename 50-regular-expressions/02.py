import re

my_string = 'I am a string.'
other_string = 'I am a string!'

my_regex = re.compile(r's....g\.')
print(my_regex)
print(my_regex.search(my_string))

my_regex = re.compile(r'^I.*\.$')
print(my_regex)
print(my_regex.match(my_string))
print(my_regex.match(other_string))

my_string = 'My name is Bogdan. Bogdan is instructor'
my_pattern = re.compile(r'B....n')
print(my_pattern.findall(my_string))

my_string = 'My name is Bogdan. Boooon is instructor'
print(my_pattern.findall(my_string))
