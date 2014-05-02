from math import pow, log

'''
a. (n ^ 2) * log(n)
b. 2 ^ n
c. 2 ^ (n ^ 2)
d. n ^ log(n)
e. n ^ 2

d a e b c

e a d b c
'''

def a(n):
    return pow(n, 2) * log(n, 2)

def b(n): 
    return pow(2, n)

def c(n):
    return pow(2, pow(n, 2))

def d(n):
    return pow(n, log(n, 2))

def e(n):
    return pow(n, 2)

def order(n):
    return sorted((f(n), f.__name__) for f in [a, b, c, d, e])

def answer(ordering):
    return [f for x, f in ordering]

ordering = order(20)
print ordering
ordering = order(30)
print ''.join(answer(ordering))
