import csv
from pathlib import Path

csv_file = Path('test.csv')

with open(csv_file, 'w') as file:
    writer = csv.writer(file, dialect='excel', lineterminator='\n', delimiter=';')
    writer.writerow(['user_id', 'user_name', 'comments'])
    writer.writerow([123, 'Bob', 7])
    writer.writerow([124, 'John', 14])
    writer.writerow([125, 'Michael', 5])

with open(csv_file, 'r') as file:
    reader = csv.reader(file, dialect='excel', lineterminator='\n', delimiter=';')
    print(reader)
    print(type(reader))
    print(reader.line_num)
    for row in reader:
        print(row)
    print(reader.line_num)
    csv_list = list(reader)
    print(csv_list)

csv_file.unlink()
