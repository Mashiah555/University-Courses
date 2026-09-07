# Yuval Mashiah | 329245161
# Programming Languages Structure 
# HW Assignment 1 Challenge Question 6

def add_3_dicts(d1, d2, d3):
    return {k: tuple(set(d[k] for d in (d1, d2, d3) if k in d)) 
            for k in d1.keys() | d2.keys() | d3.keys()}