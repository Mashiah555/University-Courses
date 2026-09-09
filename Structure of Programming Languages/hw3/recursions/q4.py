# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 4 of Recursions
# ==========================================

# Method 1: Regular Recursion (String slicing)
# ------------------------------------------
def is_palindrome_number_regular(n: int) -> bool:
    """
    Checks if an integer is a palindrome using regular recursion.
    Converts the number to a string and recursively checks if the first 
    and last characters match, shrinking the string in each call.
    """
    def check_str(s: str) -> bool:
        return True if len(s) <= 1 else (s[0] == s[-1] and check_str(s[1:-1]))
    
    return check_str(str(abs(n)))

# Method 2: Tail Recursion (Mathematical reversal)
# ------------------------------------------
def is_palindrome_number_tail(n: int) -> bool:
    """
    Checks if an integer is a palindrome using tail recursion.
    Uses a helper function to mathematically reverse the number using an accumulator `acc`. 
    The recursive call is the absolute final operation.
    """
    def reverse_tail(remaining: int, acc: int = 0) -> int:
        return acc if remaining == 0 else reverse_tail(remaining // 10, acc * 10 + (remaining % 10))
        
    return str(n) == str(n)[::-1] if n < 0 else n == reverse_tail(n)

# Execution
# ------------------------------------------
# print(is_palindrome_number_regular(123454321))
# print(is_palindrome_number_tail(123454321))
# print(is_palindrome_number_tail(1234554321))