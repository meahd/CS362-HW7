#David Meah - CS362 - HW7 - Q1

def number_counter():
    for list in range(1,100):
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
