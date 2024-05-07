def validate_numeric_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 'All arguments must be int or float!')
        result = fn(*args, **kwargs)
        return result
    return wrapper


@validate_numeric_args
def sum_numbers(a, b):
    return a + b


try:
    print(sum_numbers(1, 2))
    print(sum_numbers(10.5, 2.3))
    print(sum_numbers([1, 2, 4], 2.3))
    print(sum_numbers(a=10.5, b='2.3'))
except ValueError as e:
    print(e)
