"""
Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element

 kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based ) 
NOTE
You are not allowed to modify the array ( The array is read only ). 
Try to do it using constant extra space.
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        if not A:
            return -1
        previous_smallest = -1
        smallest = None
        count = 0
        for i in xrange(len(A)):
            for n in A:
                # Find smallest
                if n > previous_smallest:
                    if smallest == None or n < smallest:
                        smallest = n
    
            for n in A:
                if n <= smallest:
                    count += 1
                if count == k:
                    return smallest
            previous_smallest = smallest
            smallest = None
            count = 0
        return -1
                