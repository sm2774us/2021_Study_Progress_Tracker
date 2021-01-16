from typing import List
from functools import lru_cache

import unittest

class Solution:
    #
    # SOLUTION-1
    #
    ## APPROACH : BACK-TRACKING ##
    ## Similar to Leetcode 32. Longest Valid Parentheses ##
    ## LOGIC ##
    #   1. use stack to find invalid left and right braces.
    #   2. if its close brace at index i , you can remove it directly to make it valid and also you can also remove any of the close braces before that i.e in the range [0,i-1]
    #   3. similarly for open brace, left over at index i, you can remove it or any other open brace after that i.e [i+1, end]
    #   4. if left over braces are more than 1 say 2 close braces here, you need to make combinations of all 2 braces before that index and find valid parentheses.
    #   5. so, we count left and right invalid braces and do backtracking removing them
    #
    ## TIME COMPLEXITY : O(2^N) ## (each brace has 2 options: exits or to be removed)
    ## SPACE COMPLEXITY : O(N) ##
    def removeInvalidParentheses_using_backtracking_solution_1(self, s: str) -> List[str]:

        def isValid(s):
            stack = []
            for i in range(len(s)):
                if (s[i] == '('):
                    stack.append((i, '('))
                elif (s[i] == ')'):
                    if (stack and stack[-1][1] == '('):
                        stack.pop()
                    else:
                        stack.append((i, ')'))  # pushing invalid close braces also
            return len(stack) == 0, stack

        def dfs(s, left, right):
            visited.add(s)
            if left == 0 and right == 0 and isValid(s)[0]:  res.append(s)
            for i, ch in enumerate(s):
                if ch != '(' and ch != ')': continue  # if it is any other char ignore.
                if (ch == '(' and left == 0) or (
                        ch == ')' and right == 0): continue  # if left == 0 then removing '(' will only cause imbalance. Hence, skip.
                if s[:i] + s[i + 1:] not in visited:
                    dfs(s[:i] + s[i + 1:], left - (ch == '('), right - (ch == ')'))

        stack = isValid(s)[1]
        lc = sum([1 for val in stack if val[1] == "("])  # num of left braces
        rc = len(stack) - lc

        res, visited = [], set()
        dfs(s, lc, rc)
        return res

    #
    # SOLUTION-2
    #
    ## APPROACH : DYNAMIC PROGRAMMING ##
    ## LOGIC ##
    # We can perceive the task as minimization the number of removed parenthesis and represent the solution as
    # recursive with parameters si - 'Start Index' and oc - 'Open Count'.
    #
    # DropCount = min(DropCount[si + 1][oc], DropCount[si + 1][oc + {1 if s[si] == '(' else -1}]
    #
    def removeInvalidParentheses_using_dynamic_programming_solution_2(self, s: str) -> List[str]:
        """
        :type s: str
        :rtype: List[str]
        """
        N = len(s)
        cache = [[-1 for x in range(N)] for x in range(N)]
        pseq = [[set() for x in range(N + 1)] for x in range(N + 1)]

        c = self.minDrop(s, 0, 0, cache, pseq)

        return list(pseq[0][0])

    def minDrop(self, s, si, oc, cache, pseq):
        N = len(s)

        if oc < 0:
            return N - si + 1

        if si == N:
            if oc == 0:
                pseq[si][oc] = {''}
            return oc

        if cache[si][oc] != -1:
            return cache[si][oc]

        if s[si] in '()':
            dc0 = 1 + self.minDrop(s, si + 1, oc, cache, pseq)
            pseq0 = pseq[si + 1][oc]

            if s[si] == '(':
                dc1 = self.minDrop(s, si + 1, oc + 1, cache, pseq)
                pseq1 = ['(' + x for x in pseq[si + 1][oc + 1]]
            else:
                dc1 = self.minDrop(s, si + 1, oc - 1, cache, pseq)
                pseq1 = [')' + x for x in pseq[si + 1][oc - 1]]

            cache[si][oc] = min(dc0, dc1)

            # note '=' - in case of eqaulity we keep both combination sets
            if dc0 >= dc1:
                pseq[si][oc] = pseq[si][oc].union(pseq1)

            if dc0 <= dc1:
                pseq[si][oc] = pseq[si][oc].union(pseq0)

        else:
            cache[si][oc] = self.minDrop(s, si + 1, oc, cache, pseq)
            pseq[si][oc] = [s[si] + x for x in pseq[si + 1][oc]]

        return cache[si][oc]

    #
    # SOLUTION-3
    #
    ## APPROACH : TOP-DOWN DYNAMIC PROGRAMMING w/ MEMOIZATION using functools.lru_cache ##
    #
    def removeInvalidParentheses_using_top_down_dp_with_memoization_solution_3(self, s: str) -> List[str]:
        @lru_cache(None)
        def dp(i, open):
            ans = set()
            if open < 0:
                return ans # Invalid -> return 0 result
            if i == len(s):
                if open == 0: ans.add("") # Valid -> Return 1 result (empty string)
                return ans

            if s[i] == '(' or s[i] == ')': # Case 1: Skip s[i]: '(', ')'
                ans.update(dp(i + 1, open))

            newOpen = open
            if s[i] == '(': newOpen = open + 1
            elif s[i] == ')': newOpen = open - 1
            for suffix in dp(i + 1, newOpen): # Case 2: Include s[i]: '(', ')' or letter
                ans.add(s[i] + suffix)
            return ans

        validAnswers = dp(0, 0)
        maxLen = max(map(len, validAnswers))
        return filter(lambda x: len(x) == maxLen, validAnswers)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findWords(self) -> None:
        sol = Solution()
        for s, solution in (
            [ "()())()", ["()()()", "(())()"] ],
            [ "(a)())()", ["(a)()()", "(a())()"] ],
            [ ")(", [""] ]
        ):
            self.assertEqual(sorted(solution), sorted(sol.removeInvalidParentheses_using_backtracking_solution_1(s)))
            self.assertEqual(sorted(solution), sorted(sol.removeInvalidParentheses_using_dynamic_programming_solution_2(s)))
            self.assertEqual(sorted(solution), sorted(sol.removeInvalidParentheses_using_top_down_dp_with_memoization_solution_3(s)))

# main
if __name__ == "__main__":
    unittest.main()
