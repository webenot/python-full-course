from datetime import datetime

my_datetime = datetime(2222, 12, 10, 18, 10, 45)

print(my_datetime.strftime('%d/%m/%Y %H:%M:%S'))
print(my_datetime.strftime('%d %b %Y %H:%M:%S'))

date_str = '10/12/2022'
converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print(converted_date)
