from datetime import date, datetime

print(type(date))

my_date = date(2100, 4, 15)

print(my_date)

print(my_date.day)
print(my_date.year)
print(my_date.month)

print(my_date.isocalendar())

my_datetime = datetime(2222, 12, 10, 18, 10, 45)
print(my_datetime)
print(my_datetime.year)
print(my_datetime.second)
print(my_datetime.microsecond)

print(my_datetime.now())
print(my_datetime.now().microsecond)
