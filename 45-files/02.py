from pathlib import Path

file_path = Path('test.txt')
print([m for m in dir(file_path) if not m.startswith('_')])

print(Path('test.txt').exists())
# True
print(Path('test1.txt').exists())
# False

print(Path('test.txt').is_file())
# True
print(Path('test.txt').is_dir())
# False

print()

for f in Path('.').iterdir():
    print(f)
