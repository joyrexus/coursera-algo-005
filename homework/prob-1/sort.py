class MergeSort:

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

        '''
        i = j = 0
        result = []
        for k in range(len(a) + len(b)):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
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


