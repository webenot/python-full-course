import sys

print(sys.argv)
# in terminal: python .\02.py test
# ['.\\02.py', 'test']

if len(sys.argv) < 3:
    raise IOError("You must provide username and password")

filename, username, password = sys.argv
print(username, password)
