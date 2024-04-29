def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting('Good Morning')

print(morning_greeting('Bob'))
# Good Morning, Bob!

evening_greeting = greeting('Good Evening')

print(evening_greeting('Bob'))
# Good Evening, Bob!
