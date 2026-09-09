# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 7 of Recursions
# ==========================================

import sys
sys.setrecursionlimit(2000)

# Method 1: Regular Recursion
# ------------------------------------------
def get_prefix_length(s: str) -> int:
    """
    Helper function to find the length of the consecutive character prefix.
    Uses regular recursion.
    """
    return 1 if len(s) <= 1 or s[0] != s[1] else 1 + get_prefix_length(s[1:])

def encode_rle_regular(s: str) -> str:
    """
    Encodes a string using RLE with regular recursion.
    The concatenation happens after the recursive call returns.
    """
    return "" if not s else s[0] + str(get_prefix_length(s)) + encode_rle_regular(s[get_prefix_length(s):])

# Method 2: Tail Recursion
# ------------------------------------------
def encode_rle_tail(s: str) -> str:
    """
    Encodes a string using RLE with tail recursion.
    Uses an inner helper to pass the accumulated result and current character state forward.
    """
    def rle_helper(rem: str, ch: str, count: int, acc: str) -> str:
        return acc + ch + str(count) if not rem else (
            rle_helper(rem[1:], ch, count + 1, acc) if rem[0] == ch else
            rle_helper(rem[1:], rem[0], 1, acc + ch + str(count))
        )
    
    return "" if not s else rle_helper(s[1:], s[0], 1, "")

def encode_rle(s: str) -> str:
    """
    Wrapper RLE function
    """
    return encode_rle_tail(s)

# Main Script
# ------------------------------------------
if __name__ == "__main__":
    try:
        user_input = input("enter text:\n")
        # If the input is empty or contains only spaces, print "invalid input"
        print("invalid input" if not user_input.strip() else encode_rle(user_input))
    except EOFError:
        pass