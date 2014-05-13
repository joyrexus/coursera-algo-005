import random

def quicksort(arr, l=0, r=None):
    '''An in-place implementation of quicksort.'''
    if r is None:
        r = len(arr) - 1
    if l < r:
        i, j, p = l, r + 1, arr[l]
        while i < j:
            i = i + 1
            while i <= r and arr[i] < p: 
                i = i + 1
            j = j - 1
            while j >= l and arr[j] > p: 
                j = j - 1
            if i <= r: 
                arr[i], arr[j] = arr[j], arr[i]
        if i <= r: 
            arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[l] = arr[l], arr[j]
        quicksort(arr, l, j-1)
        quicksort(arr, j+1, r)

def qsort(arr):
    if len(arr) < 2: return arr
    lt, eq, gt = [], [], []                 # less than, equal to, greater than pivot
    p = random.randrange(0, len(arr))       # index of pivot
    pivot = arr[p]
    eq.append(pivot)
    for i, x in enumerate(arr):
        if i == p: continue
        if x == pivot:
            eq.append(x)
        elif x < pivot:
            lt.append(x)
        elif x > pivot:
            gt.append(x)
    return qsort(lt) + eq + qsort(gt)


if __name__ == "__main__":
    input    = [2, 6, 5, 4, 0, 9, 8, 3, 1, 7, 5, 5]
    expected = [0, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    result = qsort(input)
    assert result == expected

    arr = range(10)
    random.shuffle(arr)
    assert qsort(arr) == range(10)

    quicksort(input)
    assert input == expected
