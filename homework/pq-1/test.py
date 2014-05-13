import random
from sort import MergeSort


sort = MergeSort()

def test_sorting():
    '''
    Testing sort method.
    
    '''
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([0, 1]) == [0, 1]
    assert sort([1, 0]) == [0, 1]

    n = 1000
    input = range(n)
    random.shuffle(input)
    assert sort(input) == range(n)

def test_basic_inversions():
    '''
    Testing basic cases of inversion counting.
    
    '''
    assert sort([]) == []
    assert sort.inversions == 0, "for empty input"

    assert sort([1]) == [1]
    assert sort.inversions == 0, "for odd-size input"

    assert sort([1, 1]) == [1, 1]
    assert sort.inversions == 0, "for identical elements"

    assert sort([0, 1]) == [0, 1]
    assert sort.inversions == 0, "for correctly ordered case"

    assert sort([1, 0]) == [0, 1]
    assert sort.inversions == 1, "for basic split-inversion case"

    assert sort([1, 0, 1]) == [0, 1, 1]
    assert sort.inversions == 1, "for left inversion"

    assert sort([0, 1, 0]) == [0, 0, 1]
    assert sort.inversions == 1, "for right inversion"

    assert sort([1, 1, 0]) == [0, 1, 1]
    assert sort.inversions == 2, "for multiple left inversions"

    assert sort([1, 0, 0]) == [0, 0, 1]
    assert sort.inversions 
    assert sort.inversions == 2, "for multiple right inversions"

    assert sort([1, 0, 1, 0]) == [0, 0, 1, 1]
    assert sort.inversions == 3, \
        "for split-inversions together with sub-problem results"

    assert sort([1, 0, 1, 1, 0]) == [0, 0, 1, 1, 1]
    assert sort.inversions == 4, \
        "for split-inversions together with sub-problem results"

    assert sort([2, 1, 0, 0]) == [0, 0, 1, 2]
    assert sort.inversions == 5, "for multiple right inversions"

    assert sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert sort.inversions == 6, "for multiple right inversions"

def test_inversions():
    '''
    Testing misc cases of inversion counting.
    
    '''
    sort([1, 3, 5, 2, 4, 6]) 
    assert sort.inversions == 3

    sort([1, 5, 3, 2, 4])
    assert sort.inversions == 4

    sort([5, 4, 3, 2, 1])  
    assert sort.inversions == 10

    n = 10
    input = range(10, 0, -1)    # [10, 9, ..., 1]
    sort(input)
    assert sort.inversions == (n * (n - 1)) / 2, "should be n choose 2"

    sort([1, 6, 3, 2, 4, 5])
    assert sort.inversions == 5

    input = [int(x) for x in '9 12 3 1 6 8 2 5 14 13 11 7 10 4 0'.split()]
    sort(input)
    assert sort.inversions == 56

    input = [ 37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 
              16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 
              38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 
              27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45 ]
    sort(input)
    assert sort.inversions == 590

def test_homework():
    '''
    Testing inversion counting for input file (`input.txt`)
    provided with homework assignment.

    '''
    input = [int(i.rstrip()) for i in open('input.txt')]
    assert len(input) == 100000, 'for provided input'

    sort(input)
    assert sort.inversions == 2407905288, 'for our final answer'
