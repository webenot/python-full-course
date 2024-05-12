import re
import string


def check_password(password):
    if type(password) is not str:
        return (False, 'Password must be a string')

    spaces_pattern = re.compile(r'\s+')
    if re.search(spaces_pattern, password):
        return (False, 'Password must not contain spaces')

    length_pattern = re.compile(r'\S{8,}')
    if not re.fullmatch(length_pattern, password):
        return (False, 'Password must contain at least 8 characters')

    lowercase_pattern = re.compile(r'[a-z]+')
    if not re.search(lowercase_pattern, password):
        return (False, 'Password must contain at least one lowercase letter')

    uppercase_pattern = re.compile(r'[A-Z]+')
    if not re.search(uppercase_pattern, password):
        return (False, 'Password must contain at least one uppercase letter')

    number_pattern = re.compile(r'[0-9]+')
    if not re.search(number_pattern, password):
        return (False, 'Password must contain at least one number')

    special_characters_pattern = re.compile(r'[' + string.punctuation + ']+')
    if not re.search(special_characters_pattern, password):
        return (False, 'Password must contain at least one special character')

    return (True, 'Password is valid')


print(check_password(123))
print(check_password('1234  567aB$  88877'))
print(check_password('123'))
print(check_password('12345678'))
print(check_password('zxcvbnma'))
print(check_password('zxcvbFGH'))
print(check_password('1234567aB'))
print(check_password('1234567aB$'))

while True:
    user_pass = input('Enter your password: ')
    result = check_password(user_pass)
    print(result[1])
    if result[0]:
        break
