def is_odd(b): 
    return b % 2

def pow(a, b): 
    result = None
    if b == 0:
        return 1
    elif b == 1: 
        return a
    else:
        result = pow(a * a, b / 2)
    if is_odd(b):
        return a * result
    else:
        return result

print [pow(3, x) for x in range(0, 5)]
