from typing import List
from operator import attrgetter
import heapq

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

def isEmpty(a):
    return all([isEmpty(b) for b in a]) if isinstance(a, list) else False

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

    # Solution 1 : Divide and Conquer
    #
    # This is the solution expected in an interview. However, the time-limit is exceeded, so prefer other 2 solutions.
    #
    # #1.
    # Think of divide and conquer technique
    #
    # #2.
    # Divide:
    # If k > 2 the n, in general case, keep dividing k lists into first half of size k/2, and second half of size k/2.
    #
    # #3.
    # Conquer:
    # When they return from base case k = 0 or k = 1, then start merging,
    # merging process is the same as we did in Leetcode #21 Merge Two Sorted Lists
    #
    # #4.
    # Finally, the merging result of first half and second half is the answer.
    #
    # TC: O(kN)
    #
    def mergeKLists_using_divide_and_conquer_solution_1(self, lists: List[ListNode]) -> ListNode:
        '''
        input: k sorted list
        output: merged result of k sorted list
        '''
        if not lists or isEmpty(lists):
            return None

        # ----------------------------------
        def merge(l1, l2) -> ListNode:
            '''
            input: two sorted list l1, l2
            output: merged sorted list
            '''

            dummy_head = ListNode('#')
            cur = dummy_head

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    cur, l1 = cur.next, l1.next
                else:
                    cur.next = l2
                    cur, l2 = cur.next, l2.next

            if l1:
                cur.next = l1
            else:
                cur.next = l2

            return dummy_head.next
        # ----------------------------------

        if not lists:
            # base case:
            # empty list
            return None

        elif len(lists) == 1:
            # base case:
            # only one list
            return lists[0]

        # general case:
        # divide-and-conquer

        # divide:
        mid = len(lists) // 2
        left = self.mergeKLists_using_divide_and_conquer_solution_1(lists[:mid])
        right = self.mergeKLists_using_divide_and_conquer_solution_1(lists[mid:])

        # conquer:
        return merge(left, right)

    # Solution 2 : Heap
    #
    # TC: O(N * logK) ; SC: O(K)
    #
    def mergeKLists_using_heap_solution_2(self, lists: List[ListNode]) -> ListNode:
        if not lists or isEmpty(lists):
            return None
        ## If two elements have the same val, the next tuple items will be compared:
        ## "i" in the below code, which is guaranteed to be unique.
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap != []:
            val, i, node = heap[0]
            if not node.next:  # exhausted one linked-list
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap, (node.next.val, i, node.next))  # recycling tie-breaker i guarantees uniqueness
            curr.next = node
            curr = curr.next
        return dummy.next

    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists_using_sort_solution_3(self, lists):
        if not lists or isEmpty(lists):
            return None
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        #sorted_list = sorted(sorted_list, key=attrgetter('val'))
        sorted_list = sorted(sorted_list, key=lambda x: x.val)
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_kClosest(self) -> None:
        sol = Solution()
        arr1 = [1, 4, 5]
        ll1 = createLinkedListFromArray(arr1)
        arr2 = [1, 3, 4]
        ll2 = createLinkedListFromArray(arr2)
        arr3 = [2, 6]
        ll3 = createLinkedListFromArray(arr3)
        ll = [ll1, ll2, ll3]
        # self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6],
        #                  createArrayFromLinkedList(sol.mergeKLists_using_divide_and_conquer_solution_1(ll)))
        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6],
                         createArrayFromLinkedList(sol.mergeKLists_using_heap_solution_2(ll)))
        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6],
                         createArrayFromLinkedList(sol.mergeKLists_using_sort_solution_3(ll)))

        # self.assertEqual([],
        #                  createArrayFromLinkedList(sol.mergeKLists_using_divide_and_conquer_solution_1([])))
        self.assertEqual([],
                         createArrayFromLinkedList(sol.mergeKLists_using_heap_solution_2([])))
        self.assertEqual([],
                         createArrayFromLinkedList(sol.mergeKLists_using_sort_solution_3([])))

        # self.assertEqual([],
        #                  createArrayFromLinkedList(sol.mergeKLists_using_divide_and_conquer_solution_1([[]])))
        self.assertEqual([],
                         createArrayFromLinkedList(sol.mergeKLists_using_heap_solution_2([[]])))
        self.assertEqual([],
                         createArrayFromLinkedList(sol.mergeKLists_using_sort_solution_3([[]])))


if __name__ == "__main__":
    unittest.main()
