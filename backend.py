import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError

    return a/b

def logarithm(a, b):
    if b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b
