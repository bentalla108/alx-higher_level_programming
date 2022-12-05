#!/usr/bin/python3
def print_last_digit(number):
    print(abs(number) % 10, end='')  # find last digit of number and print
    return (abs(number) % 10)  # return all last digits from numbers
