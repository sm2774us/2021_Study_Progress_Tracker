from typing import List
import collections
import heapq

import unittest

class Solution:
    def inverse(self, num):
        return -1 * num

    #
    # Solution 1:
    #
    # Task Scheduler https://leetcode.com/problems/task-scheduler/description/
    #
    # ##Algorithm##
    #
    # This is an extremely tricky problem.
    # The main idea is to schedule the most frequent tasks as frequently as possible. Begin with scheduling the most frequent task. Then cool-off for n, and in that cool-off period schedule tasks in order of frequency, or if no tasks are available, then be idle.
    # Exampe: Say we have the following tasks: [A,A,A,B,C,D,E] with n =2
    # Now if we schedule using the idea of scheduling all unique tasks once and then calculating if a cool-off is required or not, then we have: A,B,C,D,E,A,idle,dile,A i.e. 2 idle slots.
    # But if we schedule using most frequent first, then we have:
    # 2.1: A,idle,idle,A,idle,idle,A
    # 2.2: A,B,C,A,D,E,A i.e. no idle slots. This is the general intuition of this problem.
    # 3.The idea in two can be implemented using a heap and temp list. This is illustrated in the code below.
    # 4.Time complexity is O(N * n) where N is the number of tasks and n is the cool-off period.
    # 5.Space complexity is O(1) - will not be more than O(26).
    #
    # TC: O(N * n)  - where N is the number of tasks and n is the cool-off period.
    # SC: O(1)      - will not be more than O(26)
    #
    def leastInterval_solution_1(self, tasks: List[str], n: int) -> int:
        # What are the inputs here
        #   - tasks - a list of strings the represent information we're processing
        #   - n - the time between tasks of the exact same time. This would leave us room to process other tasks
        # we asking for here?
        #   - We're looking for an int as an output. That's because we're returning a count
        #   - We're looking for the minimum number of intervals that we're going to use for the problem

        # How I think we're going to solve the problem
        # 1. We process the most important tasks often
        #   - That's because we want to process everything quickly, and processing it quickly means processing the most frequent tasks immediately after the cooldown time is over is necessary.
        # 2. Determine my interval
        #   - I want to be able to determine what step I'm at
        # 3. Create a dict of counts since I last processed my task

        # Task map to store if we've seen the item before
        task_count = collections.Counter(tasks)
        current_time = 0
        current_heap = []

        # Sorting from least to greatest inside of the heap current_heap
        for k, v in task_count.items():
            heapq.heappush(current_heap,
                     (self.inverse(v), k))  # Pushes item from least to greatest (hence the negative values)

        # Here we're running through the entire heap and processing the sorted tasks
        while current_heap:  # We're running until this list runs out because we intend to pop elements from it
            index, temp = 0, []
            while index <= n:
                current_time += 1  # We're counting the interval time here
                if current_heap:
                    timing, taskid = heapq.heappop(current_heap)
                    # We're checking to see if it's at the end of the overall count.
                    # Remember that it was negative at the beginning
                    if timing != -1:
                        # if current element does not used out this time, so there could be idles
                        # and it cannot be used again in this n+1 space, so removed to temp and add back later
                        # we can add all left idles if no h but have temp, to improve time complexity.
                        temp.append((timing + 1, taskid))
                # Checking to see if we're out of tasks. Exit the inner loop if both are true.
                # This will automatically exit out of the overall tasks
                if not current_heap and not temp:
                    break
                else:
                    index += 1
            # Because we transfered all of the items from the heap to temp, we're transferring them back to know if we should continue
            # heap -> If we're not out of tasks -> temp
            # temp -> Because we're not out -> heap
            for item in temp:
                heapq.heappush(current_heap, item)
            # We only stop if we're out of tasks
            # (Constantly checking the current_heap for if it's empty)
        return current_time

    #
    # Solution 2:
    #
    # Task Scheduler https://leetcode.com/problems/task-scheduler/description/
    #
    # ##Algorithm##
    #
    # O(n) # of the most frequent tasks, say longest, will determine the legnth
    # to void counting idle intervals, we count (longest - 1) * (n + 1)
    # then count how many will in the last cycle which means finding ties
    # if counted number is less than # of tasks which means
    # less frequent tasks can be always placed in such cycle
    # and it won't cause any conflicts with requirement since even most frequent can be settle
    # finally, return max(# of task, total counted number)
    #
    def leastInterval_solution_2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = collections.defaultdict(int)
        for t in tasks:
            c[t] += 1
        m = max(c.values())
        l = len([k for k in c if c[k] == m])
        return max(len(tasks), (m - 1) * (n + 1) + l)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_lruCache(self) -> None:
        sol = Solution()
        for tasks, n, solution in (
            [
                ["A","A","A","B","B","B"],
                2,
                8,
            ],
            [
                ["A","A","A","B","B","B"],
                0,
                6
            ],
            [
                ["A","A","A","A","A","A","B","C","D","E","F","G"],
                2,
                16
            ]
        ):
            self.assertEqual(
                sol.leastInterval_solution_1(
                    tasks, n
                ),
                solution,
            )
            self.assertEqual(
                sol.leastInterval_solution_2(
                    tasks, n
                ),
                solution,
            )


if __name__ == "__main__":
    unittest.main()
