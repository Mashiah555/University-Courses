# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 2 of Lazy Evaluations & Generators
# ==========================================

import sys
sys.setrecursionlimit(5000)

# Pure Functional Prime Checker
# ------------------------------------------
def is_prime(n: int, divisor: int = 2) -> bool:
    """
    Checks if a number is prime using recursion instead of loops.
    """
    return False if n < 2 else (
        True if divisor * divisor > n else (
            False if n % divisor == 0 else is_prime(n, divisor + 1)
        )
    )

# Prime Numbers Generator
# ------------------------------------------
def prime_generator(current: int = 2):
    """
    A generator that yields the next prime number indefinitely.
    Uses recursion and `yield from` to completely avoid loops and 
    mutable variables while maintaining the lazy evaluation state.
    """
    if is_prime(current):
        yield current
        
    yield from prime_generator(current + 1)

# Execution
# ------------------------------------------
if __name__ == "__main__":
    # Initialize the generator
    primes = prime_generator()
    
    # print(next(primes))  # 2
    # print(next(primes))  # 3
    # print(next(primes))  # 5
    # print(next(primes))  # 7
    # print(next(primes))  # 11