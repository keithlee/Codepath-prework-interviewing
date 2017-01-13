"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example: 
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if A == None or len(A) == 0:
            return 0
        d = {}
        max_sequence = 1
        for n in A:
            d[n] = 1
        for key, value in d.iteritems():
            if value == 1:
                down = key - 1
                up = key + 1
                sequence = 1
                while down in d:
                    sequence += 1
                    d[down] = 0 #skip in future
                    down -= 1
                while up in d:
                    sequence += 1
                    d[up] = 0 #skip in future
                    up += 1
                if sequence > max_sequence:
                    max_sequence = sequence
        return max_sequence
                    
                
                