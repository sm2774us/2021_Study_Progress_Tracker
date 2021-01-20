# Time:  O(n^2)
# Space: O(n * d)

import collections


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        dp = [collections.defaultdict(int) for i in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result

