#David Meah - CS362 - HW7 - Q1

def number_counter():
    for list in range(1,6):
        print(list)

def is15(fizzbuzz):
    if fizzbuzz % 15 == 0:
        return 'FizzBuzz'

def is3(fizzbuzz):
    if fizzbuzz % 3 == 0:
        return 'Fizz'

def is5(fizzbuzz):
    if fizzbuzz % 5 == 0:
        return 'Buzz'

#Final version of code
for list in range(1,101):
    if list % 15 == 0:
        print('FizzBuzz')
        continue

    elif list % 3 == 0:
        print('Fizz')
        continue

    elif list % 5 == 0:
        print('Buzz')
        continue

    print(list)
