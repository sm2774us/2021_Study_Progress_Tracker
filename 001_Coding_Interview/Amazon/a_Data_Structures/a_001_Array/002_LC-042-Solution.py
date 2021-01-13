#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# 42. Trapping Rain Water
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
# **************************************************************************
# Source: https://leetcode.com/problems/trapping-rain-water/ (Leetcode - Problem 42 - Trapping Rain Water)
#         https://practice.geeksforgeeks.org/problems/trapping-rain-water/0 (GeeksForGeeks - Trapping Rain Water)
#
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# Use Two Pointers to track the highest bar on left and right, respectively.
#
# - start check from both sides, move the point where wall is lower ( because taller wall may leak water on the
#   other lower side )
#
# - <leftmax> and <rightmax> are used to record the walls. If the land is lower than the wall, means it can hold water.
#
# - if a wall found taller than the max height wall on the other side, stop there (because taller wall may leak water
#   on the other lower side). Then move the lower side point.
#
from typing import List

import unittest


class Solution:
    # Time: O(n)
    # Space: O(1)
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        leftCursor, rightCursor = 0, len(height) - 1
        leftMax, rightMax, storedWater = 0, 0, 0

        while leftCursor <= rightCursor:
            leftMax = max(leftMax, height[leftCursor])
            rightMax = max(rightMax, height[rightCursor])
            if leftMax < rightMax:
                storedWater += leftMax - height[leftCursor]
                leftCursor += 1
            else:
                storedWater += rightMax - height[rightCursor]
                rightCursor -= 1

        return storedWater


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_trap(self) -> None:
        s = Solution()
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        trappedWater = s.trap(height)
        self.assertEqual(
            6,
            trappedWater,
            "Should compute how much water it is able to trap after raining",
        )


if __name__ == "__main__":
    unittest.main()
