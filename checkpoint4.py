"""
Given an array, find the next greater element G[i] for every element A[i] in the array. 
The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. 
More formally,
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        ret = [-1] * len(A)
        for i in xrange(len(A)):
            for n in A[i:]:
                if n > A[i]:
                    ret[i] = n
                    break
        return ret
                