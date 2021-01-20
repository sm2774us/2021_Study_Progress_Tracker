# Time:  O(h * 2^n)
# Space: O(2^n)

class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        HAT_SIZE = 40
        hat_to_people = [[] for _ in range(HAT_SIZE)]
        for i in range(len(hats)):
            for h in hats[i]:
                hat_to_people[h-1].append(i)
        dp = [0]*(1<<len(hats))
        dp[0] = 1
        for people in hat_to_people:
            for mask in reversed(range(len(dp))):
                for p in people:
                    if mask & (1<<p):
                        continue
                    dp[mask | (1<<p)] += dp[mask]
                    dp[mask | (1<<p)] %= MOD
        return dp[-1]
