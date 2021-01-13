from typing import List
import collections

import unittest

# ---------------------------------------------------
# Utility functions for TEST CASES:
# ---------------------------------------------------
def createLinkedListFromMatrix(matrix: List[List[int]]) -> 'Node':
    if len(matrix) == 0:
        return None

    ((x, random_val), next_val) = ((matrix[0]), matrix[1][0])
    head = Node(x=x, next=Node(x=0) if next_val is not None else None, random=Node(x=0) if random_val is not None else None)
    if random_val is not None:
        head.random.val = random_val
    if next_val is not None:
        head.next.val = next_val
    cur = head

    for i in range(1, len(matrix)):
        if len(matrix[i]) == 0:
            continue
        if len(matrix) < i+1:
            cur.next = None
            cur = cur.next
        elif len(matrix) == i+1:
            ((x, random_val), next_val) = ((matrix[i]), None)
            cur.next = Node(x=x, next=Node(x=0) if next_val is not None else None, random=Node(x=0) if random_val is not None else None)
            if cur.next.random is not None:
                cur.next.random.val = random_val
            if cur.next.next is not None:
                cur.next.next.val = next_val
            cur = cur.next
        else:
            ((x, random_val), next_val) = ((matrix[i]), matrix[i + 1][0])
            cur.next = Node(x=x, next=Node(x=0) if next_val is not None else None, random=Node(x=0) if random_val is not None else None)
            if cur.next.random is not None:
                cur.next.random.val = random_val
            if cur.next.next is not None:
                cur.next.next.val = next_val
            cur = cur.next
    return head

def createMatrixFromLinkedList(head: 'Node') -> List[List[int]]:
    res = []

    while head is not None:
        res.append([head.val, head.random.val if head.random is not None else None])
        head = head.next
        #print(head)

    return res

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        lst = []
        p = self
        while p:
            lst.append([str(p.val), str(p.random.val) if p.random is not None else None])
            p = p.next

        return "->".join([' '.join([str(c) for c in el]) for el in lst])
        #return "[val={0} ; random={1}]  -> {2}".format(self.val, self.random.val if self.random is not None else None, self.next.val if self.next is not None else None)

