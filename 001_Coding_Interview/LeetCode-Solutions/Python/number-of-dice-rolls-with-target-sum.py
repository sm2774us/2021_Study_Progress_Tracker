# Time:  O(d * f * t)
# Space: O(t)

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0 for _ in range(target+1)] for _ in range(2)]
        dp[0][0] = 1
        for i in range(1, d+1):
            dp[i%2] = [0 for _ in range(target+1)]
            for k in range(1, f+1):
                for j in range(k, target+1):
                    dp[i%2][j] = (dp[i%2][j] + dp[(i-1)%2][j-k]) % MOD
        return dp[d%2][target] % MOD
