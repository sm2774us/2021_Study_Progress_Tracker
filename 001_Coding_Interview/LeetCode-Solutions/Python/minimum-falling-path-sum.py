# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                A[i][j] += min(A[i-1][max(j-1, 0):j+2])
        return min(A[-1])
