# Yuval Mashiah
# 329245161
# Exercise 2 Submittion

import math
import ast
import random

# --- QUESTION 1 ---

def pentaNumRange(n1, n2):
    """
    Part A:
    Returns a map object (iterator) of pentagonal numbers in the range [n1, n2).
    Uses a local lambda function to calculate the n-th pentagonal number.
    """
    # Lambda expression to calculate the n-th pentagonal number
    getPentaNum = lambda n: (n * (3 * n - 1)) / 2
    
    # Returns a map object applying the lambda to every number in the range
    return map(getPentaNum, range(n1, n2))

def printPentaImperative():
    """
    Part B:
    Imperative approach to read inputs, validate them, and print the pentagonal 
    numbers using a standard 'for' loop (10 numbers per line).
    """
    try:
        n1 = int(input("enter the value of n1: "))
        n2 = int(input("enter the value of n2: "))
        
        # Validation checks
        if n1 <= 0 or n2 <= n1:
            print("ERROR: the values must be positive integers and n2 > n1")
            return
        
        # Using a standard loop to format 10 numbers per line
        nums = list(pentaNumRange(n1, n2))
        for i in range(len(nums)):
            print(nums[i], end=" ")
            if (i + 1) % 10 == 0:
                print()
                
        # Print a final newline if the last row isn't exactly 10 items
        if len(nums) % 10 != 0:
            print()
            
    except ValueError:
        print("ERROR: the values must be positive integers and n2 > n1")

def printPentaFunctional():
    """
    Part C:
    Functional approach. Performs the same task as Part B but strictly uses
    functional programming tools (map, filter, lambda) without explicit loops.
    """
    try:
        n1 = int(input("enter the value of n1: "))
        n2 = int(input("enter the value of n2: "))
        
        if n1 <= 0 or n2 <= n1:
            print("ERROR: the values must be positive integers and n2 > n1")
            return
        
        # To avoid loops, we use enumerate() to attach an index to each pentagonal number.
        # Then, we map over them, returning a string with a newline '\n' for every 10th element.
        formatted_strings = map(
            lambda item: f"{item[1]} \n" if (item[0] + 1) % 10 == 0 else f"{item[1]} ", 
            enumerate(pentaNumRange(n1, n2))
        )
        
        # Join the mapped strings together and strip any trailing whitespace/newlines
        print("".join(formatted_strings).strip())
        
    except ValueError:
        print("ERROR: the values must be positive integers and n2 > n1")

def q1():
    printPentaFunctional()

# --- QUESTION 2 ---

def sumDigits(n):
    """
    Part A:
    Calculates and returns the sum of the digits of an integer 'n'.
    Works for both positive and negative integers.
    Uses only functional tools and built-in functions: abs, str, list, map, and sum.
    """
    # 1. abs(n) removes the negative sign if the number is negative.
    # 2. str() converts the positive number into a string of characters.
    # 3. list() converts that string into a list of individual character strings.
    # 4. map(int, ...) applies the int() function to every character, turning them back into numbers.
    # 5. sum() adds all the numbers in the resulting map object together.
    return sum(map(int, list(str(abs(n)))))

def processUserInput():
    """
    Part B:
    Reads an input from the user, validates that it is a valid integer 
    (rejecting floats and strings), and prints the sum of its digits.
    """
    user_input = input("Enter an integer number n (positive or negative): ")
    
    try:
        # Attempt to convert the input directly to an integer
        n = int(user_input)
        
        # If successful, pass it to the pure function and print the result
        print(sumDigits(n))
        
    except ValueError:
        # A ValueError occurs if the user types a float (e.g., 231.5) or letters.
        # We catch this error and print the exact message requested.
        print("ERROR: Input number is incorrect!")

def q2():
    processUserInput()

# --- QUESTION 3 ---

def reverseDigits(n):
    """
    Helper function to reverse the digits of a number.
    It takes an integer n, removes the sign using abs(), converts it to a string,
    then to a list of characters, and finally reverses the list using slicing [::-1].
    """
    return list(str(abs(n)))[::-1]

def isPalindrome(n):
    """
    Checks if a given integer n is a palindrome.
    It converts the absolute value of the number to a list of digits and 
    compares it strictly against the reversed list from reverseDigits(n).
    Returns a boolean (True or False).
    """
    # Compare the forward list of digits with the reversed list of digits
    return list(str(abs(n))) == reverseDigits(n)

def processPalindromeInput():
    """
    Reads an input from the user, validates that it is a proper integer,
    calls the isPalindrome function, and prints the exact requested output.
    """
    user_input = input("Enter an integer number n (positive or negative): ")
    
    try:
        # Attempt to cast the user's input to an integer
        n = int(user_input)
        
        # Check the boolean result of the pure function
        if isPalindrome(n):
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
            
    except ValueError:
        # If the input is a float (like 12.21) or contains text, print the error
        print("ERROR: Input number is incorrect!")

def q3():
    processPalindromeInput()

# --- QUESTION 4 ---

