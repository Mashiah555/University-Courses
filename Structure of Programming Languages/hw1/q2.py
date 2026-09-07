# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 1 Question 2

def sum_digit(n):
    return sum(int(d) for d in n) if n.isdigit() else 'invalid input'

num = input('enter number:\n')
print(sum_digit(num))
