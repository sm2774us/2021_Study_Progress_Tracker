# Time:  O(m * n * 2^n)
# Space: O(2^n)

# dp with rolling window
class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        total = 2**len(cost[0])
        dp = [[float("inf")]*total for _ in range(2)]
        dp[0][0] = 0
        for i in range(len(cost)):
            dp[(i+1)%2] = [float("inf")]*total
            for mask in range(total):
                base = 1
                for j in range(len(cost[0])):
                    dp[i%2][mask|base] = min(dp[i%2][mask|base], cost[i][j]+dp[i%2][mask])
                    dp[(i+1)%2][mask|base] = min(dp[(i+1)%2][mask|base], cost[i][j]+dp[i%2][mask])
                    base <<= 1
        return dp[len(cost)%2][-1]
