def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be zero")
    return a / b


try:
    print(divide_nums(2, 0))
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print('There was no error')
finally:
    print('Continue...')
