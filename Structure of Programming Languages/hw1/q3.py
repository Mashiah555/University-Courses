# Yuval Mashiah
# Structure of Programming Languages
# HW Assignment 1 Question 3

def normalize_text(text):
    return "".join(sorted(text.lower().replace(" ", "")))

def are_anagrams(str1, str2):
    return normalize_text(str1) == normalize_text(str2)

text1 = input("enter first text:\n")
text2 = input("enter second text:\n")

if not text1.strip() or not text2.strip():
    print("invalid input")
else:
    print(are_anagrams(text1, text2))