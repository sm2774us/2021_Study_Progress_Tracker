# Time:  O(n^2)
# Space: O(n^2)

import collections


class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        count = collections.Counter()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                result += count[nums[i]*nums[j]]
                count[nums[i]*nums[j]] += 1
        return 8*result
