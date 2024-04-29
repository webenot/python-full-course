button = {
    'width': 200,
    'text': 'Buy',
}

red_button = {
    **button,
    'color': 'red',
}

print(red_button)
# {'width': 200, 'text': 'Buy', 'color': 'red'}

print(button)
# {'width': 200, 'text': 'Buy'}
