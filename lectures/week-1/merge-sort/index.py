import random

def split(arr):
    n = len(arr)
    i = n / 2
    a, b = arr[:i], arr[i:]
    return a, b

def _merge(a, b, result=[]):
    '''
    Recursive version.

    '''
    if not a:
        return result + b
    if not b:
        return result + a
    if a[0] < b[0]:
        return merge(a[1:], b, result + a[:1])
    else:
        return merge(a, b[1:], result + b[:1])
  

def merge(a, b):
    i = j = 0
    result = []
    for k in range(len(a) + len(b)):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
        if len(a) == i:
            result.extend(b[j:])
            break
        elif len(b) == j:
            result.extend(a[i:])
            break
    return result

def sort(arr):
    if len(arr) < 2: return arr
    a, b = split(arr)
    return merge(sort(a), sort(b))


n = 1000
input = range(n)
random.shuffle(input)

assert sort(input) == range(n)
