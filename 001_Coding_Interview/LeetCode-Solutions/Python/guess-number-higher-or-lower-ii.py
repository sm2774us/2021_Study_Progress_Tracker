# Time:  O(n^2)
# Space: O(n^2)

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        pay = [[0] * n for _ in range(n+1)]
        for i in reversed(range(n)):
            for j in range(i+1, n):
                pay[i][j] = min(k+1 + max(pay[i][k-1], pay[k+1][j]) \
                                for k in range(i, j+1))
        return pay[0][n-1]

