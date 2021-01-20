# Time:  O(2^n)
# Space: O(2^n)

class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        curr = range(10)
        for i in range(N-1):
            curr = [x*10 + y for x in curr for y in set([x%10 + K, x%10 - K]) 
                    if x and 0 <= y < 10]
        return curr
