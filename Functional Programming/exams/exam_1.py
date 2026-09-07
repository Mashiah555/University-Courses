import string


letters = list(string.ascii_lowercase)

def creator(*words):
    return {letter: [w for w in words if w.startswith(letter)] for letter in letters}

print(creator('apple', 'banana', 'swimming', 'ant'))