class Solution:

    # # Approach #1. Hash
    # #
    # # Time: O(n); Space: O(n)
    # #
    # # @param head, a Node
    # # @return a Node
    # def copyRandomList_solution_1(self, head: Node) -> Node:
    #     """
    #     Given a head pointer to a linked with random pointers,
    #     this program creates a clone of the linked list using
    #     a hash table.
    #
    #     :param head: head pointer to given linked list with
    #                  random pointers
    #     :type head: Node
    #     :return: head pointer to clone of given linked list
    #     :rtype: Node
    #     """
    #
    #     """
    #     Base Case:
    #     - If given linked list has no nodes, return None.
    #     """
    #     if head is None:
    #         return None
    #
    #     """
    #     Create hash table and clone of linked list:
    #     - Create node_to_clone, a hash table that maps a node
    #       in the given linked list to its clone.
    #     - Create clone of the given linked list without the
    #       random pointers being defined.
    #     """
    #     node_to_clone = dict()
    #     node = head
    #     clone_head = Node(head.val)
    #     node_to_clone[head] = clone_head
    #     clone_node = clone_head
    #     while node.next:
    #         clone_node.next = Node(node.next.val)
    #         node = node.next
    #         clone_node = clone_node.next
    #         node_to_clone[node] = clone_node
    #
    #     """
    #     Add the random pointers to the linked list clone with
    #     the help of the hash table node_to_node.
    #     """
    #     node = head
    #     while node:
    #         if node.random:
    #             clone_node = node_to_clone[node]
    #             clone_node.random = node_to_clone[node.random]
    #         node = node.next
    #     return clone_head
    #
    # # Approach #2. Interleave
    # #
    # # Intuition :- You can easily use space(hashmap) and assign random pointers then. The core idea is to somehow accomodate random pointers with constant space. Now what we could do is somehow duplicate all nodes within the same linkedlist by putting all duplicates next to their original. What that will do is if the original's random pointer points to a node suppose 'n' then the duplicate's random will point to it's next node i.e 'n.next'. This is how we can remove the dependency on space for random pointer assignment.
    # #
    # # Algorithm :- The code is pretty intuitive
    # #
    # # Time: O(n); Space: O(n)
    # #
    # # @param head, a Node
    # # @return a Node
    # def copyRandomList_solution_2(self, head: Node) -> Node:
    #     # make copy of the list
    #     curr = head
    #     while (curr):
    #         store_next = curr.next
    #         curr.next = Node(curr.val, store_next)
    #         curr = store_next
    #
    #     # copy random pointer
    #     curr = head
    #     while (curr):
    #         next_node = curr.next
    #         next_node.random = curr.random.next if curr.random else None
    #         curr = curr.next.next
    #
    #     # extract the new list from the merged list
    #     new_head = None
    #     curr = head.next if head else None
    #     while (curr):
    #         if not new_head:
    #             new_head = curr
    #         if curr.next:
    #             new_curr = curr.next.next
    #             curr.next = curr.next.next
    #             curr = new_curr
    #         else:
    #             curr = curr.next
    #     return new_head

    def copyRandomList_solution_1(self, head: Node) -> Node:
        m, m[None], n = collections.defaultdict(lambda: Node(0, None, None)), None, head
        while n:
            m[n].val, m[n].next, m[n].random, n = n.val, m[n.next], m[n.random], n.next
        return m[head]

    def copyRandomList_solution_2(self, head: Node) -> Node:
        # Insert each node's copy right after it, already copy .label
        node = head
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next

        # Set each copy's .random
        node = head
        while node:
            node.next.random = node.random and node.random.next
            node = node.next.next

        # Separate the copied list from the original, (re)setting every .next
        node = head
        copy = head_copy = head and head.next
        while node:
            node.next = node = copy.next
            copy.next = copy = node and node.next

        return head_copy

    def copyRandomList_zip_copy_unzip_solution_3(self, head: 'Node') -> 'Node':
        # zip:
        src = head
        head = Node(0, src, None)
        while src:
            copy = Node(src.val, src.next, None)
            src.next = copy
            src = copy.next

        # random:
        src = head.next
        while src:
            src.next.random = src.random and src.random.next
            src = src.next.next

        # unzip:
        copy_tail = copy_head = Node(0, None, None)
        src = head.next
        while src:
            copy_tail.next = src.next   # append copy_node
            copy_tail = copy_tail.next
            src.next = src.next.next
            src = src.next
        return copy_head.next

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_copyRandomList(self) -> None:
        # Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        # Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
        #
        # Input: head = [[1,1],[2,1]]
        # Output: [[1,1],[2,1]]
        #
        # Input: head = [[3,null],[3,0],[3,null]]
        # Output: [[3,null],[3,0],[3,null]]
        #
        # Input: head = []
        # Output: []
        s = Solution()
        for head, solution in (
            [[[7,None],[13,0],[11,4],[10,2],[1,0]], [[7,None],[13,0],[11,0],[10,0],[1,0]]],
            [[[1,1],[2,1]], [[1,0],[2,0]]],
            [[[3,None],[3,0],[3,None]], [[3,None],[3,0],[3,None]]],
            [[],[]]
        ):
            self.assertEqual(
                solution,
                createMatrixFromLinkedList(s.copyRandomList_solution_1(createLinkedListFromMatrix(head)))
            )

        for head, solution in (
            [[[7,None],[13,0],[11,4],[10,2],[1,0]], [[7,None],[13,None],[11,None],[10,None],[1,None]]],
            [[[1,1],[2,1]], [[1,None],[2,None]]],
            [[[3,None],[3,0],[3,None]], [[3,None],[3,None],[3,None]]],
            [[],[]]
        ):
            # self.assertEqual(
            #     solution,
            #     createMatrixFromLinkedList(s.copyRandomList_solution_1(createLinkedListFromMatrix(head)))
            # )
            self.assertEqual(
                solution,
                createMatrixFromLinkedList(s.copyRandomList_solution_2(createLinkedListFromMatrix(head)))
            )
            self.assertEqual(
                solution,
                createMatrixFromLinkedList(s.copyRandomList_zip_copy_unzip_solution_3(createLinkedListFromMatrix(head)))
            )


if __name__ == "__main__":
    unittest.main()
