# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 3 Question 6 of Recursions
# ==========================================

# Method 1: Regular Recursion
# ------------------------------------------
def sortedzip_regular(lsts: list) -> zip:
    """
    Recursively applies `sorted` to each sub-list and returns their `zip`.
    Uses regular recursion to build the tuple of sorted lists.
    """
    def recursive_sort(l: list) -> tuple:
        return () if not l else (sorted(l[0]),) + recursive_sort(l[1:])
        
    return zip(*recursive_sort(lsts))

# Method 2: Tail Recursion
# ------------------------------------------
def sortedzip_tail(lsts: list) -> zip:
    """
    Recursively applies `sorted` to each sub-list using tail recursion.
    Accumulates the sorted lists in a tuple to maintain immutability,
    then returns their `zip`.
    """
    def tail_sort(l: list, acc: tuple = ()) -> tuple:
        return acc if not l else tail_sort(l[1:], acc + (sorted(l[0]),))
        
    return zip(*tail_sort(lsts))

# Execution
# ------------------------------------------
# test_lists = [[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']]
# print(list(sortedzip_regular(test_lists)))
# print(list(sortedzip_tail(test_lists)))