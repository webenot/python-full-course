import time

start_time = time.time()

# my_list = list(range(100000000))
# print(my_list[1000])
my_range = range(100000000)
print(my_range[1000])

end_time = time.time()

print('Total duration', end_time - start_time)
