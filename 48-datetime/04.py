import time

my_time = time.time()
print(my_time)

my_time_2 = time.ctime(23452345234)
print(my_time_2)

time.sleep(5)
end_time = time.time()
print('Wakeup after 5s')
print(end_time - my_time)
