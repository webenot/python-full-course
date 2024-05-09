from pathlib import Path

cwd = Path('.')

print(cwd)
print(cwd.absolute())
print(isinstance(cwd, Path))
print(type(cwd))
print(Path.__subclasses__())
print(dir(cwd))

cwd_2 = (Path('D:/') / '/aquilla' / 'work' / 'projects' /
         'python-full-course' / '45-files' / 'test')
print(cwd_2.absolute())
print(cwd_2.exists())
print(cwd_2.is_dir())

if not cwd_2.exists():
    print(cwd_2.mkdir())

if cwd_2.exists():
    print(cwd_2.rmdir())
