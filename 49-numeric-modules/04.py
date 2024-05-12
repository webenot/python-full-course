def calc_factorial(n):
    if type(n) is not int:
        raise TypeError('Param n must be an integer')
    if n <= 0:
        raise ValueError('Param n must be more than or equal to zero')
    if n == 0 or n == 1:
        return 1
    return n * calc_factorial(n-1)


print(calc_factorial(5))
