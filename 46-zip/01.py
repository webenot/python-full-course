from zipfile import ZipFile
from pathlib import Path

files_dir = Path('my-files')
files_dir.mkdir(exist_ok=True)

first_file = files_dir / 'first.txt'

with open(first_file, 'w') as f:
    f.write('This is first file.')

second_file = files_dir / 'second.txt'

with open(second_file, 'w') as f:
    f.write('This is second file.')

with ZipFile('my_files.zip', 'w') as myzip:
    print(myzip)
    for file in files_dir.iterdir():
        myzip.write(file)

with ZipFile('my_files.zip', 'r') as myzip:
    print(myzip.infolist())
    myzip.extractall('unzipped')
