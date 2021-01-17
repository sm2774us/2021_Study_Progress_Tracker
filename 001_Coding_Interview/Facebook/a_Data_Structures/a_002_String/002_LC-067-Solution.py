from typing import List
import collections
import re

import unittest


class Solution:

    # Solution 1: GRADE-SCHOOL ADDITION LOGIC
    #
    #
    def addBinary_grade_school_addition_logic_solution_1(self, a: str, b: str) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        sum = ""
        aIndex = len(a) - 1
        bIndex = len(b) - 1

        while aIndex >= 0 or bIndex >= 0 or carry:
            if aIndex >= 0:
                carry += int(a[aIndex])

            if bIndex >= 0:
                carry += int(b[bIndex])

            sum = str(carry % 2) + sum
            carry //= 2

            aIndex -= 1
            bIndex -= 1

        return sum

    # Solution 1: BITWISE SOLUTION
    # ##LOGIC##
    #
    # The solution does not calculate carry digit by digit but use and("&") operator, which means,
    # if two digits are "1", there must be a carry equals 1. But we need to left shift("<<") it
    # because the carry is one digit higher.
    # for the part not include carry, we can use XOR(^), 1^1 = 0, 1 + 1 = 10, without carry ,it is also "0".
    #
    #
    def addBinary_bitwise_solution_2(self, a: str, b: str) -> str:
        if a == "":
            return b
        if b == "":
            return a
        a_2 = int(a,2)
        b_2 = int(b,2)
        carry = 1
        while carry != 0:
            carry = (a_2 & b_2)<<1
            a_2 = a_2 ^ b_2
            b_2 = carry
        return bin(a_2)[2:]


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_most_common_word(self):
        sol = Solution()

        for a, b, solution in (["11", "1", "100"],["1010", "1011", "10101"]):
            self.assertEqual(
                sol.addBinary_grade_school_addition_logic_solution_1(
                    a, b
                ),
                solution,
            )
            self.assertEqual(
                sol.addBinary_bitwise_solution_2(
                    a, b
                ),
                solution,
            )


if __name__ == "__main__":
    unittest.main()
