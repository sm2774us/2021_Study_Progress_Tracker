# Time:  O(n)
# Space: O(1)

import operator


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums, \
                      reduce(operator.xor, range(len(nums) + 1)))


class Solution2(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)

