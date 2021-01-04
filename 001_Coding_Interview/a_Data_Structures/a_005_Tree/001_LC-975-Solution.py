from typing import List

import unittest

class BstNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"key:{self.key} value:{self.value}"


class BstTree:
    def __init__(self):
        self.root = None

    def get(self, key):
        return self.search(key, self.root)

    def search(self, key, node):  # return (leaf_node or match node, l_neigh, r_neigh)
        l_neigh = None
        r_neigh = None
        s_node = None

        if not node:
            return s_node, l_neigh, r_neigh
        else:
            if node.key > key:  # left side
                r_neigh = node
                if node.left is None:
                    s_node = node
                else:
                    c_node, c_l, c_r = self.search(key, node.left)
                    s_node = c_node
                    if c_l is not None:
                        l_neigh = c_l
                    if c_r is not None:
                        r_neigh = c_r

            elif node.key < key:  # right side
                l_neigh = node
                if node.right is None:
                    s_node = node
                else:
                    c_node, c_l, c_r = self.search(key, node.right)
                    s_node = c_node
                    if c_l is not None:
                        l_neigh = c_l
                    if c_r is not None:
                        r_neigh = c_r
            else:
                s_node = node
                if node.right is not None:
                    c_node, c_l, c_r = self.search(key, node.right)
                    if c_r is not None:
                        r_neigh = c_r
                if node.left is not None:
                    c_node, c_l, c_r = self.search(key, node.left)
                    if c_l is not None:
                        l_neigh = c_l

        return s_node, l_neigh, r_neigh

    def update(self, key, value):
        node, l, r = self.get(key)
        if not node:
            self.root = BstNode(key, value)
        else:
            if node.key == key:
                node.value = value
            elif node.key < key:
                node.right = BstNode(key, value)
            else:
                node.left = BstNode(key, value)

class Solution:

    # Solution 1: Stack-based Solution
    #
    # Time O(NlogN)
    # Space O(N)
    #
    def oddEvenJumps_using_stack(self, A: List[int]) -> int:

        # sort indexes of A by values in A
        sorted_indexes = sorted(range(len(A)), key=lambda i: A[i])

        # generate list of indexes we can jump to next on odd jumps
        oddnext = self.makeStack(sorted_indexes)

        # sort indexes of A by reverse order of their value in A
        sorted_indexes.sort(key=lambda i: A[i], reverse=True)

        # generate list of indexes we can jump to next on even jumps
        evennext = self.makeStack(sorted_indexes)

        # initialize odd and even lists that will contain
        # the information of if the end can be reached
        # from the respective index
        odd = [False] * len(A)
        even = [False] * len(A)

        # the last index is always counted
        odd[len(A) - 1] = even[len(A) - 1] = True

        # iterate through A backwards, starting at next to last element
        for i in range(len(A) - 2, -1, -1):

            # if an odd jump is available from current index,
            # check if an even jump landed on the index of the available
            # odd jump and set current index in odd to True if it did
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]

            # if an even jump is available from current index,
            # check if an odd jump landed on the index of the available
            # even jump and set current index in even to True if it did
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        # return the number of spots marked True in odd
        # we always start with an odd jump, so odd will
        # contain the number of valid jumps to reach the end
        return sum(odd)

    # makes monotonic stack
    def makeStack(self, sorted_indexes):
        result = [None] * len(sorted_indexes)
        stack = []
        for i in sorted_indexes:
            while stack and i > stack[-1]:
                result[stack.pop()] = i
            stack.append(i)
        # delete stack as a memory optimization
        del stack
        return result

    # Solution 2: BST-based Solution
    #
    # We perform a single pass from right to left, and as we insert each node we also compute the "next higher" and "next lower" indices. Since insertion is O(log n), complexity is O(n log n).
    #
    # Node is a normal BST implementation with two twists:
    #
    # It stores value and index, and when inserting an existing value we just override the index
    # insert() returns the index of in-order predecessor and in-order successor
    #
    # Time O(NlogN)
    # Space O(N)
    #
    # def oddEvenJumps_using_BST(self, A: List[int]) -> int:
    #     n = len(A)
    #     root = Node(A[-1], n - 1)
    #     higher, lower = [0] * n, [0] * n
    #     higher[n - 1], lower[n - 1], num_good = 1, 1, 1
    #     for i in reversed(range(n-1)):
    #         lower[i], higher[i] = root.insert(A[i], i)
    #         if higher[i]:
    #             higher[i] = lower[higher[i]]
    #         if lower[i]:
    #             lower[i] = higher[lower[i]]
    #             num_good += higher[i]
    #     return num_good
    def oddEvenJumps_using_BST(self, A: List[int]) -> int:
        if not A:
            return 0

        if len(A) == 1:
            return 1

        bst = BstTree()

        h_j = [0] * len(A)
        l_j = [0] * len(A)

        for i in reversed(range(len(A))):
            n, l, r = bst.get(A[i])
            if n is None:
                h_j[i] = i
                l_j[i] = i
            elif n.key == A[i]:  # found same value
                h_j[i] = n.value
                l_j[i] = n.value
            elif n.key < A[i]:
                l_j[i] = n.value
                if r is None:
                    h_j[i] = i
                else:
                    h_j[i] = r.value
            else:  # n.key > A[i]:
                h_j[i] = n.value
                if l is None:
                    l_j[i] = i
                else:
                    l_j[i] = l.value

            bst.update(A[i], i)

        count = 0

        for i in range(len(A) - 1, -1, -1):
            if h_j[i] != i:
                h_j[i] = l_j[h_j[i]]
            if l_j[i] != i:
                l_j[i] = h_j[l_j[i]]

            if h_j[i] == len(A) - 1:
                count += 1

        return count

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_oddEvenJumps(self) -> None:
        sol = Solution()
        for A, solution in ([[10,13,12,14,15],2],[[2,3,1,1,4],3],[[5,1,3,4,2],3]):
            self.assertEqual(
                solution,
                sol.oddEvenJumps_using_stack(A)
            )
            self.assertEqual(
                solution,
                sol.oddEvenJumps_using_BST(A)
            )


if __name__ == "__main__":
    unittest.main()
