# Yuval Mashiah | 329245161
# Programming Languages Structure
# HW Assignment 1 Question 1

def get_penta_num(n):
    return n * (3*n - 1) // 2

def pentaNumRange(n1, n2):
    return [get_penta_num(num) for num in range(n1, n2)]

print(get_penta_num(1))
print(get_penta_num(2))
print(get_penta_num(3))
print(get_penta_num(4))
print(pentaNumRange(1, 5))