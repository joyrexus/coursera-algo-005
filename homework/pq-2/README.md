# General Directions

The file named `input.txt` contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the ith row of the file gives you the ith entry of an input array.

Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length *m*, you should simply add *m − 1* to your running total of comparisons. (This is because the pivot element is compared to each of the other *m − 1* elements in the subarray in this recursive call.)
