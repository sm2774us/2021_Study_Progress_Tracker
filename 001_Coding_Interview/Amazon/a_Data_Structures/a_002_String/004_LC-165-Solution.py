import itertools

import unittest

class Solution:
    # Solution 1 : Pad with itertools.zip_longest with fillvalue=0
    def compareVersion_solution_1(self, version1: str, version2: str) -> int:
        splits = (map(int, v.split('.')) for v in (version1, version2))
        for p1, p2 in itertools.zip_longest(*splits, fillvalue=0):
            if p1>p2: return 1
            elif p1<p2: return -1
        return 0

    # Solution 2 : Pad with [0] * lengthDifference
    #
    def compareVersion_solution_2(self, version1: str, version2: str) -> int:
        def cmp(a, b): return (a > b) - (a < b)
        v1, v2 = (list(map(int, v.split('.'))) for v in (version1, version2))
        d = len(v2) - len(v1)
        return cmp(v1 + [0]*d, v2 + [0]*-d)

    # Solution 3 : Iterative, add zeros on the fly
    def compareVersion_solution_3(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        for i in range(max(len(version1), len(version2))):
            p1 = int(version1[i]) if i<len(version1) else 0
            p2 = int(version2[i]) if i<len(version2) else 0
            if p1>p2: return 1
            elif p1<p2: return -1
        return 0

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_longestPalindrome(self) -> None:
        s = Solution()
        for version1, version2, solution in (
            ["1.01", "1.001", 0],
            ["1.0", "1.0.0", 0],
            ["0.1", "1.1", -1],
            ["1.0.1", "1", 1],
            ["7.5.2.4", "7.5.3", -1]
        ):
            self.assertEqual(
                solution,
                s.compareVersion_solution_1(version1, version2)
            )
            self.assertEqual(
                solution,
                s.compareVersion_solution_2(version1, version2)
            )
            self.assertEqual(
                solution,
                s.compareVersion_solution_3(version1, version2)
            )


if __name__ == "__main__":
    unittest.main()
