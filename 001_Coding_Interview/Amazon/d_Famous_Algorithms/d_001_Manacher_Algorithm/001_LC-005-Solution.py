# Time : O(N); Space: O(N)
# @tag : String, Manacher's Algorithm
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 5: Longest Palindromic Substring
#
# Description:
#
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
#
# Input: "cbbd"
# Output: "bb"
#
# **************************************************************************
# Source: https://leetcode.com/problems/longest-palindromic-substring/ (Leetcode - Problem 5 - Longest Palindromic Substring)
#         https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0 (GeeksForGeeks - Longest Palindrome in a String)
#
# Solution Explanation
# **************************************************************************
# There is an O(n) algorithm called Manacher's algorithm, explained here in detail.
# However, it is a non-trivial algorithm, and no one expects you to come up with this algorithm
# in a 45 minutes coding session. But, please go ahead and understand it, I promise it will be a lot of fun.
#
# **************************************************************************
# Palindrome Definition (https://en.wikipedia.org/wiki/Palindrome) :
# ***********************
# A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward,
# such as madam, racecar.
#
# **************************************************************************
# Longest palindromic substring - [Manacher's algorithm] - (https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm) :
# Glen Manacher (1975) invented a linear time algorithm for listing all the palindromes that appear at the start of a given string.
# **************************************************************************
# To find a longest palindrome in a string in linear time, an algorithm may take advantage of the following characteristics or observations about a palindrome and a sub-palindrome:
#
# 1. The left side of a palindrome is a mirror image of its right side.
# 2. (Case 1) A third palindrome whose center is within the right side of a first palindrome will have exactly the same
#    length as a second palindrome anchored at the mirror center on the left side, if the second palindrome is within
#    the bounds of the first palindrome by at least one character (not meeting the left bound of the first palindrome).
#    Such as "dacabacad", the whole string is the first palindrome, "aca" in the left side as second palindrome,
#    "aca" in the right side as third palindrome.
#    In this case, the second and third palindrome have exactly the same length.
# 3. (Case 2) If the second palindrome meets or extends beyond the left bound of the first palindrome,
#    then the distance from the center of the second palindrome to the left bound of the first palindrome
#    is exactly equal to the distance from the center of the third palindrome to the right bound
#    of the first palindrome.
# 4. To find the length of the third palindrome under Case 2, the next character after the right outermost
#    character of the first palindrome would then be compared with its mirror character about the center of the
#    third palindrome, until there is no match or no more characters to compare.
# 5. (Case 3) Neither the first nor second palindrome provides information to help determine the
#    palindromic length of a fourth palindrome whose center is outside the right side of the first palindrome.
# 6. It is therefore desirable to have a palindrome as a reference (i.e., the role of the first palindrome)
#    that possesses characters farthest to the right in a string when determining from left to right the
#    palindromic length of a substring in the string (and consequently, the third palindrome in Case 2
#    and the fourth palindrome in Case 3 could replace the first palindrome to become the new reference).
# 7. Regarding the time complexity of palindromic length determination for each character in a string:
#    there is no character comparison for Case 1, while for Cases 2 and 3 only the characters in the string beyond
#    the right outermost character of the reference palindrome are candidates for comparison (and consequently
#    Case 3 always results in a new reference palindrome while Case 2 does so only if the third palindrome
#    is actually longer than its guaranteed minimum length).
# 8. For even-length palindromes, the center is at the boundary of the two characters in the middle.
#
#
import unittest


class Solution:
    # Solution 1 : Manacher Algorithm
    def longestPalindrome_Manacher_Algorithm_solution_1(self, s: str) -> str:
        if not s or not len(s):
            return ""

        # Transform S into T.
        T = "#".join(f"#{s}#")

        n = len(T)
        max_right_size_length = [0] * n
        C = R = 0

        for i in range(1, n - 1):
            max_right_size_length[i] = (R > i) and min(
                R - i, max_right_size_length[2 * C - i]
            )  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while (
                i - 1 - max_right_size_length[i] >= 0
                and i + 1 + max_right_size_length[i] < n
                and T[i + 1 + max_right_size_length[i]]
                == T[i - 1 - max_right_size_length[i]]
            ):
                max_right_size_length[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + max_right_size_length[i] > R:
                C, R = i, i + max_right_size_length[i]

        # Find the maximum element in max_right_size_length.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(max_right_size_length))
        return s[(centerIndex - maxLen) // 2 : (centerIndex + maxLen) // 2]

    # Solution 2 : Dynamic Programming
    #
    # Video Explanation : https://youtu.be/XjBgjmWB_Kw
    #
    def longestPalindrome_dynamic_programming_solution_2(self, s):
        dp = [[0] * len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if ans == "" or max_length < j - i + 1:
                        ans = s[i:j+1]
                        max_length = j - i + 1
        return ans

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_longestPalindrome(self) -> None:
        s = Solution()
        for strs, solution in (["babad", "aba"], ["cbbd", "bb"]):
            self.assertEqual(
                solution,
                s.longestPalindrome_Manacher_Algorithm_solution_1(strs),
                "Should return the longest palindromic substring",
            )
            self.assertEqual(
                solution,
                s.longestPalindrome_dynamic_programming_solution_2(strs),
                "Should return the longest palindromic substring",
            )


if __name__ == "__main__":
    unittest.main()
