import re

my_string = 'I am a string'

res = re.search('string', my_string)

print(res)

res = re.search('s....g', my_string)

print(res)

my_string = 'I am a soooog'

res = re.search('s....g', my_string)

print(res)

res = re.search('s....g$', my_string)

print(res)

my_string = 'I am a string!'

res = re.search('s....g$', my_string)

print(res)

res = re.search('^I.*a', my_string)

print(res)

my_string = 'I am a string.'

res = re.search(r's....g\.', my_string)

print(res)

print(res.span())
print(res.start())
print(res.end())
