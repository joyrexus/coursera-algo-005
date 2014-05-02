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
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                self.inversions += 1
                result.append(b[j])
                j += 1
            if len(a) == i:
                result.extend(b[j:])
                break
            elif len(b) == j:
                result.extend(a[i:])
                break
        return result

    def sort(self, arr):
        '''
        Numerically sort an array.

        '''
        self.inversions = 0             # reset inversion count
        if len(arr) < 2: return arr
        a, b = self.split(arr)
        return self.merge(self.sort(a), self.sort(b))
