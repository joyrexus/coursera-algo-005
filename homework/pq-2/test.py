from random import randrange
from quicksort import partition, quicksort
from quicksort import Counter


def test_partition():
    #     l&i                      r 
    arr = [4, 8, 7, 0, 2, 6, 5, 3, 1]
    i = 0                               # index of pivot element
    l = 0                               # index of starting element
    r = len(arr) - 1                    # index of ending element
    assert i == 0, 'index of pivot element is set to first element'
    assert arr[i] == 4
    i = partition(arr, i, l, r)
    assert i == 4
    assert arr[i] == 4
    assert all(x < 4 for x in arr[l:i])
    assert all(x > 4 for x in arr[i+1:r])

    #      l  i                    r 
    arr = [4, 8, 7, 0, 2, 6, 5, 3, 1]
    i = 1                               # index of pivot element
    l = 0                               # index of starting element
    r = len(arr) - 1                    # index of ending element
    assert i == 1
    assert arr[i] == 8
    i = partition(arr, i, l, r)
    assert i == 8
    assert arr[i] == 8
    assert all(x < 8 for x in arr[l:i])
    assert all(x > 8 for x in arr[i+1:r])

    #      l                      i&r 
    arr = [4, 8, 7, 0, 2, 6, 5, 3, 1]
    i = 8                               # index of pivot element
    l = 0                               # index of starting element
    r = len(arr) - 1                    # index of ending element
    assert i == 8
    assert arr[i] == 1
    i = partition(arr, i, l, r)
    assert i == 1
    assert arr[i] == 1
    assert all(x < 1 for x in arr[l:i])
    assert all(x > 1 for x in arr[i+1:r])


def test_quicksort():
    input = [8, 7, 4, 2, 6, 5, 3, 1]
    arr = input[:]
    quicksort(arr)
    assert arr, sorted(input)

    input = [randrange(1, 100) for x in range(100)]
    arr = input[:]
    quicksort(arr)
    assert arr, sorted(input)


def test_counter():
    count = Counter(5)
    assert count.total == 5
    count(5)
    assert count.total == 10
    count(5)
    assert count.total == 15


def test_comparisons():
    input = [2, 5, 4, 3, 0, 9, 8, 6, 1, 20, 17]
    comparisons = Counter()
    first = lambda l, r: l
    quicksort(input, count=comparisons, pivot=first)
    assert comparisons.total == 31


'''
[x.rstrip() for x in open('input.txt')]

size   first      last      median
10     25        29        21
100   615      587      518
1000 10297 10184  8921
'''
