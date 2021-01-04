from typing import List
from math import ceil

import heapq

import unittest

def round_up(num, n):
    multiplier = pow(10,n)
    return ceil(num * multiplier) / multiplier

class Solution:

    #
    # Solution 1: Sorted Wage/Quality and Max Heap
    #
    # Suppose we have a team of two workers (w1, q1), (w2, q2). What we need to pay is
    #   max(w1, q1*w2/q2) + max(w2, q2*w1/q1).
    # And
    #   w1 = q1*w1/q1,
    #   w2 = q2*w2/q2.
    # So the cost is
    #   q1*max(w1/q1,w2/q2) + q2*max(w1/q1,w2/q2) = max(w1/q1,w2/q2) * (q1+q2)
    #
    # So generally, a team cost is
    #   ∑wi = w/q * ∑qi
    # where, w/q is the maximum wage/quality ratio in that team.
    # Thus, to find minimal wage to pay for a k-workers team, we need to:
    #   minimize w/q and ∑qi.
    #
    # So we can iterate a sorted team with the order of w/q, and keep retain k workers
    # who have the lowest qualities. (what a sarcasm that worker with high quality raises
    # wage bar so he/she can't be hired...).
    #
    # We can use a maximum heap to retain k lowest qualities. Once team size reaches K,
    # we update our cost as min(cost, w/q * ∑qi). Once team size exceed K,
    # we pop the highest quality and remove that quality from ∑qi.
    # I used two variable ratio and sumq for w/q and ∑qi.
    #
    # ratio keeps increase as we iterate in a sorted array and heap always retains k
    # lowest qualities under current ratio so we won't miss the lowest cost.
    #
    # Trick : When popping the highest quality in the team, we observed that even if the popped worker is the
    #         one we just added, the cost will always remain the same because the ratio is in ascending order.
    #         To be more precise, in this case,
    #         in the expression: min(cost, sumq * ratio),
    #         sumq == cost
    #         and
    #         ratio is bigger than the one which is used to calculate the cost
    #
    # Both sorting takes O(nlogn) and iteration takes O(nlogK). So time complexity is O(nlogn) and space complexity is O(K).
    #
    # TC: O(N*log(N))
    # SC: O(K)
    #
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = sorted((w / q, w, q) for w, q in zip(wage, quality))
        cost, team, sumq = float('inf'), [], 0
        for ratio, w, q in workers:
            heapq.heappush(team, -q)
            sumq += q
            if len(team) > K: sumq += heapq.heappop(team)
            if len(team) == K: cost = min(cost, sumq * ratio)
        return cost

    #
    # Solution 1: Sorted Wage/Quality and Max Heap - Long Version
    #
    # TC: O(N*log(N))
    # SC: O(K)
    #
    def mincostToHireWorkers_long_version(self, quality: List[int], wage: List[int], K: int) -> float:
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        worker_ratios = []
        n = len(quality)

        # For each worker, store the pair of
        # 1. ratio of wage to quality and
        # 2. quality
        for i in range(n):
            ratio = float(wage[i]) / float(quality[i])
            worker_ratios.append((ratio, quality[i]))

        # Sort the ratios so that we start at min wage to
        # quality and go up while calculating total cost
        worker_ratios.sort()

        # Heap h stores the max qualities encountered so far
        h = []
        # total_quality stores the total of qualities currently stored in the max heap
        total_quality = 0
        # Final result is stored here
        #min_cost = sys.maxsize
        min_cost = float('inf')

        for ratio, qual in worker_ratios:
            total_quality += qual

            # Store negative of quality for max heap
            heapq.heappush(h, -qual)

            if len(h) > K:
                # Storing negative values for quality
                # so, on popping max value, we get quality to subtract
                # from current total quality
                quality_to_remove = heapq.heappop(h)
                total_quality += quality_to_remove

            if len(h) == K:
                # If there are current K items in max
                # heap of qualities, calculate the
                # cost to hire these workers at rate of
                # current worker's ratio. Because the ratios are sorted
                # we are here trying to get min cost for max quality
                cost = total_quality * ratio
                min_cost = min(min_cost, cost)

        return min_cost

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_mincostToHireWorkers_without_rounding(self) -> None:
        sol = Solution()
        for quality, wage, K, solution in (
            [
                [10,20,5],
                [70,50,30],
                2,
                105.00000                             # Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
            ],
            [
                [3,1,10,10,1],
                [4,8,2,2,7],
                3,
                30.666666666666664                    # Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers separately.
            ]
        ):
            self.assertEqual(
                solution,
                sol.mincostToHireWorkers(quality, wage, K)
            )
            self.assertEqual(
                solution,
                sol.mincostToHireWorkers_long_version(quality, wage, K)
            )

    def test_mincostToHireWorkers(self) -> None:
        sol = Solution()
        for quality, wage, K, solution in (
            [
                [10,20,5],
                [70,50,30],
                2,
                105.00000                   # Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
            ],
            [
                [3,1,10,10,1],
                [4,8,2,2,7],
                3,
                30.66667                    # Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers separately.
            ]
        ):
            self.assertEqual(
                solution,
                round_up(sol.mincostToHireWorkers(quality, wage, K),5)
            )
            self.assertEqual(
                solution,
                round_up(sol.mincostToHireWorkers_long_version(quality, wage, K),5)
            )

if __name__ == "__main__":
    unittest.main()
