#
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 909: Snakes and Ladders
#
# Description:
#
# On an N x N board, the numbers from 1 to N*N are written boustrophedonically (of or relating to lines written in opposite directions)
# starting from the bottom left of the board,
# and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:
#
# Refer to Fig_1.png
#
# Example 1:
#
# You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:
#
#       * You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
#           * (This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
#       * If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
#
# A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].
#
# Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)
#
# Return the least number of moves required to reach square N*N.  If it is not possible, return -1.
#
# Example 1:
#
# Input: [
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation:
# At the beginning, you start at square 1 [at row 5, column 0].
# You decide to move to square 2, and must take the ladder to square 15.
# You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
# You then decide to move to square 14, and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
#
# Note:
#
#   1. 2 <= board.length = board[0].length <= 20
#   2. board[i][j] is between 1 and N*N or is equal to -1.
#   3. The board square with number 1 has no snake or ladder.
#   4. The board square with number N*N has no snake or ladder.
#
# **************************************************************************
# Source: https://leetcode.com/problems/snakes-and-ladders/ (LeetCode - Problem 909 - Snakes and Ladders)
#         https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem/0 (GeeksForGeeks - Snake and Ladder Problem)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# Explanation
# **************************************************************************
# Build a transform mapping from order,
# Find all alien words with letters in normal order.
#
# For example, if we have order = "xyz..."
# We can map the word "xyz" to "abc" or "123"
#
# Then we check if all words are in sorted order.
#
# Complexity
# **************************************************************************
# Time O(NS)
# Space O(1)
#
#
from typing import List

import unittest


class Solution:
    #
    # we need not take +1, +2, +3, +4, +5 steps if the +6 step was a regular board square,
    # unless one of those earlier steps was a snake or ladder.
    # There's nothing that we'd like to do from one of those earlier steps that we can't do from the +6 step.
    # In general, the code to reduce the expansion of nodes is as below.
    # This beats 100% on some runs, and if the test cases were bigger the speed difference would be even more dramatic.
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            refuse_steps = False
            for i in range(min(n ** 2, x + 6), x, -1):
                a, b = (i - 1) // n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0:
                    i = nxt
                if i == n * n:
                    return need[x] + 1
                if nxt == -1 and refuse_steps:
                    continue
                if nxt == -1:
                    refuse_steps = True
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isAlienDictionarySorted(self) -> None:
        sol = Solution()
        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
        self.assertEqual(4, sol.snakesAndLadders(board))


# main
if __name__ == "__main__":
    unittest.main()
