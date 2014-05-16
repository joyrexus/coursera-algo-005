from random import randrange
from quicksort import partition, quicksort
from quicksort import first, last, median, Counter


def test_partition():
    #     l&i                      r 
    arr = [4, 8, 7, 0, 2, 6, 5, 3, 1]
    i = 0                               # index of pivot element
    l = 0                               # index of starting element
    r = len(arr) - 1                    # index of ending element
    assert i == 0, 'index of pivot element is set to first element'
    assert arr[i] == 4
    i = partition(arr, l, r, i)
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
    i = partition(arr, l, r, i)
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
    i = partition(arr, l, r, i)
    assert i == 1
    assert arr[i] == 1
    assert all(x < 1 for x in arr[l:i])
    assert all(x > 1 for x in arr[i+1:r])

    #            l     i     r
    arr = [4, 8, 7, 0, 2, 6, 5, 3, 1]
        # [      7, 0, 2, 6, 5      ]
        # [      0, 2, 7, 6, 5      ]
        #  0  1  2  3
    i = 4                               # index of pivot element
    l = 2                               # index of starting element
    r = 6                               # index of ending element
    assert i == 4
    assert arr[i] == 2
    i = partition(arr, l, r, i)
    assert i == 3
    assert arr[i] == 2
    assert all(x < 2 for x in arr[l:i])
    assert all(x > 2 for x in arr[i+1:r])

    #    l&i&r
    arr = [1]
    i = 0                               # index of pivot element
    l = 0                               # index of starting element
    r = 0                               # index of ending element
    comparisons = Counter()
    assert i == 0
    assert arr[i] == 1
    i = partition(arr, l, r, i, count=comparisons)
    assert i == 0
    assert arr[i] == 1
    assert comparisons.total == 0
    assert all(x < 1 for x in arr[l:i])
    assert all(x > 1 for x in arr[i+1:r])

    #      l i&r
    arr = [1, 2]
    i = 1                               # index of pivot element
    l = 0                               # index of starting element
    r = 1                               # index of ending element
    comparisons = Counter()
    assert i == 1
    assert arr[i] == 2
    i = partition(arr, l, r, i, count=comparisons)
    assert i == 1
    assert arr[i] == 2
    assert comparisons.total == 1
    assert all(x < 2 for x in arr[l:i])
    assert all(x > 2 for x in arr[i+1:r])

    #     l&i r
    arr = [1, 2]
    i = 0                               # index of pivot element
    l = 0                               # index of starting element
    r = 1                               # index of ending element
    comparisons = Counter()
    assert i == 0
    assert arr[i] == 1
    i = partition(arr, l, r, i, count=comparisons)
    assert i == 0
    assert arr[i] == 1
    assert comparisons.total == 1
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


def test_median():
    arr = [3, 2, 1]
    assert median(arr, 0, 2) == 1

    arr = [2, 3, 1]
    assert median(arr, 0, 2) == 0

    arr = [1, 3, 2]
    assert median(arr, 0, 2) == 2

    arr = [1, 0]
    assert median(arr, 0, 1) == 0

    arr = [0, 1]
    assert median(arr, 0, 1) == 0

    arr = [1, 5, 3, 6]
    assert median(arr, 0, 3) == 1

    arr = [1, 3, 5, 4, 6]
    assert median(arr, 0, 4) == 2


def test_comparisons():

    # see thread containing test cases:
    # https://class.coursera.org/algo-005/forum/thread?thread_id=312

    input = [2, 5, 4, 3, 0, 9, 8, 6, 1, 20, 17]
    comparisons = Counter()
    quicksort(input, count=comparisons, pivot=first)
    assert comparisons.total == 31

    input = [2, 5, 4, 3, 0, 9, 8, 6, 1, 20, 17]
    comparisons = Counter()
    quicksort(input, count=comparisons, pivot=last)
    assert comparisons.total == 35

    input = [2, 5, 4, 3, 0, 9, 8, 6, 1, 20, 17]
    comparisons = Counter()
    quicksort(input, count=comparisons, pivot=median)
    assert comparisons.total == 24  # should be 24!


    # see thread discussion at
    # https://class.coursera.org/algo-005/forum/thread?thread_id=386
    input = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    comparisons = Counter()
    quicksort(input, count=comparisons, pivot=median)
    assert comparisons.total == 25


    # see thread containing test cases:
    # https://class.coursera.org/algo-005/forum/thread?thread_id=177
    # 
    #   size   first    last      median
    #   10     25       29        21
    #   100    615      587       518
    #   1000   10297    10184     8921

    #       [x.rstrip() for x in open('test-data/10.txt')]
    input = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
    comparisons = Counter()
    quicksort(input, count=comparisons, pivot=first)
    assert comparisons.total == 25

    #       [x.rstrip() for x in open('test-data/10.txt')]
    input = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
    comparisons = Counter()
    quicksort(input, count=comparisons, pivot=last)
    assert comparisons.total == 29

    #       [x.rstrip() for x in open('test-data/10.txt')]
    input = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
    comparisons = Counter()
    quicksort(input, count=comparisons, pivot=median)
    assert comparisons.total == 21

    input = [int(x.rstrip()) for x in open('test-data/100.txt')]
    arr = input[:]
    comparisons = Counter()
    quicksort(arr, count=comparisons, pivot=first)
    assert arr == sorted(input[:])
    assert comparisons.total == 615

    arr = input[:]
    comparisons = Counter()
    quicksort(arr, count=comparisons, pivot=last)
    assert arr == sorted(input[:])
    assert comparisons.total == 587

    arr = input[:]
    comparisons = Counter()
    quicksort(arr, count=comparisons, pivot=median)
    assert arr == sorted(input[:])
    assert comparisons.total == 518

# [int(x.rstrip()) for x in open('input.txt')]

