try:
    print(10 / 1)
except ZeroDivisionError as e:
    print(e)
    # division by zero
except TypeError as e:
    print(e)
    # unsupported operand type(s) for /: 'str' and 'int'
else:
    print('There was no error')

print('Continue...')
