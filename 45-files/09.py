from pathlib import Path

files_dir = Path('files')
files_dir.mkdir(exist_ok=True)

first_file = files_dir / 'first.txt'
second_file = files_dir / 'second.txt'

with open(first_file, 'w') as f:
    f.write('First line\n')
    f.write('Second line\n')

with open(second_file, 'w') as f:
    f.write('First line\n')
    f.write('Second line\n')
    f.write('Third line\n')

with open(first_file, 'r') as f:
    print(f.read())

with open(second_file, 'r') as f:
    for line in f:
        print(line.strip().upper())
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     print(line.strip().upper())

first_file.unlink()
second_file.unlink()
files_dir.rmdir()
