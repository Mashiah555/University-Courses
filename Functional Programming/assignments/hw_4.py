# Yuval Mashiah
# 329245161
# Exercise 4 Submission

# IMPORTANT REMARKS:
# The assignment states that we were given a function called get_proj_info - which was not provided.
# The assignment contains a function appendix called get_exam_info - that has no actual use.

import ast

# --- QUESTION 1 ---

def get_proj_info(file_name):
    """
    Mock function representing the file parser.
    Since I don't have the actual file, this returns the exact nested 
    structure provided in the assignment description instead.
    """
    return [
        [['a1', 10, 12], []], 
        [['a2', 13, 18], [
            [['a21', 6, 8], []], 
            [['a22', 7, 10], []]
        ]], 
        [['a3', 3, 7], []]
    ]

def proj_times(file_name):
    """
    Part A:
    Reads project data and returns an identically structured nested list, 
    but replaces [name, planned, actual] with [name, diff].
    Uses tree recursion and list comprehensions.
    """
    data = get_proj_info(file_name)
    
    def process_tree(nodes):
        # Tree recursion using list comprehension:
        # node[0] is the activity info: [name, planned, actual]
        # node[1] is the sub-activities list
        return [
            [[node[0][0], node[0][2] - node[0][1]], process_tree(node[1])] 
            for node in nodes
        ]
        
    return process_tree(data)

def proj_time_cost(file_name, cost_per_time_unit):
    """
    Part B:
    Calculates total planned time/cost, actual time/cost, and the differences.
    Only uses the top-level items of the nested list as instructed.
    Uses list comprehensions for sums.
    """
    data = get_proj_info(file_name)
    
    # Extract sums using list comprehensions
    planned_time = sum([node[0][1] for node in data])
    actual_time = sum([node[0][2] for node in data])
    diff_time = actual_time - planned_time
    
    return (
        (planned_time, planned_time * cost_per_time_unit),
        (actual_time, actual_time * cost_per_time_unit),
        (diff_time, diff_time * cost_per_time_unit)
    )

def q1():
    # The file passed for both parts does not make a difference, 
    # as neither the file or its parser function were provided.

    print("--- Part A: proj_times ---")
    print(proj_times("dummy_file.txt"))
    
    print("\n--- Part B: proj_time_cost ---")
    # Using 1000.00 as the cost per time unit just like in the assignment example
    print(proj_time_cost("dummy_file.txt", 1000.00))

# --- QUESTION 2 ---

def reverseList(lst):
    """
    Reverses a nested collection using tree recursion and list/tuple comprehensions.
    If the item is a list, tuple, or string, it recursively reverses it.
    Otherwise, it leaves the item as is.
    """
    if isinstance(lst, list):
        return [reverseList(x) for x in lst[::-1]]
    elif isinstance(lst, tuple):
        return tuple(reverseList(x) for x in lst[::-1])
    elif isinstance(lst, str):
        return lst[::-1]
    else:
        return lst

def q2():
    try:
        user_input = input("Enter a list: ")
        parsed_list = ast.literal_eval(user_input)
        
        if not isinstance(parsed_list, list):
            print("ERROR: Input is not a list!")
            return
            
        print(reverseList(parsed_list))
    except (ValueError, SyntaxError):
        print("ERROR: Input is incorrect!")

# --- QUESTION 3 ---

def isPalindrome(lst):
    """
    Checks if a nested list is a palindrome by comparing it to its reversed self.
    """
    return lst == reverseList(lst)

def q3():
    try:
        user_input = input("Enter a list: ")
        parsed_list = ast.literal_eval(user_input)
        
        if not isinstance(parsed_list, list):
            print("ERROR: Input is not a list!")
            return
            
        if isPalindrome(parsed_list):
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
    except (ValueError, SyntaxError):
        print("ERROR: Input is incorrect!")

# --- QUESTION 4 ---

def sieve(lst):
    """
    Sieve of Eratosthenes implemented purely functionally using 
    recursion and list comprehensions.
    """
    if not lst:
        return []
    # Take the first prime, and recursively filter out all its multiples 
    # from the rest of the list using a list comprehension.
    return [lst[0]] + sieve([x for x in lst[1:] if x % lst[0] != 0])

def twinp(n):
    """
    Returns a dictionary of twin primes in the range [1, n].
    """
    if n < 2:
        return {}
        
    primes = sieve(list(range(2, n + 1)))
    
    # Use dictionary comprehension and list comprehension to find twins
    return {
        primes[i]: primes[i+1] 
        for i in range(len(primes) - 1) 
        if primes[i+1] - primes[i] == 2
    }

def q4():
    user_input = input("Enter a Natural number n: ")
    try:
        n = int(user_input)
        if n <= 0:
            print("ERROR: Input number is incorrect!")
            return
            
        twins = twinp(n)
        
        # Format the output without imperative loops
        output = "\n".join([f"{k} {v}" for k, v in twins.items()])
        if output:
            print(output)
            
    except ValueError:
        print("ERROR: Input number is incorrect!")

# --- QUESTION 5 ---

def add3dicts(d1, d2, d3):
    """
    Merges three dictionaries functionally using list and dictionary comprehensions.
    Values sharing keys are grouped into unique tuples.
    """
    # Create a union of all keys
    all_keys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())
    
    # Helper to fetch a list of values for a given key across all dicts
    get_vals = lambda k: [d[k] for d in (d1, d2, d3) if k in d]
    
    # Helper to deduplicate a list while preserving order (via list comprehension)
    dedup = lambda lst: tuple([x for i, x in enumerate(lst) if x not in lst[:i]])
    
    # Helper to determine the final value shape: raw value if unique, deduped tuple if shared
    final_val = lambda vals: vals[0] if len(vals) == 1 else dedup(vals)
    
    # Dictionary comprehension to build the final dictionary
    return {k: final_val(get_vals(k)) for k in all_keys}

def q5():
    try:
        d1 = eval(input("Enter a dictionary: "))
        d2 = eval(input("Enter a dictionary: "))
        d3 = eval(input("Enter a dictionary: "))
        
        if not (isinstance(d1, dict) and isinstance(d2, dict) and isinstance(d3, dict)):
            raise TypeError
            
        result = add3dicts(d1, d2, d3)
        
        formatted_output = sorted(list(result.items()), key=lambda item: str(item[0]))
        print(formatted_output)
        
    except Exception:
        print("ERROR: Input is incorrect!")

# --- MAIN MENU ---

def main():
    funcList = [q1, q2, q3, q4, q5]
    descList = ["Exit the program", "Question 1", "Question 2", "Question 3", "Question 4", "Question 5"]

    while True:
        print("\n" + "=" * 50)
        print("Your choices:")
        for (i, s) in enumerate(descList):
            print(f"{i}  :  {s}")
        
        try:
            c = int(input("Please enter your choice: "))
            if c == 0:
                break
            elif 1 <= c <= len(descList) - 1:
                print("-" * 50 + "\n")
                funcList[c - 1]()
            else:
                print("Error")
        except ValueError:
            print("Error")

if __name__ == "__main__":
    main()