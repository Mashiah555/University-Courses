# Yuval Mashiah
# 329245161
# Exercise 5 Submission

import ast

# --- QUESTION 1 ---

def evenprt(n1, n2, n3):
    """
    Prints even numbers in the range [n1, n2], with n3 numbers per line.
    Strictly uses generators for maximum memory efficiency and avoids explicit loops.
    """
    # Create a lazy generator expression for even numbers to save memory
    evens_gen = (str(x) for x in range(n1, n2 + 1) if x % 2 == 0)
    
    # Map the generator functionally to append a newline every n3 items, or a space otherwise
    formatted_gen = map(
        lambda item: f"{item[1]}\n" if (item[0] + 1) % n3 == 0 else f"{item[1]} ", 
        enumerate(evens_gen)
    )
    result = "".join(formatted_gen)
    
    if result:
        # If the total count wasn't a perfect multiple of n3, append a final newline
        if result[-1] != '\n':
            result += '\n'
        print(result, end='')

def q1():
    try:
        n1 = int(input("Enter the value of N1: "))
        n2 = int(input("Enter the value of N2: "))
        n3 = int(input("Enter the value of N3: "))
        
        # Input validation
        if n1 <= 0 or n2 <= n1 or n3 <= 0 or n3 >= (n2 - n1):
            print("ERROR: at least one of the input values is incorrect")
            return
            
        evenprt(n1, n2, n3)
        
    except ValueError:
        print("ERROR: at least one of the input values is incorrect")


# --- QUESTION 2 ---

def napa(n):
    """
    Helper function implementing the Sieve of Eratosthenes using list comprehensions.
    Returns all primes up to 'n', plus '1' as required by the assignment examples.
    """
    # Determine non-primes
    multiples = [j for i in range(2, int(n**0.5) + 1) for j in range(i*2, n + 1, i)]
    
    # Extract primes purely functionally using list comprehension
    return [1] + [x for x in range(2, n + 1) if x not in multiples]

def primefactors(n):
    """
    Returns all prime factors of a positive integer n.
    """
    primes = napa(n)
    
    # List comprehension to filter primes that perfectly divide n
    return [p for p in primes if n % p == 0]

def q2():
    try:
        n = int(input("Enter a positive number:"))
        if n <= 0:
            print("ERROR: the number must be a positive integer")
            return
            
        print(primefactors(n))
        
    except ValueError:
        print("ERROR: the number must be a positive integer")


# --- QUESTION 3 ---

def sortedzip(lst):
    """
    Returns a zip object of the sublists, where each sublist is sorted in ascending order.
    Uses 'str' as the sorting key to prevent TypeErrors when sorting mixed types (ints and strings).
    """
    return zip(*[sorted(sub, key=str) for sub in lst])

def reversedzip(lst):
    """
    Returns a zip object of the sublists, where each sublist is reversed.
    """
    return zip(*[sub[::-1] for sub in lst])

def funczip(func, lst):
    """
    Applies the given function (closure) to the list.
    """
    return func(lst)

def unzippy(zipped_lst):
    """
    Unzips the transposed list back into its original sublists shape.
    The assignment note explicitly asks to find an alternative to N*[] for initializing empty lists.
    Using a nested list comprehension cleanly transposes the matrix functionally without 
    needing to explicitly build and append to empty lists.
    """
    if not zipped_lst: return []
    num_elements = len(zipped_lst[0])
    
    # Generates a matrix functionally
    return [[row[i] for row in zipped_lst] for i in range(num_elements)]

def q3():
    funcs = {
        1: sortedzip,
        2: reversedzip
    }
    
    try:
        size = int(input("Enter the size of the sublists of the list to process: "))
        user_list = input("Enter the list to process: ")
        
        # Safely evaluate string input into a nested python list
        lst = ast.literal_eval(user_list)
            
        # Check that all sublists adhere to the defined size 
        # (using 'any' which acts as a lazy functional evaluator)
        if any(len(sub) != size for sub in lst):
            print(f"ERROR - all sublists must be of size {size}")
            return
        
        print("1: sortedzip")
        print("2: reversedzip")
        choice = int(input("Which function do you want to choose? "))
        
        # Verify function existence
        if choice not in funcs:
            print("ERROR - chosen function does not exist.")
            return
            
        # Execute the closure
        res_iterator = funczip(funcs[choice], lst)
        
        # Convert the zip object to a list
        res_list = list(res_iterator)
        
        print(res_list)
        print(unzippy(res_list))
        
    except (ValueError, SyntaxError, TypeError):
        print("ERROR: input is incorrect")


# --- MAIN MENU ---

def main():
    funcList = [q1, q2, q3]
    descList = [
        "Exit the program", 
        "Question 1 (Even numbers with generators)", 
        "Question 2 (Prime factors using list comprehensions)", 
        "Question 3 (Closures and Zip processing)"
    ]

    while True:
        print("\n" + "=" * 50)
        print("Your choices:")
        for (i, s) in enumerate(descList):
            print(f"{i} : {s}")
            
        try:
            c = int(input("Please enter your choice: "))
            if c == 0:
                break
            elif 1 <= c <= len(funcList):
                print("-" * 50 + "\n")
                funcList[c - 1]()
            else:
                print("Error")
        except ValueError:
            print("Error")

if __name__ == "__main__":
    main()