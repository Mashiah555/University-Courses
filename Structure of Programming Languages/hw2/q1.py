# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 2 Question 1

import time
from functools import reduce

def main():
    # Define the linear function Y = X/2 + 2 using a lambda expression
    linear_function = lambda x: x / 2 + 2
    
    # Create a list of numbers from 0 to 10000
    numbers_list = list(range(10001))
    
    # Apply the lambda expression to the list
    mapped_list = list(map(linear_function, numbers_list))
    
    # Sum the elements of the new list, and
    # measure the execution time of the higher-order function approach
    start_time_hof = time.perf_counter()
    sum_hof = reduce(lambda a, b: a + b, mapped_list)
    end_time_hof = time.perf_counter()
    hof_duration = end_time_hof - start_time_hof
    
    # Measure the execution time of an imperative approach (standard for-loop)
    start_time_imperative = time.perf_counter()
    sum_imperative = 0
    for num in mapped_list:
        sum_imperative += num
    end_time_imperative = time.perf_counter()
    imperative_duration = end_time_imperative - start_time_imperative
    
    # Print the comparison results
    print("--- Runtime Comparison ---")
    print(f"Higher-Order Function Sum: {sum_hof} | Time: {hof_duration:.6f} seconds")
    print(f"Imperative Approach Sum:   {sum_imperative} | Time: {imperative_duration:.6f} seconds")
    
    # Perform the mapping and summation using ONLY ONE higher-order function
    single_hof_sum = reduce(lambda acc, x: acc + (x / 2 + 2), numbers_list, 0)
    
    print("\n--- Single Higher-Order Function ---")
    print(f"Single HOF Sum Result: {single_hof_sum}")

if __name__ == "__main__":
    main()