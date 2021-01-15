#
# Time : O(N); Space: O(1)
# @tag : Grid Routing, Hadlock's Algorithm
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# 42. Trapping Rain Water
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
# **************************************************************************
# Source: https://leetcode.com/problems/trapping-rain-water/ (Leetcode - Problem 42 - Trapping Rain Water)
#         https://practice.geeksforgeeks.org/problems/trapping-rain-water/0 (GeeksForGeeks - Trapping Rain Water)
#
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# Use Two Pointers to track the highest bar on left and right, respectively.
#
# - start check from both sides, move the point where wall is lower ( because taller wall may leak water on the
#   other lower side )
#
# - <leftmax> and <rightmax> are used to record the walls. If the land is lower than the wall, means it can hold water.
#
# - if a wall found taller than the max height wall on the other side, stop there (because taller wall may leak water
#   on the other lower side). Then move the lower side point.
#
from typing import List
import collections

import unittest

class Solution:
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # Solution 1: Hadlock's Algorithm ( Grid Routing Algorithms )
    #
    # Basically find the trees, sort them by order, find the distance from each tree to the next, and sum those
    # distances. But how to find the distance from one cell to some other cell? BFS is far to slow for the current
    # test suite. Instead use what's apparently known as "Hadlock's Algorithm" (though I've only seen high-level
    # descriptions of that). First try paths with no detour (only try steps in the direction towards the goal),
    # then if necessary try paths with one detour step, then paths with two detour steps, etc. The distance then is
    # the Manhattan distance plus twice the number of detour steps (twice because you'll have to make up for a
    # detour step with a later step back towards the goal).
    #
    # How to implement that?
    #   * Round 1: Run a DFS only on cells that you can reach from the start cell with no detour towards the goal,
    #              i.e., only walking in the direction towards the goal. If this reaches the goal, we're done.
    #              Otherwise...
    #   * Round 2: Try again, but this time try starting from all those cells reachable with one detour step.
    #              Collect these in round 1.
    #   * Round 3: If round 2 fails, try again but start from all those cells reachable with two detour steps.
    #              Collect these in round 2.
    #   * And so on...
    #
    # If there are no obstacles, then this directly walks a shortest path towards the goal, which is of course
    # very fast. Much better than BFS which would waste time looking in all directions.
    # With only a few obstacles, it's still close to optimal.
    #
    # My distance function does this searching algorithm. I keep the current to-be-searched cells in my
    # now stack. When I move to a neighbor that's closer to the goal, I also put it in now. If it's not closer,
    # then that's a detour step so I just remember it on my soon stack for the next round.
    #
    def cutOffTree_hadlock_algorithm_solution_1(self, forest: List[List[int]]) -> int:

        # Add sentinels (a border of zeros) so we don't need index-checks later on.
        forest.append([0] * len(forest[0]))
        for row in forest:
            row.append(0)

        # Find the trees.
        trees = [(height, i, j)
                 for i, row in enumerate(forest)
                 for j, height in enumerate(row)
                 if height > 1]

        # Can we reach every tree? If not, return -1 right away.
        queue = [(0, 0)]
        reached = set()
        for i, j in queue:
            if (i, j) not in reached and forest[i][j]:
                reached.add((i, j))
                queue += (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
        if not all((i, j) in reached for (_, i, j) in trees):
            return -1

        # Distance from (i, j) to (I, J).
        def distance(i, j, I, J):
            now, soon = [(i, j)], []
            expanded = set()
            manhattan = abs(i - I) + abs(j - J)
            detours = 0
            while True:
                if not now:
                    now, soon = soon, []
                    detours += 1
                i, j = now.pop()
                if (i, j) == (I, J):
                    return manhattan + 2 * detours
                if (i, j) not in expanded:
                    expanded.add((i, j))
                    for i, j, closer in (i + 1, j, i < I), (i - 1, j, i > I), (i, j + 1, j < J), (i, j - 1, j > J):
                        if forest[i][j]:
                            (now if closer else soon).append((i, j))

        # Sum the distances from one tree to the next (sorted by height).
        trees.sort()
        return sum(distance(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees))

    #
    #
    #
    # A nice explanation of A* algorithm (pseudo code): https://en.wikipedia.org/wiki/A*_search_algorithm
    #
    # The general idea is :
    #
    # g is the cost it took to get to the node, most likely the number of squares we passed by from the start. h is our guess as to how much it'll cost to reach the goal from that node. f is the cost function, and f = g+h.
    #
    # struct node {
    #     node *parent;
    #     int x, y;
    #     float f, g, h;
    # }
    #
    # // A*
    # initialize the open list
    # initialize the closed list
    # put the starting node on the open list (you can leave its f at zero)
    #
    # while the open list is not empty
    #     find the node with the least f on the open list, call it "q"
    #     pop q off the open list
    #     generate q's 8 successors and set their parents to q
    #     for each successor
    #     	if successor is the goal, stop the search
    #         successor.g = q.g + distance between successor and q
    #         successor.h = distance from goal to successor
    #         successor.f = successor.g + successor.h
    #
    #         if a node with the same position as successor is in the OPEN list \
    #             which has a lower f than successor, skip this successor
    #         if a node with the same position as successor is in the CLOSED list \
    #             which has a lower f than successor, skip this successor
    #         otherwise, add the node to the open list
    #     end
    #     push q on the closed list
    # end
    #
    # In that way, we only add a node to the queue if it guarantees a better solution.
    #
    def cutOffTree_a_star_search_algorithm_solution_2(self, forest: List[List[int]]) -> int:
        #print(forest)
        rows = len(forest)
        if rows == 0:
            return 0

        cols = len(forest[0])
        if cols == 0:
            return 0

        forest.append([0] * cols)
        for row in forest:
            row.append(0)

        trees = {(r, c) for c in range(cols) for r in range(rows) if forest[r][c] > 1}

        visited = {(0, 0)}
        queue = [(0, 0)]
        while len(queue) != 0:
            r, c = queue.pop()
            for nr, nc in ((r + dr, c + dc) for dr, dc in self.d):
                if (nr, nc) not in visited and forest[nr][nc] > 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        if trees.difference(visited):
            return -1

        trees = sorted(trees, key=lambda t: forest[t[0]][t[1]])
        if trees[0] != (0, 0):
            trees.insert(0, (0, 0))
        num_trees = len(trees)
        #print('TREES:', trees)

        total_steps = 0
        for i in range(1, num_trees):
            pr, pc = p = trees[i - 1]
            qr, qc = q = trees[i]
            cost = abs(pr - qr) + abs(pc - qc)

            queue, next_queue = [], [] # Using list: 0.53s, 0.52s, 0.54s
            #queue, next_queue = collections.deque(), collections.deque() # Using collections.deque: 1.45s, 1.50s, 1.46s
            queue.append(p)
            visited, pending_visited = {p}, set()
            while len(queue) + len(next_queue) != 0:
                if len(queue) == 0:
                    queue = next_queue
                    next_queue = collections.deque()

                    visited.update(pending_visited)
                    pending_visited = set()
                    cost += 2

                (r, c) = queue.pop() # Using list
                #(r, c) = queue.popleft() # Using collections.deque
                #print('POP', r, c, cost)

                safe_dr = qr - r
                safe_dr = safe_dr and safe_dr // abs(safe_dr)
                safe_dc = qc - c
                safe_dc = safe_dc and safe_dc // abs(safe_dc)
                for dr, dc in self.d:
                    nbr = (r + dr, c + dc)
                    if nbr not in visited and forest[nbr[0]][nbr[1]] > 0:
                        #print('SAFE', (safe_dr, safe_dc), 'D', (dr, dc))
                        if (dr == safe_dr and dc != -safe_dc) or (dc == safe_dc and dr != -safe_dr):
                            queue.append(nbr)
                            visited.add(nbr)
                            ncost = cost
                            #print('PUSH', nbr)
                        else:
                            next_queue.append(nbr)
                            pending_visited.add(nbr)
                            ncost = cost + 2
                            #print('PUSH NEXT', nbr)
                        if nbr == q:
                            #print('COST:', p, q, ncost)
                            total_steps += ncost
                            queue = next_queue = list()
                            break

                # print('MAP', cost)
                # for rr in range(rows):
                #     for cc in range(cols):
                #         if (rr, cc) == (r, c):
                #             print('*', end='')
                #         elif (rr, cc) in queue:
                #             print('Q', end='')
                #         elif (rr, cc) in visited:
                #             print('+', end='')
                #         elif (rr, cc) in next_queue:
                #             print('N', end='')
                #         else:
                #             print(forest[rr][cc], end='')
                #     print()

        return total_steps

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_cutOffTree(self) -> None:
        s = Solution()
        for forest, solution in (
            [[[1,2,3],[0,0,4],[7,6,5]], 6],
            [[[1,2,3],[0,0,0],[7,6,5]], -1],
            [[[2,3,4],[0,0,5],[8,7,6]], 6]
        ):
            self.assertEqual(
                solution,
                s.cutOffTree_hadlock_algorithm_solution_1(forest),
            )
            self.assertEqual(
                solution,
                s.cutOffTree_a_star_search_algorithm_solution_2(forest)
            )


if __name__ == "__main__":
    unittest.main()
