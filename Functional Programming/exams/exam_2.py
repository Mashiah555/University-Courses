from functools import reduce


def divs(num):
    return [x for x in range(1, num) if num % x == 0]

def factorials(num):
    if num == 0:
        return []

    def factorize(num):
        if num <= 1:
            return 1
        return num * factorize(num - 1)
    
    return factorials(num // 10) + [factorize(num % 10)]

def special(func, num):
    return reduce(lambda x, y: x + y, func(num))

print(divs(28))
print(special(divs, 28))
print(factorials(145))
print(special(factorials, 145))