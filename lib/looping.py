#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

happy_new_year()


def square_integers(int_list):
    # code goes here!
    squared_nums = [num1 ** 2 for num1 in int_list]
    return squared_nums



def fizzbuzz():
    # code goes here!
    for num in range (1, 101):
        if (num%3 == 0 and num%5 == 0):
            print("FizzBuzz")
        elif (num % 3 == 0):
            print("Fizz")
        elif (num % 5 == 0):
            print("Buzz")
        else:
            print(num)
fizzbuzz()