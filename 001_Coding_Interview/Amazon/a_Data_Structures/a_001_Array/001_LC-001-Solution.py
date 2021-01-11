from typing import List

import unittest

class Solution:

    # Solution 1 : Brute Force
    #              (nested loop get all combination of two numbers)
    #
    # TC: O(N^2)    : because there is only n * (n - 1) / 2 combinations
    # SC: O(1)      : we occupy no extra space in memory
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        for i in range(len(nums) - 1):
            firstNum = nums[i]
            for j in range(i+1, len(nums)):
                secondNum = nums[j]
                if firstNum + secondNum == target:
                    return [i, j]
        return []

    # Solution 2 : Dictionary
    #              ( one pass, store and find target - nums[i] same time )
    # TC: O(N)
    # SC: O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        seen = {}
        for i, value in enumerate(nums):  # 1
            remaining = target - nums[i]  # 2

            if remaining in seen:  # 3
                return [seen[remaining], i]  # 4
            else:
                seen[value] = i  # 5

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_twoSum(self) -> None:
        s = Solution()
        for nums, target, solution in (
                [[2, 7, 11, 15], 9, [0, 1]],  # Because nums[0] + nums[1] == 9, we return [0, 1].
                [[3, 2, 4], 6, [1, 2]],
                [[3, 3], 6, [0, 1]],
                [[1, 4, 2, 0], 3, [0, 2]],
                [[3, 5, -4, 8, 11, 1, -1, 6], 10, [4, 6]]
        ):
            self.assertEqual(solution, s.twoSum_brute_force(nums, target))
            self.assertEqual(solution, s.twoSum(nums, target))

if __name__ == "__main__":
    unittest.main()
