while True:
    try:
        num_1 = float(input('Enter a first number: '))
        num_2 = float(input('Enter a second number: '))
    except Exception as e:
        print(e)
        print('Values should be numbers')
        continue
    if num_2 == 0:
        print('The second number is zero. Please, try again.')
        continue
    print(num_1 / num_2)
    do_continue = input('Continue? [yes/no]: ')
    if do_continue == 'no':
        break
