import unittest

class Solution:

    #
    # Two-pointer Solution
    #
    # TC: O(N)
    # SC: O(1)
    def backspaceCompare(self, S: str, T: str) -> bool:
        si = len(S) - 1
        ti = len(T) - 1
        skip1 = 0
        skip2 = 0

        while si > -1 or ti > -1:
            c1 = S[si] if si >= 0 else ""
            c2 = T[ti] if ti >= 0 else ""

            if c1 == "#":
                skip1 += 1
                si -= 1
                continue

            elif c2 == "#":
                skip2 += 1
                ti -= 1
                continue

            if skip1 > 0:
                si -= 1
                skip1 -= 1
                continue

            if skip2 > 0:
                ti -= 1
                skip2 -= 1
                continue

            if c1 != c2:
                return False

            si -= 1
            ti -= 1

        return si < 0 and ti < 0

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_backspaceCompare(self) -> None:
        sol = Solution()
        for S, T, solution in (["ab#c","ad#c",True],["ab##","c#d#",True],["a##c","#a#c",True],["a#c","b",False]):
            self.assertEqual(
                solution,
                sol.backspaceCompare(S,T)
            )


if __name__ == "__main__":
    unittest.main()
