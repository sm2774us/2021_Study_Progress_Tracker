#
# Time : O(log N); Space: O(1)
# @tag : Heap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 295: Find Median from Data Stream
#
# Description:
#
# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# For example,
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
#
#
# Example:
#
#   addNum(1)
#   addNum(2)
#   findMedian() -> 1.5
#   addNum(3)
#   findMedian() -> 2
#
# Follow up:
#
#   1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
#   2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
#
# **************************************************************************
# Source: https://leetcode.com/problems/find-median-from-data-stream/ (Leetcode - Problem 295 - Find Median from Data Stream)
#         https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0 (GeeksForGeeks - Find median in a stream)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# I keep two heaps (or priority queues):
#
# Max-heap small has the smaller half of the numbers.
# Min-heap large has the larger half of the numbers.
# This gives me direct access to the one or two middle values (they're the tops of the heaps),
# so getting the median takes O(1) time. And adding a number takes O(log n) time.
#
# Supporting both min- and max-heap is more or less cumbersome,
# depending on the language, so I simply negate the numbers in the heap in which I want the
# reverse of the default order. To prevent this from causing a bug with -231
# (which negated is itself, when using 32-bit ints), I use integer types larger than 32 bits.
#
# Using larger integer types also prevents an overflow error when taking the mean of the two
# middle numbers. I think almost all solutions posted previously have that bug.
#
# **************************************************************************
# Detailed Explanation :
# **************************************************************************
# The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of smaller half is kept to be n / 2 at all time and the length of the larger half is either n / 2 or n / 2 + 1 depend on n's parity.
#
# This way we only need to peek the two heaps' top number to calculate median.
#
# Any time before we add a new number, there are two scenarios, (total n numbers, k = n / 2):
#
# (1) length of (small, large) == (k, k)
# (2) length of (small, large) == (k, k + 1)
# After adding the number, total (n + 1) numbers, they will become:
#
# (1) length of (small, large) == (k, k + 1)
# (2) length of (small, large) == (k + 1, k + 1)
# Here we take the first scenario for example, we know the large will gain one more item and small will remain the same size, but we cannot just push the item into large. What we should do is we push the new number into small and pop the maximum item from small then push it into large (all the pop and push here are heappop and heappush). By doing this kind of operations for the two scenarios we can keep our invariant.
#
# Therefore to add a number, we have 3 O(log n) heap operations. Luckily the heapq provided us a function "heappushpop" which saves some time by combine two into one. The document says:
#
# Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
# Alltogether, the add operation is O(logn), The findMedian operation is O(1).
#
# Note that the heapq in python is a min heap, thus we need to invert the values in the smaller half to mimic a "max heap".
#
# A further observation is that the two scenarios take turns when adding numbers, thus it is possible to combine the two into one. For this please see stefan's post
# **************************************************************************
#
#
from heapq import *

import unittest


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        # small - the smaller half of the list, max heap (invert min-heap)
        # large - the larger half of the list, min heap
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findMedian(self) -> None:
        medianFinder = MedianFinder()
        medianFinder.addNum(2)
        medianFinder.addNum(3)
        medianFinder.addNum(4)
        self.assertEqual(3, medianFinder.findMedian())
        medianFinder = MedianFinder()
        medianFinder.addNum(2)
        medianFinder.addNum(3)
        self.assertEqual(2.5, medianFinder.findMedian())
        medianFinder = MedianFinder()
        medianFinder.addNum(1)
        medianFinder.addNum(2)
        self.assertEqual(1.5, medianFinder.findMedian())


if __name__ == "__main__":
    unittest.main()
