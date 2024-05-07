def decorator_function(original_fn):
    def wrapper(*args, **kwargs):
        print('Before original function called')
        result = original_fn(*args, **kwargs)
        print('After original function called')
        return result
    return wrapper


@decorator_function
def my_function(a, b):
    print('This is my function')
    return (a, b)


result = my_function(100, 50)
print(result)
