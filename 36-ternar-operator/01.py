my_img = ('1920', '1080')

info = (f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else
        "Incorrect image formatting")

print(info)

my_str = 'Some random string'

print('String is short' if len(my_str) < 10 else 'String is too long')
