import unittest

# Similar to: [LC-904 - Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
class Solution:

    #
    # Sliding window approach where we denote right and left as pointers making up our window.
    # We use a hashmap to ensure that there are at most three different types of fruits in our window range.
    #
    # Here are the basics:
    #
    # If only 1 distinct character in our window range -> Increment the right pointer to include all character(s) until a second distinct character is found.
    # If we have 2 distinct characters in our window range -> Increment the right pointer to include all characters(s) until a third distinct character is found.
    # If we have 3 distinct characters in our window range -> Shorten the left side of our window by incrementing our left pointer.
    # and so on...
    #
    # TC: O(N)
    # SC: O(N)
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        longest_substr, dict = 0, {}
        right = left = count = 0

        while right < len(s):
            right_str = s[right]

            """ 1 distinct character in dict """
            if len(dict) < 2:
                dict[right_str] = (
                    dict[right_str] + 1 if right_str in dict else 1)
                count += 1
                right += 1

            """ 2 distinct characters in dict """
            if len(dict) == 2:
                # Increment right pointer until a third fruit type is found
                while right < len(s) and s[right] in dict:
                    dict[s[right]] += 1
                    count += 1
                    right += 1

                longest_substr = max(longest_substr, count)

                """ Shorten left side of window: Increment left pointer to discard all 
                character(s) of left_str variation from window """
                left_str = s[left]
                while left < right and s[left] == left_str:
                    dict[left_str] -= 1
                    count -= 1
                    left += 1

                # No more variation of left_str in bucket
                if not dict[left_str]:
                    # Delete left_str category from bucket
                    del dict[left_str]
                    # RESET COUNTER: count = remaining character(s) that's NOT of left_str category
                    count = dict[s[left]]

        return max(count, longest_substr)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_kEmptySlots(self) -> None:
        sol = Solution()
        for s, solution in (["eceba",3],["ccaabbb",5]):
            self.assertEqual(
                solution,
                sol.lengthOfLongestSubstringTwoDistinct(s)
            )


if __name__ == "__main__":
    unittest.main()
