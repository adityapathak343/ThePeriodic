for i in range(1, 101):
    a = 0
    if i%3 == 0:
        print('Fizz', end='')
        a = 1
    if i%5 == 0:
        print('Buzz', end='')
        a = 1
    if a == 0:
        print(i, end='')
    print('\n')