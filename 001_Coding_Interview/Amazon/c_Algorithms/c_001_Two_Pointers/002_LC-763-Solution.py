from typing import List

import unittest

class Solution:

    # Approach 1: Two Pointers
    #
    # Figure out the rightmost index first and use it to denote the start of the next section.
    #
    # Reset the left pointer at the start of each new section.
    #
    # Store the difference of right and left pointers + 1 as in the result for each section.
    def partitionLabels_two_pointer_solution_1(self, S: str) -> List[int]:
        rightmost = {c: i for i, c in enumerate(S)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(S):

            right = max(right, rightmost[letter])

            if i == right:
                result += [right - left + 1]
                left = i + 1

        return result

    # Approach 2: Greedy Algorithm
    #
    # The idea of this solution is greedily construct our partition, let us consider the example
    # S = ababcbacdefegdehijhklij. We need to start with letter a and we can not stop, until we reach the last occurence of a: so, we need to take ababcba part at least. But if we take this part, we need to consider letters b and c as well and also traverse our string until we meet the last occurence of these letters, so we need to take ababcbac. Here we can stop, because we already take into account all symbols inside this string. So, we go to the next symbol and repeat our partition. So, what we have in my code:
    #
    # First, we need to know all ends for each letter in advance, I call it ends.
    # Also, curr is current index and last is index we need to traverse until. For each group of symbols we need to do: last = ends[S[curr]]: we find the place we need to traverse; while we do no reach this place, we look at the next symbol and update our last. So, we stop, when curr become greater than last.
    # We add curr to our out result.
    # Note, that we need to have [8,7,8] for our example, but we get [8,15,23], places where our partitions are. So, we evaluate differences 8-0, 15-8, 23-15 and return them.
    #
    # Complexity: time complexity is O(n), we traverse our string twice: one time when we evaluate ends and second time when we do partitions. Space complexity is O(26): to keep our ends (also we have answer, but it can not be greater than 26 as well).
    #
    def partitionLabels_greedy_solution_2(self, S: str) -> List[int]:
        ends = {c: i for i, c in enumerate(S)}
        curr, out = 0, [0]

        while curr < len(S):
            last = ends[S[curr]]
            while curr <= last:
                symb = S[curr]
                last = max(last, ends[symb])
                curr += 1
            out.append(curr)

        return [out[i] - out[i - 1] for i in range(1, len(out))]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_partitionLabels(self) -> None:
        sol = Solution()
        S = "ababcbacadefegdehijhklij"
        self.assertEqual(
            [9,7,8],
            sol.partitionLabels_two_pointer_solution_1(S)
        )
        self.assertEqual(
            [9, 7, 8],
            sol.partitionLabels_greedy_solution_2(S)
        )


if __name__ == "__main__":
    unittest.main()
