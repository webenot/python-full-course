from os import path
from pathlib import Path


current_file_path_1 = path.abspath(('.'))
print(current_file_path_1)
print(type(current_file_path_1))
print(type(path))

print()

current_file_path_2 = Path('.').absolute()
print(current_file_path_2)
print(type(current_file_path_2))
print(type(Path))
