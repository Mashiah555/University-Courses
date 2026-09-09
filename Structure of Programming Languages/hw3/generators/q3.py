# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 3 of Lazy Evaluations & Generators
# ==========================================

import sys
sys.setrecursionlimit(5000)

# Taylor Series Generator for e^x
# ------------------------------------------
def taylor_exp_generator(x: float, n: int = 0, current_term: float = 1.0, current_sum: float = 0.0):
    """
    A generator that calculates the Taylor series for e^x lazily.
    Uses recursion to pass the state (n, current_term, and current_sum) forward
    without using loops or mutable variables.
    
    `x`: The exponent (e.g., 2 for e^2).
    `n`: The current `step/iteration`.
    `current_term`: The calculated value of `x^n / n!`.
    `current_sum`: The accumulated sum of the series up to step `n-1`.
    """
    # Calculate the new sum for the current step
    next_sum = current_sum + current_term
    
    # Yield the current sum to the caller
    yield next_sum
    
    # Calculate the next term mathematically: term(n+1) = term(n) * (x / (n + 1))
    next_term = current_term * (x / (n + 1))
    
    # Recursively yield from the next state
    yield from taylor_exp_generator(x, n + 1, next_term, next_sum)

# Execution
# ------------------------------------------
if __name__ == "__main__":
    # Initialize the generator for e^2
    e_squared_gen = taylor_exp_generator(2.0)
    
    # Fetching the first 8 elements to match the output example
    for _ in range(8):  # Using a loop only in the test script, not in the logic
        print(next(e_squared_gen))