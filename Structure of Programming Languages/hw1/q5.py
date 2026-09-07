# Yuval Mashiah | 329245161
# Programming Languages Structure 
# HW Assignment 1 Question 5

import math

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, math.isqrt(n) + 1))

def get_twin_prime(n):
    return n + 2 if is_prime(n) and is_prime(n + 2) else None

def get_prime_twins_dict(n):
    return {i: get_twin_prime(i) for i in range(2, n + 1) if is_prime(i)}

num_str = input("enter number:\n")
if num_str.isdigit():
    num = int(num_str)
    twin = get_twin_prime(num)
    
    if twin is not None:
        print(twin)
    else:
        print("invalid input")
else:
    print("invalid input")