def getSeriesElements(n):
    """
    Helper function (Hint A): Builds and returns a sequence of the series elements 
    for positions in the range [1, n].
    
    Uses a lambda expression (Hint B) to express the mathematical formula: i / (i + 1).
    """
    term_formula = lambda i: i / (i + 1)
    
    # map() applies the lambda formula to every integer in the range 1 through n
    return map(term_formula, range(1, n + 1))

def m(n):
    """
    Part A:
    Receives a positive integer 'n' and returns the sum of the first 'n' elements 
    in the mathematical series.
    
    Applies the built-in sum() function to the values returned by the helper function (Hint C).
    """
    return sum(getSeriesElements(n))

def processSeriesInput():
    """
    Part B:
    Reads an input from the user, validates that it is a natural number (n > 0),
    and applies the function m(i) to every number from 1 to n.
    Prints the index and the calculated sum on a new line.
    
    Adheres strictly to functional principles by avoiding 'for' or 'while' loops.
    """
    user_input = input("Enter a Natural number n: ")
    
    try:
        n = int(user_input)
        
        # A natural number must be strictly greater than 0
        if n <= 0:
            print("ERROR: Input number is incorrect!")
            return
            
        # Functional approach: map() applies a lambda that formats the string "i m(i)"
        # \n.join() stitches all the resulting strings together into a single block of text
        formatted_output = "\n".join(map(lambda i: f"{i} {m(i)}", range(1, n + 1)))
        
        print(formatted_output)
        
    except ValueError:
        # Catch non-integer inputs (like text or floats)
        print("ERROR: Input number is incorrect!")

def q4():
    processSeriesInput()

# --- QUESTION 5 ---

def add3dicts(d1, d2, d3):
    """
    Takes three dictionaries and merges them functionally.
    - If a key appears in >1 dictionary, its values are combined into a tuple without duplicates.
    - If a key appears in only 1 dictionary, it is transferred as-is.
    """
    # Extract the keys into sets
    s1, s2, s3 = set(d1.keys()), set(d2.keys()), set(d3.keys())
    
    # Hint: Helper lambdas operating on sets
    # Common keys appear in at least two sets (intersection logic)
    get_common_keys = lambda a, b, c: (a & b) | (b & c) | (a & c)
    
    # Unique/foreign keys appear in the union of all sets minus the common keys
    get_unique_keys = lambda a, b, c: (a | b | c) - get_common_keys(a, b, c)
    
    common_keys = get_common_keys(s1, s2, s3)
    unique_keys = get_unique_keys(s1, s2, s3)
    
    # Helper lambda to extract a value for a unique key 
    # (Checks d1, then d2, then d3. It's guaranteed to be in exactly one)
    get_unique_val = lambda k: d1[k] if k in d1 else (d2[k] if k in d2 else d3[k])
    
    # Helper lambda to extract and deduplicate multiple values for a common key
    # It builds a list of values, then uses dict.fromkeys() to remove duplicates while preserving order
    get_common_vals = lambda k: tuple(dict.fromkeys(
        ([d1[k]] if k in d1 else []) + 
        ([d2[k]] if k in d2 else []) + 
        ([d3[k]] if k in d3 else [])
    ))
    
    # Build the merged dictionaries using dictionary comprehensions (functional mapping)
    # The ** operator unpacks them into a single new dictionary.
    return {
        **{k: get_unique_val(k) for k in unique_keys}, 
        **{k: get_common_vals(k) for k in common_keys}
    }

def processDictInput():
    """
    User interface function to read 3 dictionaries, execute add3dicts, 
    and print the result or an error message.
    """
    try:
        d1_str = input("Enter a dictionary: ")
        d2_str = input("Enter a dictionary: ")
        d3_str = input("Enter a dictionary: ")
        
        # We use eval() here because the assignment example inputs include 
        # explicit Python casting syntax like "dict([(5,(2,6,'def')) ... ])"
        # which standard ast.literal_eval cannot process.
        d1 = eval(d1_str)
        d2 = eval(d2_str)
        d3 = eval(d3_str)
        
        # Validate that all inputs successfully evaluated into dictionary objects
        if not (isinstance(d1, dict) and isinstance(d2, dict) and isinstance(d3, dict)):
            raise TypeError
            
        # Execute pure function and print
        print(add3dicts(d1, d2, d3))
        
    except Exception:
        # Catches syntax errors (like the typo in the assignment's second test case)
        # and validation errors.
        print("ERROR: Input is incorrect!")

def q5():
    processDictInput()

# --- MAIN MENU ---

def main():
    funcList = [q1, q2, q3, q4, q5]
    descList = ["Exit the program", "Question 1", "Question 2", "Question 3", "Question 4", "Question 5"]

    while True:
        print("\n" + "=" * 50)
        print("Your choices:")
        for (i, s) in enumerate(descList):
            print(i, " : ", s)
        c = int(input("Please enter your choice: "))
        if c == 0:
            break
        elif 1 <= c <= len(descList):
            print("-" * 50 + "\n")
            funcList[c - 1]()
        else:
            print("Error")

if __name__ == "__main__":
    main()