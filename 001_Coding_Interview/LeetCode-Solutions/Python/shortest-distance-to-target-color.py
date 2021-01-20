# Time:  O(n)
# Space: O(n)

class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dp = [[-1 for _ in range(len(colors))] for _ in range(3)]
        dp[colors[0]-1][0] = 0
        for i in range(1, len(colors)):
            for color in range(3):
                dp[color][i] = dp[color][i-1]
            dp[colors[i]-1][i] = i

        dp[colors[len(colors)-1]-1][len(colors)-1] = len(colors)-1
        for i in reversed(range(len(colors)-1)):
            for color in range(3):
                if dp[color][i+1] == -1:
                    continue
                if dp[color][i] == -1 or \
                   abs(dp[color][i+1]-i) < abs(dp[color][i]-i):
                    dp[color][i] = dp[color][i+1]
            dp[colors[i]-1][i] = i
         
        return [abs(dp[color-1][i]-i) if dp[color-1][i] != -1 else -1 \
                    for i, color in queries]
