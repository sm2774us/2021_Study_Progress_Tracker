#
# Time : O(N) ; Space: O(1)
# @tag : Tree and BST ; Recursion ;
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 297: Serialize and Deserialize Binary Tree
#
# Description:
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
# in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
# to a string and this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative and come up with different
# approaches yourself.
#
#
# Example 1:
#
# Given the following tree [1,2,3,null,null,4,5]:
#
#     1
#    / \
#   2   3
#     /  \
#    4    5
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
# Example 2:
#
# Input: root = []
# Output: []
#
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
# **************************************************************************
# Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/ (Leetcode - Problem 297 - Serialize and Deserialize Binary Tree)
#         https://practice.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1 (GeeksForGeeks - Serialize and Deserialize a Binary Tree)
#
from typing import List
from collections import deque

import json

import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Iterative - take advantage of deque O(1) popleft operation
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque()
        queue.append(p)
        queue.append(q)

        while queue:
            p, q = queue.popleft(), queue.popleft()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)

        return True

    # Iterative Solutions

    def serializeIterative(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def _serialize_level_order_helper(root):
            if root is None:
                return []
            q = deque()
            q.append(root)
            ret = []
            while q:
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    if node is not None:
                        ret.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                    else:
                        ret.append(None)
            return ret

        return json.dumps(_serialize_level_order_helper(root))

    def deserializeIterative(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        lst = json.loads(data)

        def _deserialize_level_order_helper(lst):
            # print(lst)
            if not lst:
                return None
            root = TreeNode(lst[0])
            level = deque([root])
            i = 1
            while i < len(lst):
                # print(i, level)
                node = level.popleft()

                if lst[i] is not None:
                    node.left = TreeNode(lst[i])
                    level.append(node.left)

                if lst[i + 1] is not None:
                    node.right = TreeNode(lst[i + 1])
                    level.append(node.right)
                # print(node)
                i += 2
            return root

        return _deserialize_level_order_helper(lst)

    # Recursive Solutions

    def serializeRecursive(self, root):
        def tuplify(root):
            return root and (root.val, tuplify(root.left), tuplify(root.right))

        return json.dumps(tuplify(root))

    def deserializeRecursive(self, data):
        def detuplify(t):
            if t:
                root = TreeNode(t[0])
                root.left = detuplify(t[1])
                root.right = detuplify(t[2])
                return root

        return detuplify(json.loads(data))


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_serialize(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(
            "[1, 2, 3, null, null, 4, 5, null, null, null, null]",
            s.serializeIterative(root),
        )
        self.assertEqual(
            "[1, [2, null, null], [3, [4, null, null], [5, null, null]]]",
            s.serializeRecursive(root),
        )
        root = TreeNode(None)
        self.assertEqual("[null, null, null]", s.serializeIterative(root))
        self.assertEqual("[null, null, null]", s.serializeRecursive(root))
        root = TreeNode(1)
        self.assertEqual("[1, null, null]", s.serializeIterative(root))
        self.assertEqual("[1, null, null]", s.serializeRecursive(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual("[1, 2, null, null, null]", s.serializeIterative(root))
        self.assertEqual("[1, [2, null, null], null]", s.serializeRecursive(root))

    def test_deserialize(self) -> None:
        s = Solution()
        expected = TreeNode(1)
        expected.left = TreeNode(2)
        expected.right = TreeNode(3)
        expected.right.left = TreeNode(4)
        expected.right.right = TreeNode(5)
        actual = s.deserializeIterative(
            "[1, 2, 3, null, null, 4, 5, null, null, null, null]"
        )
        self.assertEqual(True, s.isSameTree(expected, actual))
        actual = s.deserializeRecursive(
            "[1, [2, null, null], [3, [4, null, null], [5, null, null]]]"
        )
        self.assertEqual(True, s.isSameTree(expected, actual))
        expected = TreeNode(None)
        actual = s.deserializeIterative("[null, null, null]")
        self.assertEqual(True, s.isSameTree(expected, actual))
        actual = s.deserializeRecursive("[null, null, null]")
        self.assertEqual(True, s.isSameTree(expected, actual))
        expected = TreeNode(1)
        actual = s.deserializeIterative("[1, null, null]")
        self.assertEqual(True, s.isSameTree(expected, actual))
        actual = s.deserializeRecursive("[1, null, null]")
        self.assertEqual(True, s.isSameTree(expected, actual))
        expected = TreeNode(1)
        expected.left = TreeNode(2)
        actual = s.deserializeIterative("[1, 2, null, null, null]")
        self.assertEqual(True, s.isSameTree(expected, actual))
        actual = s.deserializeRecursive("[1, [2, null, null], null]")
        self.assertEqual(True, s.isSameTree(expected, actual))


if __name__ == "__main__":
    unittest.main()
