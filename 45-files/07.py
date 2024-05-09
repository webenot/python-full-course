test_file = open('test.txt', 'w')
# Opens file for write and in Windows will encode as cp1251
# and with CRLF line separator

print(test_file)
print(type(test_file))

test_file.write('First string\n')
test_file.write('Second string\n')

test_file.close()

test_file = open('test.txt', 'r')

print(test_file.read())

with open('test.txt', 'wb') as test_file:
    test_file.write(bytes('First string\n', 'utf-8'))
    test_file.write(bytes('Second string\n', 'utf-8'))

with open('test.txt') as test_file:
    print(test_file.read())
