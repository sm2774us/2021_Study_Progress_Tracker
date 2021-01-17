#
# Time : O(N); Space: O(N)
# @tag : Tree and BST ; Euler Tour ; Range Minimum Query Problem
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 426: Convert Binary Search Tree to Sorted Doubly Linked List
#
# Description:
#
# Convert a BST to a sorted circular doubly-linked list in-place.
# Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
#
# Examples:
# Refer to 002_LC-426-Problem_Description.md.
#
# **************************************************************************
# Source: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/ (Leetcode - Problem 426 - Convert Binary Search Tree to Sorted Doubly Linked List)
#         https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1 (GeeksForGeeks - Binary Tree to DLL)
#
# Solution Explanation
# **************************************************************************
# Youtube video: https://www.youtube.com/watch?v=MiHxSfY8Qyc
#
# Time: O(v), v is Number of nodes in the binary tree
# Space: O(v)
#
import unittest

# Definition for a Node.
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DoublyLinkedList:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

        # addNode() will add a node to the list

    def addNode(self, data):
        # Create a new node
        newNode = Node(data)

        # If list is empty
        if self.head == None:
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's left will point to None
            self.head.left = None
            # tail's right will point to None, as it is the last node of the list
            self.tail.right = None
        else:
            # newNode will be added after tail such that tail's right will point to newNode
            self.tail.right = newNode
            # newNode's left will point to tail
            newNode.left = self.tail
            # newNode will become new tail
            self.tail = newNode
            # As it is last node, tail's right will point to None
            self.tail.right = None

    # display() will print out the nodes of the list
    def display(self):
        # Node current will point to head
        current = self.head
        if self.head == None:
            # print("List is empty")
            return ""
        # print("Nodes of doubly linked list: ")
        dl_list = []
        while current != None:
            # Prints each node by incrementing pointer.
            # print(f"{current.val}<=>",end='')
            dl_list.append(f"{current.val}")
            current = current.right
        # print(*dl_list, sep="<=>")
        return "<=>".join([str(x) for x in dl_list])


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root: "Node") -> "Node":
        if not root:
            return root
        first, last = None, None

        def helper(node):
            nonlocal first, last
            if not node:
                return
            helper(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            helper(node.right)

        helper(root)
        first.left = last
        last.right = first
        return first


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_treeToDoublyList(self) -> None:
        s = Solution()
        root = Node(10)
        root.left = Node(12)
        root.left.left = Node(25)
        root.left.right = Node(30)
        root.right = Node(15)
        root.right.left = Node(36)
        solution = s.treeToDoublyList(root)
        dList = DoublyLinkedList()
        dList.addNode(solution.val)
        dList.addNode(solution.right.val)
        dList.addNode(solution.right.right.val)
        dList.addNode(solution.right.right.right.val)
        dList.addNode(solution.right.right.right.right.val)
        dList.addNode(solution.right.right.right.right.right.val)
        str = dList.display()
        # print(str)
        self.assertEqual("25<=>12<=>30<=>10<=>36<=>15", dList.display())
        root = Node(4)
        root.left = Node(2)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right = Node(5)
        solution = s.treeToDoublyList(root)
        dList = DoublyLinkedList()
        dList.addNode(solution.val)
        dList.addNode(solution.right.val)
        dList.addNode(solution.right.right.val)
        dList.addNode(solution.right.right.right.val)
        dList.addNode(solution.right.right.right.right.val)
        str = dList.display()
        # print(str)
        self.assertEqual("1<=>2<=>3<=>4<=>5", dList.display())
        root = Node(1)
        root.left = Node(3)
        root.right = Node(2)
        solution = s.treeToDoublyList(root)
        dList = DoublyLinkedList()
        dList.addNode(solution.val)
        dList.addNode(solution.right.val)
        dList.addNode(solution.right.right.val)
        str = dList.display()
        # print(str)
        self.assertEqual("3<=>1<=>2", dList.display())
        root = Node(10)
        root.left = Node(20)
        root.left.left = Node(40)
        root.left.right = Node(60)
        root.right = Node(30)
        solution = s.treeToDoublyList(root)
        dList = DoublyLinkedList()
        dList.addNode(solution.val)
        dList.addNode(solution.right.val)
        dList.addNode(solution.right.right.val)
        dList.addNode(solution.right.right.right.val)
        dList.addNode(solution.right.right.right.right.val)
        str = dList.display()
        # print(str)
        self.assertEqual("40<=>20<=>60<=>10<=>30", dList.display())


if __name__ == "__main__":
    unittest.main()
