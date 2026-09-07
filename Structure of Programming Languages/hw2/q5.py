# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 2 Question 5

import math
from functools import reduce

# Part A:
def power_function(exponent: int):
    """
    Returns a function that accepts a base and returns the base raised to the given exponent.
    """
    return lambda base: base ** exponent

# Part B:
def get_power_functions_map(n: int):
    """
    Returns a map object containing power functions from exponent 0 up to n-1.
    """
    return map(power_function, range(n))

# Part C:
def taylor_approx_e(x: float, terms: int) -> float:
    """
    Calculates the Taylor approximation for e^x using functional methods.
    Strictly avoids loops and list creations.
    """
    # Retrieve the map of power functions for the given number of terms
    power_funcs = get_power_functions_map(terms)
    
    # Calculate numerators (x^0, x^1, x^2, ...)
    numerators = map(lambda f: f(x), power_funcs)
    
    # Calculate denominators (0!, 1!, 2!, ...)
    denominators = map(math.factorial, range(terms))
    
    # Divide numerators by denominators (using map with two iterables)
    taylor_terms = map(lambda num, den: num / den, numerators, denominators)
    
    # Sum the evaluated terms
    return reduce(lambda a, b: a + b, taylor_terms, 0)


def main():
    """
    Main script execution as requested in Part B, with an added demonstration for Part C.
    """
    # --- Part B Demonstration ---
    n = int(input("Enter number of powers:\n"))
    
    result = get_power_functions_map(n)
    print(type(result))
    
    base = int(input("Enter base:\n"))
    
    # Evaluate each function inside the map object by passing the base
    # The mapped results are converted to a tuple as requested by the example output
    evaluated_tuple = tuple(map(lambda f: f(base), result))
    print(evaluated_tuple)
    
    # --- Part C Demonstration ---
    print("\n--- Part C: Taylor Approximation for e^x ---")
    x_val = 2
    terms_val = 15
    approx = taylor_approx_e(x_val, terms_val)
    print(f"Taylor approximation of e^{x_val} with {terms_val} terms: {approx}")
    print(f"Actual math.exp({x_val}) for comparison: {math.exp(x_val)}")

if __name__ == "__main__":
    main()