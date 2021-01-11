# Time  :
# Space :
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 819: Most Common Word
#
# Description:
#
# Given a paragraph and a list of banned words, return the most frequent word
# that is not in the list of banned words.  It is guaranteed there is at least
# one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.
# Words in the paragraph are not case sensitive.  The answer is in lowercase.
#
#
#
# Example:
#
# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
#
#
# Note:
#
#   * 1 <= paragraph.length <= 1000.
#   * 0 <= banned.length <= 100.
#   * 1 <= banned[i].length <= 10.
#   * The answer is unique, and written in lowercase (even if its occurrences
#     in paragraph may have uppercase symbols, and even if it is a proper noun.)
#     paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
#   * There are no hyphens or hyphenated words.
#    * Words only consist of letters, never apostrophes or other punctuation symbols.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/most-common-word/ (LeetCode - Problem 819 - Most Common Word)
#
#
from typing import List
import collections
import re

import unittest


class Solution:

    # Solution 1: Using ord, list comprehension and defaultdict
    #
    # Let n = # of words in paragraph excluding white spaces and punctuations
    # Time complexity: O(len(n) + len(banned))
    # Space complexity: O(len(n))
    #
    # If banned is a long list, we can cast it into a set to force the time complexity
    # of the in operator inside the first for loop to be O(1).
    # Though, this won't affect the final time complexity because O(n) will always overtake O(1).
    #
    def mostCommonWord_solution_1_using_list_comprehension(
        self, paragraph: str, banned: List[str]
    ) -> str:
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        charRange = range(ord("a"), ord("z") + 1)
        chars = [
            char.lower() if ord(char.lower()) in charRange else " "
            for char in paragraph
        ]
        words = "".join(chars).split()

        occurrences = collections.defaultdict(int)

        for word in words:
            if word not in banned:
                occurrences[word] += 1

        maxOccurred = max(occurrences.values())

        for word, occurence in occurrences.items():
            if occurence == maxOccurred:
                return word

    # Solution 2: Using max and key function
    def mostCommonWord_solution_2_using_max_and_key_function(
        self, paragraph: str, banned: List[str]
    ) -> str:
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        dict = {}
        banned = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()

        for word in paragraph:
            if word not in banned:
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1
            # Don't need a counter if you use key function to choose the key with max. count!
        return max(dict, key=dict.get)

    # Solution 3: Using regex
    def mostCommonWord_solution_3_using_regex(
        self, paragraph: str, banned: List[str]
    ) -> str:
        ban = set(banned)
        # words = re.sub(r'[^a-zA-Z]', ' ', p).lower().split()
        # the regex in the commented line above can be simplified to:
        words = re.findall(r"\w+", paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][
            0
        ]


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_most_common_word(self):
        sol = Solution()

        for paragraph, banned, solution in (
            [
                "Bob hit a ball, the hit BALL flew far after it was hit.",
                ["hit"],
                "ball",
            ],
            ["I can not account for what I can not see.", ["i", "not"], "can"],
            ["This book is a well-known and well-written book.", [], "book"],
        ):
            self.assertEqual(
                sol.mostCommonWord_solution_1_using_list_comprehension(
                    paragraph, banned
                ),
                solution,
            )
            self.assertEqual(
                sol.mostCommonWord_solution_2_using_max_and_key_function(
                    paragraph, banned
                ),
                solution,
            )
            self.assertEqual(
                sol.mostCommonWord_solution_3_using_regex(paragraph, banned), solution
            )


if __name__ == "__main__":
    unittest.main()
