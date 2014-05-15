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
#   [   |  < p  | p |  > p  |   ] 
#       l         i         j
#
def partition(arr, i, l, r, count):
    assert l <= i <= r
    p = arr[i]                              # value of pivot element
    arr[l], arr[i] = arr[i], arr[l]         # swap pivot w/ leftmost elemnt
    i = l + 1                               # elements before index i should be < p
    for j in range(i, r + 1):
        count(1)
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i] # swap!
            i += 1                               
    i -= 1
    arr[l], arr[i] = arr[i], arr[l]         # swap pivot w/ rightmost of LT
    return i


def quicksort(arr, l=0, r=None, count=None, pivot=randint):
    if r is None: r = len(arr) - 1
    if l >= r: return
    i = pivot(l, r)
    i = partition(arr, i, l, r, count)
    quicksort(arr, l, i - 1, count, pivot)
    quicksort(arr, i + 1, r, count, pivot)


class Counter:

    def __init__(self, n=0):
        self.total = n

    def __call__(self, x=0):
        self.total += x


if __name__ == '__main__':

    first = lambda l, r: l
    last  = lambda l, r: r
    arr = [2, 5, 4, 3, 0, 9, 8, 6, 1, 20, 17]

    for pivot in [first, last]:
        input = arr[:]
        count = Counter()
        quicksort(input, count=count, pivot=pivot)
        print count.total

    input = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
    count = Counter()
    quicksort(input, count=count, pivot=first)

    input = [x.rstrip() for x in open('100.txt')]
    arr = input[:]
    count = Counter()
    quicksort(arr, count=count, pivot=first)
    assert arr == sorted(input)
    print count.total
