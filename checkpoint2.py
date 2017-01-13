class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        if A == 1:
            return [[1]]
        if A == 0:
            return []
        length = 2*A - 1
        ret = [[0 for column in xrange(length)] for row in xrange(length)]
        for i in xrange(length):
            for k in xrange(i, length - i):
                # Top row
                ret[i][k] = A - i
                # Right column
                ret[k][length-1-i]= A - i
                # Bottom row
                ret[length-1-i][k]= A - i
                # Left column
                ret[k][i] = A - i
        return ret
        