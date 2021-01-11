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
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
# and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.
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
# Solution Explanation:
# **************************************************************************
# The idea is based on Connected-component labeling, two-pass algorithm.
# Then use a set to get number of distinct label sets (number of islands)
#
# **************************************************************************
# References:
# **************************************************************************
# https://en.wikipedia.org/wiki/Connected-component_labeling (Connected-component labeling AKA CCL)
#
# Connected-component labeling (CCL), connected-component analysis (CCA), blob extraction, region labeling,
# blob discovery, or region extraction is an algorithmic application of graph theory,
# where subsets of connected components are uniquely labeled based on a given heuristic.
#
from typing import List
from collections import defaultdict

import unittest

# disjoint-set node
class DsNode:
    def __init__(self):
        self.rank = 0
        self.parent = self


class DisjointSets:
    # DisjointSets Constructors and public methods.
    def __init__(self):
        self._sets = defaultdict(DsNode)

    def find(self, x):
        # path compression
        while x.parent is not x:
            x.parent = x.parent.parent
            x = x.parent
        return x

    def findByLabel(self, label):
        return self.find(self._sets[label])

    def unionByLabel(self, labelA, labelB):
        # union by rank
        a, b = self.find(self._sets[labelA]), self.find(self._sets[labelB])
        if a is not b:
            if a.rank > b.rank:
                b.parent = a
            else:
                a.parent = b
                if a.rank == b.rank:
                    b.rank += 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        if rows > 0:
            cols = len(grid[0])
            if cols > 0:
                ds = DisjointSets()
                labels, next_label = [[0] * cols for _ in range(rows)], 1
                for row in range(rows):
                    for col in range(cols):
                        if grid[row][col] == "1":
                            # land, check get north and west
                            north, west = row - 1, col - 1
                            if north >= 0:
                                # use label of north cell for now
                                labels[row][col] = labels[north][col]
                            if west >= 0 and grid[row][west] == "1":
                                if labels[row][col] == 0:
                                    # current cell not labeled, use label of west
                                    labels[row][col] = labels[row][west]
                                elif labels[row][col] != labels[row][west]:
                                    # labels of north and west are different, union the two labels
                                    ds.unionByLabel(labels[row][col], labels[row][west])
                            if labels[row][col] == 0:
                                # current cell not labeled: must be an isolated cell. Use next label
                                labels[row][col] = next_label
                                next_label += 1
                node_set = set()
                for label in range(1, next_label):
                    node_set.add(ds.findByLabel(label))
                return len(node_set)

        return 0


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_numIslands_using_UnionFind(self) -> None:
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
