# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 3 of Recursions
# ==========================================

# Method 1: Regular Recursion (Using GCD)
# ------------------------------------------
def lcm_regular(a: int, b: int) -> int:
    """
    Calculates LCM using the mathematical formula: `abs(a * b) // GCD(a, b)`.
    This is regular recursion because the division operation occurs 
    after the recursive gcd call returns.
    """
    def gcd(x: int, y: int) -> int:
        return x if y == 0 else gcd(y, x % y)
        
    return 0 if a == 0 or b == 0 else abs(a * b) // gcd(a, b)

# Method 2: Tail Recursion (Using Multiples)
# ------------------------------------------
def lcm_tail(a: int, b: int, multiple: int = 0) -> int:
    """
    Calculates LCM using tail recursion by iteratively checking multiples.
    Passes the accumulated state `multiple` forward.
    The recursive call is the absolute final operation performed.
    """
    return (
        0 if a == 0 or b == 0 else
        multiple if (multiple > 0 and multiple % a == 0 and multiple % b == 0)
        else lcm_tail(a, b, (multiple + a) if multiple > 0 else a)
    )

# Execution
# ------------------------------------------
# print(lcm_regular(6, 4))
# print(lcm_tail(6, 4))