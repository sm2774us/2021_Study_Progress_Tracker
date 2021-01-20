# Time:  O(n^3)
# Space: O(n^2)

class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for p in range(3, len(A)+1):
            for i in range(len(A)-p+1):
                j = i+p-1;
                dp[i][j] = float("inf")
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j] + A[i]*A[j]*A[k])
        return dp[0][-1]
