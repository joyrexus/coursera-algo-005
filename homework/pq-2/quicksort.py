'''
quicksort - implementation of quicksort algorithm for problem #

'''
from random import randint


# Partition specified subarray in place.
# 
# Arguments:
#
#  arr - array to be partitioned
#  i   - index of pivot value
#  l   - index of leftmost element in subarray
#  r   - index of rightmost element in subarray
# 
#   [   *     p     |   ]
#       l     i     r
# 
#   [   p _   *     |   ]
#       l i         r   
#         j            
# 
# We want to keep the following property of `arr` invariant:
# 
#   [   p |  < p  |  > p  | _   |   ]
#       l         i         j   r   
# 
# ... ultimately re-ordering the array to the following before returning:
#
#   [   |    < p    | p |    > p    |   ] 
#       l             i         j
#       arr[l:i]    arr[i]  arr[i+1:r+1]
#
def partition(arr, l, r, i, count=None, asserting=False):
    if asserting: assert l <= i <= r
    p = arr[i]                              # value of pivot element
    arr[l], arr[i] = arr[i], arr[l]         # swap pivot w/ leftmost element
    i = l + 1                               # start i after leftmost element
    for j in range(i, r + 1):
        if count: count(1)                  # increment comparison count
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j] # swap!
            i += 1                               
    i -= 1
    arr[l], arr[i] = arr[i], arr[l]         # swap pivot w/ LAST > p element
    if asserting: assert all(x < p for x in arr[l:i])
    if asserting: assert all(x >= p for x in arr[i+1:r])
    return i


rand = lambda arr, l, r: randint(l, r)

def quicksort(arr, l=0, r=None, count=None, pivot=rand):
    if r is None: r = len(arr) - 1
    if r - l < 1: return
    i = pivot(arr, l, r)
    i = partition(arr, l, r, i, count)
    quicksort(arr, l, i - 1, count, pivot)
    quicksort(arr, i + 1, r, count, pivot)


# The following are pivot choice methods - you can use these to 
# in `quicksort` to choose a particular element on which to pivot.

def first(arr, l, r): return l

def last(arr, l, r): return r

def median(arr, l, r):
    '''
    Return index of the median value for the following three 
    elements within specified sub-array, where `l` is the index 
    of the first element, `r` is the index of the last element:

    [first, middle-element-between-first-last, last]

    '''
    m = 0 if (r - l) == 1 else ((r - l)) / 2 + l
    M = arr[m]                      # middle element
    L = arr[l]                      # leftmost element
    R = arr[r]                      # rightmost element
    ordered = sorted([(L, l), (M, m), (R, r)])
    return ordered[1][1]            # index of median of the three


class Counter:
    '''
    A simple counter class.

    Useful for counting up the number of 
    comparisons made by quicksort.

    '''
    def __init__(self, n=0):
        self.total = n

    def __call__(self, x=0):
        self.total += x


if __name__ == '__main__':


    # input = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
    # input = [int(x.rstrip()) for x in open('test-data/10.txt')]
    input = [int(x.rstrip()) for x in open('input.txt')]
    for pivot in [first, last, median]:
        arr = input[:]
        count = Counter()
        quicksort(arr, count=count, pivot=pivot)
        assert arr == sorted(input)
        print pivot.__name__, count.total

    # first 162085
    # last 164123
    # median 138382


