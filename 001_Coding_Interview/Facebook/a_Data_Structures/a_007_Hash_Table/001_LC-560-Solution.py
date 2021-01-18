from typing import List

import unittest

class Solution:
    # TC: O(N)
    # SC: O(1)

    #
    # Complexity Analysis:
    # * Time complexity : `O(N)`.
    #
    #   We traverse the list containing n elements once. Each look up in a hash table costs O(1) time.
    #   So `n` insertions and `n` lookups in a hash table takes expected time of `O(N)`.
    #
    # * Space complexity : `O(N)`.
    #
    #   The extra space required depends on the number of items stored in the dictionary,
    #   which stores at most n elements.
    #
    #
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = prefix = 0
        seen = {0:1}
        for num in nums:
            prefix += num #prefix sum
            ans += seen.get(prefix-k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
        return ans


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_subarraySum(self) -> None:
        sol = Solution()
        for nums, k, solution in ([[1,1,1], 2, 2], [[1,2,3], 3, 2]):
            self.assertEqual(
                sol.subarraySum(
                    nums, k
                ),
                solution
            )


if __name__ == "__main__":
    unittest.main()
