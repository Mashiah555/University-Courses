# Yuval Mashiah | 329245161
# Programming Languages Structure 
# HW Assignment 1 Question 7

def multiply_by_2(x): return x * 2
def square(x): return x ** 2
def inverse(x): return 1 / x

func_list = [multiply_by_2, square, inverse]

def apply_functions(numbers, funcs):
    return {func.__name__: [func(n) for n in numbers] for func in funcs}