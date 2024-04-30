try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)
    # division by zero
except TypeError as e:
    print(e)
    # unsupported operand type(s) for /: 'str' and 'int'
else:
    print('There was no error')
finally:
    print('Continue...')
