# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 1 of Recursions
# ==========================================

import sys
sys.setrecursionlimit(2000)

# Method 1: Regular Recursion
# ------------------------------------------
def create_tuple_regular(n: int = 1000) -> tuple:
    """
    Creates a tuple of numbers from 1 to n using regular recursion.
    The function waits for the recursive call to return before concatenating.
    """
    return (1,) if n == 1 else create_tuple_regular(n - 1) + (n,)

# Method 2: Tail Recursion
# -----------------------------------------
def create_tuple_tail(n: int = 1000, acc: tuple = ()) -> tuple:
    """
    Creates a tuple of numbers from 1 to n using tail recursion.
    Passes the accumulated tuple `acc` forward, avoiding operations after the return.
    """
    return acc if n == 0 else create_tuple_tail(n - 1, (n,) + acc)

# Execution
# -----------------------------------------
# print(create_tuple_regular())
# print(create_tuple_tail())