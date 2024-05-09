with open('test.txt', 'wb') as test_file:
    test_file.write(bytes('First string\n', 'utf-8'))
    test_file.write(bytes('Second string\n', 'utf-8'))
    test_file.write(bytes('Third string\n', 'utf-8'))

with open('test.txt', 'r') as test_file:
    # lines = test_file.readlines()
    # for line in test_file:
    #     print(line)
    print(test_file.readline())
