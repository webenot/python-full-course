all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = [abs(num) for num in all_nums]
absolute_nums_2 = [abs(num) for num in all_nums if num < 0]
positive_nums = [num for num in all_nums if num > 0]

print(absolute_nums)
print(absolute_nums_2)
print(positive_nums)
print(all_nums)
