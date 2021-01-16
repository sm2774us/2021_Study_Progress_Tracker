#
# Time : O(N+M)
# Space: O(N+M)
# @tag : Linked List, Two Pointers
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 2: Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
# **************************************************************************
# Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/ (LeetCode - Problem 19 - Remove Nth Node From End of List)
#         https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1 (GeeksForGeeks - Nth node from end of linked list)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# If you're struggling to visualize it, I think just drawing out a simple case would help. Say 1 + 1.
#
# Before loop:
# (0) -> None
#  ^
#  |
# root, n
#
# After 1 iteration of loop
#
# (0) -> (2) -> None
#  ^      ^
#  |      |
# root    n
# Now we want to return (2) -> None so we return root.next
#
import unittest

def createLinkedListFromArray(arr):
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head

    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head


def createArrayFromLinkedList(head):
    res = []

    while head != None:
        res.append(head.val)
        head = head.next

    return res

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        lst = []
        p = self
        while p:
            lst.append(str(p.val))
            p = p.next

        return "List: [{}].".format(",".join(lst))


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_addTwoNumbers(self) -> None:
        listNode = ListNode()
        s = Solution()
        for l1, l2, solution in (
            [
                [2, 4, 3],
                [5, 6, 4],
                [7, 0, 8],
            ],
            [
                [5, 4],
                [5, 4, 3],
                [0, 9, 3],
            ],
            [
                [3, 6],
                [7],
                [0, 7]
            ]
        ):
            self.assertEqual(
                solution,
                createArrayFromLinkedList(s.addTwoNumbers(createLinkedListFromArray(l1), createLinkedListFromArray(l2))),
                "Should return the sum of the 2 linked lists",
            )


if __name__ == "__main__":
    unittest.main()
