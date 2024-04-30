try:
    print(10 / 0)
except Exception as e:
    print(isinstance(e, ZeroDivisionError))
    print(e)
else:
    print('There was no error')
finally:
    print('Continue...')
