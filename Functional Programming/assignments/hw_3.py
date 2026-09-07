# Yuval Mashiah
# 329245161
# Exercise 3 Submission

# --- QUESTION 1 ---

# Non-tail recursive implementation
def pentaNumRange_nontail(n1, n2):
    getPentaNum = lambda n: (n * (3 * n - 1)) / 2
    if n1 >= n2:
        return []
    return [getPentaNum(n1)] + pentaNumRange_nontail(n1 + 1, n2)

# Tail recursive implementation
def pentaNumRange_tail(n1, n2, acc=None):
    if acc is None:
        acc = []
    getPentaNum = lambda n: (n * (3 * n - 1)) / 2
    if n1 >= n2:
        return acc
    acc.append(getPentaNum(n1))
    return pentaNumRange_tail(n1 + 1, n2, acc)

# Wrapper that calls one of the implementations (Tail recursion preferred)
def pentaNumRange(n1, n2):
    return pentaNumRange_tail(n1, n2)

def q1():
    """
    Reads inputs, validates them, and prints the pentagonal 
    numbers using a standard 'for' loop as explicitly requested.
    """
    try:
        n1 = int(input("enter the value of n1: "))
        n2 = int(input("enter the value of n2: "))
        
        if n1 <= 0 or n2 <= n1:
            print("ERROR: the values must be positive integers and n2 > n1")
            return
        
        nums = pentaNumRange(n1, n2)
        
        # Explicit for-loop as permitted by Q1 instructions
        for i in range(len(nums)):
            print(float(nums[i]), end=" ")
            if (i + 1) % 10 == 0:
                print()
                
        if len(nums) % 10 != 0:
            print()
            
    except ValueError:
        print("ERROR: the values must be positive integers and n2 > n1")

# --- QUESTION 2 ---

# Non-tail recursive implementation
def reverseNum_nontail(n):
    s = str(abs(n))
    def rev(s_str):
        if not s_str: return ""
        return s_str[-1] + rev(s_str[:-1])
    res = int(rev(s))
    return res if n >= 0 else -res

# Tail recursive implementation
def reverseNum_tail(n):
    s = str(abs(n))
    def rev_tail(s_str, acc=""):
        if not s_str: return acc
        return rev_tail(s_str[:-1], acc + s_str[-1])
    res = int(rev_tail(s))
    return res if n >= 0 else -res

def reverseNum(n):
    return reverseNum_tail(n)

def q2():
    user_input = input("Enter an integer number n (positive or negative): ")
    try:
        n = int(user_input)
        
        # Calculate using our recursive function
        res = reverseNum(n)
        print(res)
        
        # Validation logic requested by instructions
        s_list = list(str(abs(n)))
        built_in_rev = int("".join(reversed(s_list)))
        if n < 0:
            built_in_rev = -built_in_rev
            
        if res != built_in_rev:
            print("ERROR")
            
    except ValueError:
        print("ERROR: Input number is incorrect!")

# --- QUESTION 3 ---

# Non-tail recursive implementation
def pi_nontail(n):
    if n == 0:
        return 0
    term = ((-1)**(n + 1)) / (2 * n - 1)
    return 4 * term + pi_nontail(n - 1)

# Tail recursive implementation
def pi_tail(n, i=1, acc=0):
    if i > n:
        return acc
    term = ((-1)**(i + 1)) / (2 * i - 1)
    return pi_tail(n, i + 1, acc + 4 * term)

def pi(n):
    return pi_tail(n)

def q3():
    user_input = input("Enter a Natural number n: ")
    try:
        n = int(user_input)
        if n <= 0:
            print("ERROR: Input number is incorrect!")
            return
            
        # Recursive print loop (since 'for'/'while' is forbidden)
        def print_pi_loop(i, max_n):
            if i > max_n: return
            print(f"{i} {pi(i)}")
            print_pi_loop(i + 1, max_n)
            
        print_pi_loop(1, n)
        
    except ValueError:
        print("ERROR: Input number is incorrect!")

# --- QUESTION 4 ---

# Helper for Sieve: Filter multiples (Non-Tail)
def filter_mults_nontail(lst, prime):
    if not lst: return []
    if lst[0] % prime == 0:
        return filter_mults_nontail(lst[1:], prime)
    return [lst[0]] + filter_mults_nontail(lst[1:], prime)

