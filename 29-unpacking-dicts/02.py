button_default = {
    'text': 'Ok',
    'color': 'green',
    'width': 0,
    'height': 0,
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300,
}

button = {
    **button_default,
    **button_style,
}

print(button)
# {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}

# Since version 3.9.0
button2 = button_default | button_style

print(button)
# {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}

print(button_default)
# {'text': 'Ok', 'color': 'green', 'width': 0, 'height': 0}
print(button_style)
# {'color': 'yellow', 'width': 200, 'height': 300}
