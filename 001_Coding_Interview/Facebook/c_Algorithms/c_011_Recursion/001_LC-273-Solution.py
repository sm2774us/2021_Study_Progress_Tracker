from typing import List
import collections
import re

import unittest


class Solution:

    # Solution: RECURSIVE
    #
    #
    def numberToWords(self, num: int) -> str:
        """
        :type num: int
        :type banned: List[str]
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousand = 'Thousand Million Billion'.split()

        def word(num, idx=0):
            if num == 0:
                return []
            if num < 20:
                return [to19[num - 1]]
            if num < 100:
                return [tens[num // 10 - 2]] + word(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ['Hundred'] + word(num % 100)

            p, r = num // 1000, num % 1000
            space = [thousand[idx]] if p % 1000 != 0 else []
            return word(p, idx + 1) + space + word(r)

        return ' '.join(word(num)) or 'Zero'

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