# Helper for Sieve: Filter multiples (Tail)
def filter_mults_tail(lst, prime, acc=None):
    if acc is None: acc = []
    if not lst: return acc
    if lst[0] % prime != 0:
        acc.append(lst[0]) # Local state mutation permitted for tail recursion
    return filter_mults_tail(lst[1:], prime, acc)

# Sieve of Eratosthenes (Non-Tail)
def sieve_nontail(lst):
    if not lst: return []
    p = lst[0]
    return [p] + sieve_nontail(filter_mults_nontail(lst[1:], p))

# Sieve of Eratosthenes (Tail)
def sieve_tail(lst, acc=None):
    if acc is None: acc = []
    if not lst: return acc
    p = lst[0]
    acc.append(p)
    return sieve_tail(filter_mults_tail(lst[1:], p), acc)

# Twin Primes Extractor (Non-Tail)
def get_twins_nontail(primes):
    if len(primes) < 2: return {}
    p1, p2 = primes[0], primes[1]
    res = get_twins_nontail(primes[1:])
    if p2 - p1 == 2:
        res[p1] = p2
    return res

# Twin Primes Extractor (Tail)
def get_twins_tail(primes, acc=None):
    if acc is None: acc = {}
    if len(primes) < 2: return acc
    p1, p2 = primes[0], primes[1]
    if p2 - p1 == 2:
        acc[p1] = p2
    return get_twins_tail(primes[1:], acc)

def twinp(n):
    if n < 2: return {}
    primes = sieve_tail(list(range(2, n + 1)))
    return get_twins_tail(primes)

def q4():
    user_input = input("Enter a Natural number n: ")
    try:
        n = int(user_input)
        if n <= 0:
            print("ERROR: Input number is incorrect!")
            return
            
        twins = twinp(n)
        
        # Recursive print loop
        def print_dict_loop(keys, d):
            if not keys: return
            print(f"{keys[0]} {d[keys[0]]}")
            print_dict_loop(keys[1:], d)
            
        print_dict_loop(list(twins.keys()), twins)
        
    except ValueError:
        print("ERROR: Input number is incorrect!")

# --- QUESTION 5 ---

# Dictionary builder (Non-Tail)
def build_dict_nontail(keys, val_func):
    if not keys: return {}
    res = build_dict_nontail(keys[1:], val_func)
    res[keys[0]] = val_func(keys[0])
    return res

# Dictionary builder (Tail)
def build_dict_tail(keys, val_func, acc=None):
    if acc is None: acc = {}
    if not keys: return acc
    acc[keys[0]] = val_func(keys[0])
    return build_dict_tail(keys[1:], val_func, acc)

def add3dicts(d1, d2, d3):
    s1, s2, s3 = set(d1.keys()), set(d2.keys()), set(d3.keys())
    
    get_common_keys = lambda a, b, c: (a & b) | (b & c) | (a & c)
    get_unique_keys = lambda a, b, c: (a | b | c) - get_common_keys(a, b, c)
    
    common_keys = list(get_common_keys(s1, s2, s3))
    unique_keys = list(get_unique_keys(s1, s2, s3))
    
    get_unique_val = lambda k: d1[k] if k in d1 else (d2[k] if k in d2 else d3[k])
    
    # Functionally fetch and deduplicate list 
    def deduplicate_tail(lst, acc=None):
        if acc is None: acc = []
        if not lst: return acc
        if lst[0] not in acc:
            acc.append(lst[0])
        return deduplicate_tail(lst[1:], acc)

    get_all_vals = lambda k: ([] if k not in d1 else [d1[k]]) + \
                             ([] if k not in d2 else [d2[k]]) + \
                             ([] if k not in d3 else [d3[k]])
                             
    get_common_vals = lambda k: tuple(deduplicate_tail(get_all_vals(k)))
    
    unique_dict = build_dict_tail(unique_keys, get_unique_val)
    common_dict = build_dict_tail(common_keys, get_common_vals)
    
    return {**unique_dict, **common_dict}

def q5():
    try:
        d1 = eval(input("Enter a dictionary: "))
        d2 = eval(input("Enter a dictionary: "))
        d3 = eval(input("Enter a dictionary: "))
        
        if not (isinstance(d1, dict) and isinstance(d2, dict) and isinstance(d3, dict)):
            raise TypeError
            
        print(add3dicts(d1, d2, d3))
        
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