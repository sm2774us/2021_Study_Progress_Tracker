#
# Time : O(N); Space: O(1)
# @tag : Recursion ; DFS
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 200: Number of Islands
#
# Description:
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# **************************************************************************
# Source: https://leetcode.com/problems/number-of-islands/ (Leetcode - Problem 200 - Number of Islands)
#         https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1 (GeeksForGeeks - Find the number of islands)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.pdf.
#
#
from typing import List

import unittest


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0

        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                numIslands += self.dfs(grid, i, j)
        return numIslands

        paint(sr, sc)
        return image

    def dfs(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return 0

        grid[i][j] = "0"  # Make sunk so that we don't visit it again
        self.dfs(grid, i + 1, j)  # Down
        self.dfs(grid, i - 1, j)  # Up
        self.dfs(grid, i, j + 1)  # Right
        self.dfs(grid, i, j - 1)  # Left

        return 1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_numIslands_using_DFS_and_Recursion(self) -> None:
        s = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(1, s.numIslands(grid))
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(3, s.numIslands(grid))


if __name__ == "__main__":
    unittest.main()
