# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 5 of Recursions
# ==========================================

import sys
sys.setrecursionlimit(2000)

# Dictionary for mapping Hebrew final letters to their regular equivalents
HEBREW_FINALS = {'ך': 'כ', 'ם': 'מ', 'ן': 'נ', 'ף': 'פ', 'ץ': 'צ'}

# Pure Helper Functions (Used by both methods)
# ------------------------------------------
def normalize_char(c: str) -> str:
    """
    Converts a character to lowercase and normalizes Hebrew final letters.
    """
    return HEBREW_FINALS.get(c.lower(), c.lower())

# Method 1: Regular Recursion
# ------------------------------------------
def clean_string_regular(s: str) -> str:
    """
    Cleans the string using regular recursion.
    Filters out non-alphanumeric characters and normalizes the rest.
    """
    return "" if not s else (normalize_char(s[0]) if s[0].isalnum() else "") + clean_string_regular(s[1:])

def is_palindrome_regular_check(s: str) -> bool:
    """
    Checks if a cleaned string is a palindrome using regular recursion.
    """
    return True if len(s) <= 1 else (s[0] == s[-1] and is_palindrome_regular_check(s[1:-1]))

def is_palindrome_alphanumeric_regular(text: str) -> bool:
    """
    Main function for Method 1: Cleans and then checks the palindrome.
    """
    return is_palindrome_regular_check(clean_string_regular(text))

# Method 2: Tail Recursion
# ------------------------------------------
def clean_string_tail(s: str, acc: str = "") -> str:
    """
    Cleans the string using tail recursion, accumulating the valid characters.
    """
    return acc if not s else clean_string_tail(s[1:], acc + (normalize_char(s[0]) if s[0].isalnum() else ""))

def is_palindrome_tail_check(s: str) -> bool:
    """
    Checks if a cleaned string is a palindrome using tail recursion.
    The recursive call is the absolute final operation.
    """
    return True if len(s) <= 1 else (is_palindrome_tail_check(s[1:-1]) if s[0] == s[-1] else False)

def is_palindrome_alphanumeric_tail(text: str) -> bool:
    """
    Main function for Method 2: Cleans and then checks the palindrome.
    """
    return is_palindrome_tail_check(clean_string_tail(text))

# Main Script
# ------------------------------------------
if __name__ == "__main__":
    try:
        user_input = input("enter text:\n")
        # If the input is empty or contains only spaces, print "invalid input"
        print("invalid input" if not user_input.strip() else is_palindrome_alphanumeric_tail(user_input))
    except EOFError:
        pass