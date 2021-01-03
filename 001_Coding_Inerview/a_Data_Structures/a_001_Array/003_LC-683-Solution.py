from typing import List

import unittest

class Solution:

    # TC: O(N)
    # SC: O(N)
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * len(flowers)
        for i in range(len(flowers)):
            days[flowers[i]-1] = i
        result = float("inf")
        i, left, right = 0, 0, k+1
        while right < len(days):
            if days[i] < days[left] or days[i] <= days[right]:
                if i == right:
                    result = min(result, max(days[left], days[right]))
                left, right = i, k+1+i;
            i += 1
        return -1 if result == float("inf") else result+1

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_kEmptySlots(self) -> None:
        sol = Solution()
        for flowers, k, solution in (
            [
                [1,3,2],
                1,
                2
            ],
            [
                [1,2,3],
                1,
                -1
            ]
        ):
            self.assertEqual(
                solution,
                sol.kEmptySlots(flowers, k)
            )


if __name__ == "__main__":
    unittest.main()
