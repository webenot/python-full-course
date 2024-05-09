from pathlib import Path

with open('test.txt') as f:
    print(f.read())

with open('test.txt') as f:
    print(f.readlines())

# Rewrites existed file
with open('new.txt', 'w') as f:
    f.write('First line in a new file\n')

with open('new.txt') as f:
    print(f.read())

with open('new.txt', 'a') as f:
    f.write('Second line in a new file\n')

with open('new.txt') as f:
    print(f.read())

new_path = Path('new.txt')
print(new_path.exists())

if new_path.exists():
    new_path.unlink()

print(new_path.exists())
