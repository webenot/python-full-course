def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling function: [{fn.__name__}], args: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function [{fn.__name__}] result: {result}")
        return result

    return wrapper


@log_function_call
def mult(a, b):
    return a * b


print(mult(a=2, b=10), '\n')


@log_function_call
def add(a, b):
    return a + b


print(add(2, 10))
