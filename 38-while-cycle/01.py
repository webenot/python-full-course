import random

random_num = random.randint(1, 5)
while True:
    num = int(input('Enter a number from 1 to 5: '))
    if num != random_num:
        print('Try again...')
        continue
    print('Congratulations!')
    break
