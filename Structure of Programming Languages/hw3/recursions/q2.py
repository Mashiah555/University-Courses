# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 2 of Recursions
# ==========================================

import q1

# Method 1: Regular Recursion
# ------------------------------------------
def sum_tuple_regular(t: tuple) -> int:
    """
    Calculates the sum of elements in a tuple using regular recursion.
    Slices the tuple in each call until it is empty.
    """
    return 0 if not t else t[0] + sum_tuple_regular(t[1:])

# Method 2: Tail Recursion
# ------------------------------------------
def sum_tuple_tail(t: tuple, acc: int = 0) -> int:
    """
    Calculates the sum of elements in a tuple using tail recursion.
    Accumulates the running sum in the `acc` parameter.
    """
    return acc if not t else sum_tuple_tail(t[1:], acc + t[0])

# Execution
# ------------------------------------------
# print("Regular Recursion Sum:", sum_tuple_regular(q1.create_tuple_tail()))
# print("Tail Recursion Sum:", sum_tuple_tail(q1.create_tuple_tail()))