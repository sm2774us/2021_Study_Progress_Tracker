from typing import List

import unittest

# Similar to: [LC-159 - Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
class Solution:

    #
    # Sliding window approach where we denote right and left as pointers making up our window.
    # We use a hashmap to ensure that there are at most three different types of fruits in our window range.
    #
    # Here are the basics:
    #
    # If only 1 type of fruits is in our window range -> Increment the right pointer to include all fruit(s) until a second type of fruit is found.
    # If we have 2 type of fruits in our window range -> Increment the right pointer to include all fruit(s) until a third type of fruit is found.
    # If we have 3 type of fruits in our window range -> Shorten the left side of our window by incrementing our left pointer.
    # and so on...
    #
    # TC: O(N) - Linear
    # SC: O(1) - Constant space
    #
    def totalFruit(self, tree: List[int]) -> int:
        """
        :type tree: List[int]
        :rtype: int
        """
        if tree is None or len(tree) <= 2:
            return len(tree)

        max_fruits, fruit_bucket = 0, {}
        right = left = fruit_count = 0

        while right < len(tree):
            right_fruit = tree[right]

            """ 1 fruit type in basket """
            if len(fruit_bucket) < 2:
                fruit_bucket[right_fruit] = (
                    fruit_bucket[right_fruit] + 1 if right_fruit in fruit_bucket else 1)
                fruit_count += 1
                right += 1

            """ 2 fruit types in basket """
            if len(fruit_bucket) == 2:
                # Increment right pointer until a third fruit type is found
                while right < len(tree) and tree[right] in fruit_bucket:
                    fruit_bucket[tree[right]] += 1
                    fruit_count += 1
                    right += 1

                max_fruits = max(max_fruits, fruit_count)

                """ Shorten left side of window: Increment left pointer to discard all 
                fruit(s) of left_fruit variation from window """
                left_fruit = tree[left]
                while left < right and tree[left] == left_fruit:
                    fruit_bucket[left_fruit] -= 1
                    fruit_count -= 1
                    left += 1

                # No more variation of left_fruit in bucket
                if not fruit_bucket[left_fruit]:
                    # Delete left_fruit category from bucket
                    del fruit_bucket[left_fruit]
                    # RESET COUNTER: fruit_count = remaining fruit(s) that's NOT of left_fruit category
                    fruit_count = fruit_bucket[tree[left]]

        return max(fruit_count, max_fruits)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_totalFruit(self) -> None:
        sol = Solution()
        for tree, solution in (
            [
                [1,2,1],
                3
            ],
            [
                [0, 1, 2, 2],
                3
            ],
            [
                [1, 2, 3, 2, 2],
                4
            ],
            [
                [3,3,3,1,2,1,1,2,3,3,4],
                5
            ]
        ):
            self.assertEqual(
                solution,
                sol.totalFruit(tree)
            )


if __name__ == "__main__":
    unittest.main()
