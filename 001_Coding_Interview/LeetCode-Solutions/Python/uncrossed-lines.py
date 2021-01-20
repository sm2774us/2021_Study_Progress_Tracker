# Time:  O(m * n)
# Space: O(min(m, n))

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) < len(B):
            return self.maxUncrossedLines(B, A)

        dp = [[0 for _ in range(len(B)+1)] for _ in range(2)]
        for i in range(len(A)):
            for j in range(len(B)):
                dp[(i+1)%2][j+1] = max(dp[i%2][j] + int(A[i] == B[j]),
                                       dp[i%2][j+1],
                                       dp[(i+1)%2][j])
        return dp[len(A)%2][len(B)]
