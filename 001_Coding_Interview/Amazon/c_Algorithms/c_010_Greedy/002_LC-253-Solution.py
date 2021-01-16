#
# Time : O(n log n)
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 253: Meeting Rooms II
#
# Description:
#
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# **************************************************************************
# Examples
# **************************************************************************
# **************************************************************************
# Example 1:
# **************************************************************************
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# **************************************************************************
# Example 2:
# **************************************************************************
# Input: [[7,10],[2,4]]
# Output: 1
#
# **************************************************************************
# Source: https://leetcode.com/problems/meeting-rooms-ii/ (LeetCode - Problem 253 - Meeting Rooms II)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List

import unittest


class Solution(object):
    def minMeetingRooms(self, intervals: List[int]) -> int:
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        startTimes = [i[0] for i in intervals]
        endTimes = [i[1] for i in intervals]
        startTimes = sorted(startTimes)
        endTimes = sorted(endTimes)
        rooms = 0
        while len(startTimes) > 0:
            startTime = startTimes.pop(0)
            # now a meeting is going to start, is there a meeting ends
            # (meaning a meeting room is released)?
            endTime = endTimes[0]
            if endTime <= startTime:
                endTimes.pop(0)
            else:
                # need to ask for a new room
                rooms += 1
        return rooms


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minMeetingRooms(self) -> None:
        sol = Solution()
        for intervals, solution in (
            [[[0, 30], [5, 10], [15, 20]], 2],
            [[[7, 10], [2, 4]], 1],
        ):
            self.assertEqual(solution, sol.minMeetingRooms(intervals))


# main
if __name__ == "__main__":
    unittest.main()
