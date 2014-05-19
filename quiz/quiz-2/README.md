# Question 2

Consider the following method for calculating `a^b` (where `a` and `b` are positive integers):

```python

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

```

Now assuming that you use a calculator that supports multiplication and
division (i.e., you can do multiplications and divisions in constant time),
what would be the overall asymptotic running time of the above algorithm (as a
function of `b`)?

Note that we only make one recursive call (`a = 1`), our input value is
effectively halved with each recursive call (`b = 2`), and (given our
assumption about multiplications and divisions running in constant time) there
is a constant amount of work done outside of the recursive call and therefore
independent of the size of the input (`d = 0`).

Therefore, we find that `a == b^d` (1 = 2^0) and thus ...

    T(n) = θ(n^d log n) = θ(log n)

