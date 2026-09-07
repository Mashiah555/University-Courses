# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 2 Question 2

import itertools
from functools import reduce

def main():
    # Create a list from 1 to 1000
    numbers = list(range(1, 1001))
    
    # Split the list into evens and odds
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 != 0, numbers))

    # For evens: The accumulator represents the product of the sub-list so far.
    # It is multiplied by the (next element / 2) to match the sequence 1*2, 2*3, 6*4...
    evens_lambda = lambda acc, next_val: acc * (next_val // 2)
    
    # For odds: The linear function Y = X/2 + 2, where X represents 
    # the sum up to the current element plus the next element (acc + next_val)
    odds_lambda = lambda acc, next_val: (acc + next_val) / 2 + 2
    
    # Apply the lambda functions using a higher-order function
    evens_results = list(itertools.accumulate(evens, evens_lambda, initial=1))
    odds_results = list(itertools.accumulate(odds, odds_lambda))
    
    # Sum the results of each list
    sum_lambda = lambda a, b: a + b
    evens_total_sum = reduce(sum_lambda, evens_results)
    odds_total_sum = reduce(sum_lambda, odds_results)
    
    # Print the results.
    # Note: The evens sum grows extremely fast (factorial scale), 
    # so it only prints its length and a small snippet.  
    evens_sum_str = str(evens_total_sum)
    print(f"Evens list results summed (Total digits: {len(evens_sum_str)})")
    print(f"Evens sum snippet: {evens_sum_str[:15]}...{evens_sum_str[-15:]}")
    
    print(f"\nOdds list results summed: {odds_total_sum}")

if __name__ == "__main__":
    main()