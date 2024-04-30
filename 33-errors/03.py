try:
    print('1' / 0)
except ZeroDivisionError as e:
    print(type(e))
    # <class 'ZeroDivisionError'>
    print(e)
    # division by zero

print('Continue...')
