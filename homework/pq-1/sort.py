class MergeSort:
    '''
    A modified merge-sort implementation that counts
    inversions performed on the input array.

    We count an inversion whenever two elements from the input array `A` 
    have the following conditions:

        A[i] > A[j]
        i < j

    In other words, we increment the inversion count wherever we find
    an element with a lower index that is numerically greater than an 
    element with a higher index.

    For example, the sequence [2, 4, 1, 3, 5] has three inversions:

        (2, 1)
        (4, 1)
        (4, 3)

    '''
    def __init__(self):
        self.inversions = None  # inversions performed during merge

    def __call__(self, arr):
        return self.sort(arr)

    def split(self, arr):
        '''
        Divide an array into two sub-arrays.

        '''
        n = len(arr)
        i = n / 2
        a, b = arr[:i], arr[i:]
        return a, b

    def merge(self, a, b):
        '''
        Merge two sorted sub-arrays.

        This is where inversions get counted.

        So, we have two sorted sub-arrays, a and b, that we're
        merging.  If every element of `b` is greater than every
        element of `a`, we don't have any inversion conditions
        and we're just merging the two arrays: first each element 
        of `a` gets appended to the result, then each element of 
        `b` gets appended.

        On the other hand, when b[j] > a[i], we have an inversion 
        condition.  Recall that `a` is the left half of the input
        array and `b` is the right half -- each element in the right
        half (of the input array) has an index greater than each 
        element in the left half.

        So, we need to consider how many elements from the left half
        of the input array (`a`) our element from the right half (`b`) 
        has to "pass over" as the two sub-arrays get merged: viz, just 
        those elements from our current position in `a` to
        the end of `a`, viz. `len(a) - i`.

        '''
        i = j = 0
        result = []
        for k in range(len(a) + len(b)):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:   # we have a split inversion!
                self.inversions += len(a) - i
                result.append(b[j])
                j += 1
            if len(a) == i:                 # if end of `a` is reached
                result.extend(b[j:])        # add remainder of `b`
                break
            elif len(b) == j:               # if end of `b` is reached
                result.extend(a[i:])        # add remainder of `a`
                break
        return result

    def sort(self, arr, reset=True):
        '''
        Numerically sort an array.

        '''
        if reset: 
            self.inversions = 0                 # reset inversion count
        if len(arr) < 2: 
            return arr                          # return base case
        a, b = self.split(arr)
        return self.merge(self.sort(a, False),  # don't reset inversion count!
                          self.sort(b, False))


