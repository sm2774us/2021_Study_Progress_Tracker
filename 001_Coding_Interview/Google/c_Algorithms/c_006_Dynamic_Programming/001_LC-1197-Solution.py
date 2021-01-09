import collections
from functools import lru_cache

import unittest

class Solution:

    # Solution 1: BFS - using deque
    #
    def minKnightMoves_BFS_using_deque_solution_1(self, x: int, y: int) -> int:
        if (x, y)==(0, 0):return 0
        def bfs(i, j, x, y):
            open_list = collections.deque([(i,j,0)])
            seen = {(i, j)}
            while open_list:
                i, j, d = open_list.popleft()
                for di, dj in [(1,2),(2,1),(1,-2),(2,-1),
                               (-1,2),(-2,1), (-1,-2),(-2,-1)]:
                    r, c = i+di, j+dj
                    if (r,c) not in seen and r>-4 and c>-4:
                        if (r,c)==(x,y):return d+1
                        seen.add((r,c))
                        open_list.append((r,c,d+1))
        return bfs(0,0,abs(x), abs(y))

    # Solution 2: BFS - from both source and destination
    #
    def minKnightMoves_BFS_from_source_and_destination_solution_2(self, x: int, y: int) -> int:
        if (x, y)==(0, 0):return 0
        def bfs(open_list, seen):
            open_list_new = []
            for i, j in open_list:
                for di, dj in [(1,2),(2,1),(1,-2),(2,-1),
                        (-1,2),(-2,1), (-1,-2),(-2,-1)]:
                    r, c = i+di, j+dj
                    if (r,c) not in seen and -4<r<abs(x)+4 and -4<c<abs(y)+4:
                        seen.add((r,c))
                        open_list_new.append((r,c))
            return open_list_new, seen
        d_src, d_des = 0, 0
        open_list_src, seen_src = [(0,0)], {(0, 0)}
        open_list_des, seen_des = [(abs(x),abs(y))], {(abs(x), abs(y))}
        while True:
            if seen_src & seen_des:return d_src+d_des
            open_list_src, seen_src = bfs(open_list_src, seen_src)
            d_src += 1
            if seen_src & seen_des:return d_src+d_des
            open_list_des, seen_des = bfs(open_list_des, seen_des)
            d_des += 1

    # Solution 3: Dynamic Programming
    #
    def minKnightMoves_DP_solution_3(self, x: int, y: int) -> int:
        @lru_cache(None)
        def DP(x, y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            return min(DP(abs(x - 1), abs(y - 2)), DP(abs(x - 2), abs(y - 1))) + 1

        return DP(abs(x), abs(y))

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minKnightMoves(self) -> None:
        sol = Solution()
        for x, y, solution in ([2, 1, 1], [5, 5, 4]):
            self.assertEqual(
                solution,
                sol.minKnightMoves_BFS_using_deque_solution_1(x, y)
            )
            self.assertEqual(
                solution,
                sol.minKnightMoves_BFS_from_source_and_destination_solution_2(x, y)
            )
            self.assertEqual(
                solution,
                sol.minKnightMoves_DP_solution_3(x, y)
            )


if __name__ == "__main__":
    unittest.main()
