import unittest

class Solution:
    # Solution Explanation:
    # --------------------------------------------------------------------------------
    # For those who are concerned, about complexity, this is still O(N) time and O(N) space.
    # Efficiency comes from Python comprehension and CPython function calls.
    #
    # The string join is a linear function.
    # But if we use string concatenation or string insert
    # which has O(n) complexity, iteratively, the time complexity becomes O(n^2).
    #
    # TC: O(N)
    # SC: O(N)
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_nextClosestTime(self) -> None:
        sol = Solution()
        for S, K, solution in (["5F3Z-2e-9-w", 4, "5F3Z-2E9W"], ["2-5g-3-J", 2, "2-5G-3J"]):
            self.assertEqual(
                solution,
                sol.licenseKeyFormatting(S, K)
            )

if __name__ == "__main__":
    unittest.main()
