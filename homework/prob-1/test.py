import random
from sort import MergeSort


sort = MergeSort()

# Testing
n = 1000
input = range(n)
random.shuffle(input)

assert sort(input) == range(n)
assert 100 < sort.inversions < 1000

assert sort([]) == []
assert sort.inversions is 0

assert sort([1, 0]) == [0, 1]
assert sort.inversions is 1

'''
# do I correctly initialize and handle empty input?
Input: {}
expected Output: 0

# do I correctly handle odd-sized input?
I: {0}
O: 0

I: {4294967295} -- try using your max int value
O: 0

# do I correclty handle even-size input?
I: {0, 0}
O: 0

# do I detect basic case of split inversion?
I: {1, 0}
O: 1

# do I actually count the split inversions?
I: {1, 1, 0}
O: 2

# do I accumulate left-inversions?
I: {1, 0, 1, 1}
O: 1

# do I accumulate right-inversions?
I: {0, 0, 1, 0}
O: 1

# do I accumulate split-inversions together with sub-problem results?
I: {1, 0, 1, 0}
O: 3

TEST CASE - 1
A - {1,3,5,2,4,6} 
ANS - 3

TEST CASE - 2
A- {1,5,3,2,4}
ANS - 4

TEST CASE - 3
A- {5,4,3,2,1}  
ANS - 10

TEST CASE - 4 
A - {1,6,3,2,4,5}
ANS - 5

Test Case - #1 - 15 numbers
A - { 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 }
Ans - 56

Test Case - #2 - 50 numbers
A - { 37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45 }
Ans - 590
'''
