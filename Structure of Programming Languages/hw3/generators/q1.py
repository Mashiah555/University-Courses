# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 1 of Lazy Evaluations & Generators
# ==========================================

import sys
import time
from typing import Any, Callable

# Task A - The Regular Method
# ------------------------------------------
def create_array_eager() -> list:
    """
    Creates a `list` of numbers from 0 to 10000 eagerly.
    All elements are evaluated and loaded into memory immediately.
    """
    return list(range(10001))

# Task A - The Lazy Evaluation Method
# ------------------------------------------
def create_array_lazy() -> Any:
    """
    Creates a generator of numbers from 0 to 10000 lazily.
    Elements are only evaluated when requested.
    """
    return (x for x in range(10001))

# Task B - The Regular Method
# ------------------------------------------
def first_5000_eager(arr: list) -> list:
    """
    Creates a new `list` with the first 5000 elements eagerly, using list slicing.
    """
    return arr[:5000]

# Task B - The Lazy Evaluation Method
# ------------------------------------------
def first_5000_lazy(gen: Any) -> Any:
    """
    Creates a new generator with the first 5000 elements lazily.
    Uses `zip` with `range(5000)` to pull exactly 5000 items without 
    evaluating the rest, keeping it perfectly functional and lazy.
    """
    return (val for _, val in zip(range(5000), gen))

# Execution
# ------------------------------------------
def measure_performance(func: Callable, *args) -> Any:
    """
    Executes a function, measures its execution time and memory footprint,
    and prints the statistics.
    """
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    
    print(f"Function: {func.__name__}")
    print(f"Time taken: {end_time - start_time:.8f} seconds")
    print(f"Memory size: {sys.getsizeof(result)} bytes")
    print(f"Type: {type(result)}\n")
    
    return result

if __name__ == "__main__":
    print("=== Task A without Lazy Evaluation ===")
    eager_full = measure_performance(create_array_eager)
    print("=== Task A with Lazy Evaluation ===")
    lazy_full = measure_performance(create_array_lazy)

    print("=== Task B without Lazy Evaluation ===")
    eager_partial = measure_performance(first_5000_eager, eager_full)
    print("=== Task B with Lazy Evaluation ===")
    lazy_partial = measure_performance(first_5000_lazy, lazy_full)

    print("=== Type Matching ===")
    print("Types match in Eager" if type(eager_full) is type(eager_partial) else "Types do NOT match in Eager")
    print("Types match in Lazy" if type(lazy_full) is type(lazy_partial) else "Types do NOT match in Lazy")