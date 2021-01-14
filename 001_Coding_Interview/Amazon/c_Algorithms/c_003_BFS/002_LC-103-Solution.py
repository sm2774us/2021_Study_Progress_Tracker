#
# Time : O(N); Space: O(N)
# @tag : Tree and BST
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 103: Binary Tree Zigzag Level Order Traversal
#
# Description:
#
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
# **************************************************************************
# Source: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/ (Leetcode - Problem 103 - Binary Tree Zigzag Level Order Traversal)
#         https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1 (GeeksForGeeks - Level order traversal in spiral form)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# This question is simply almost same as Binary Tree Level Order Treversal:https://leetcode.com/problems/binary-tree-level-order-traversal/
# ( refer to Tree_and_BST/006_leetcode_P_102_BinaryTreeLevelOrderTraversal/Solution.py )
#
# you just need to do [::-1] on odd elements for ans
#
# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         if not root: return []
#         q = deque([root])
#         ans = []
#         while q:
#             temp = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node.left: q.append(node.left)
#                 if node.right: q.append(node.right)
#                 temp.append(node.val)
#             ans.append(temp)
#         for i in range(1,len(ans),2):
#             ans[i] = ans[i][::-1]
#         return ans
#
# or,
#
# if current level is from left to right order, you append the node.val. (ex [node[0].val, node[1].val,node[2].val, node[3].val])
# if current level is from right to left, you appendleft the node.val. (ex. [node[3].val, node[2].val, node[1].val, node[0].val])
#
# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         ## APPROACH : BFS ##
#         ## Similar to Leetcode : 102. Binary Tree Level Order Traversal ##
#
#         ## TIME COMPLEXITY : O(N) ##
#         ## SPACE COMPLEXITY : O(N) ##
#         if not root:
#             return []
#
#         q = deque([root])
#         ans = []
#         isFromLeft = True
#         while q:
#             temp = deque()
#             for _ in range(len(q)):
#                 node = q.popleft()
#
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#                 ###########################
#                 if isFromLeft:
#                     temp.append(node.val)
#                 else:
#                     temp.appendleft(node.val)
#                 ##########################
#             # flip the order it after 1 level is complete
#             isFromLeft = not isFromLeft
#             ans.append(temp)
#         return ans
#
#
from typing import List
from collections import deque

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ## APPROACH : BFS ##
        ## Similar to Leetcode : 102. Binary Tree Level Order Traversal ##

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##
        if not root:
            return []

        q = deque([root])
        ans = []
        isFromLeft = True
        while q:
            temp = deque()
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                ###########################
                if isFromLeft:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
                ##########################
            # flip the order it after 1 level is complete
            isFromLeft = not isFromLeft
            # ans.append(temp)
            # Convert to list - makes it easier to unit test
            ans.append(list(temp))
        return ans

    def zigzagLevelOrderGeeksForGeeks(self, root: TreeNode) -> List[List[int]]:
        ## APPROACH : BFS ##
        ## Similar to Leetcode : 102. Binary Tree Level Order Traversal ##

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##
        if not root:
            return []

        q = deque([root])
        ans = []
        isFromLeft = False
        while q:
            temp = deque()
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                ###########################
                if isFromLeft:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
                ##########################
            # flip the order it after 1 level is complete
            isFromLeft = not isFromLeft
            # ans.append(temp)
            # Convert to list - makes it easier to unit test
            ans.append(list(temp))
        return ans


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_zigzagLevelOrderLeetCode(self) -> None:
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual([[3], [20, 9], [15, 7]], s.zigzagLevelOrder(root))

    def test_zigzagLevelOrderGeeksForGeeks(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(6)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(
            [[1], [2, 3], [4, 5, 6, 7]], s.zigzagLevelOrderGeeksForGeeks(root)
        )
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        self.assertEqual([[1], [3, 2]], s.zigzagLevelOrderGeeksForGeeks(root))
        root = TreeNode(10)
        root.left = TreeNode(20)
        root.left.left = TreeNode(40)
        root.left.right = TreeNode(60)
        root.right = TreeNode(30)
        self.assertEqual(
            [[10], [20, 30], [60, 40]], s.zigzagLevelOrderGeeksForGeeks(root)
        )


if __name__ == "__main__":
    unittest.main()
