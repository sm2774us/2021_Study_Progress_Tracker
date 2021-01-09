from typing import List

import collections

import unittest

class Solution:
    # def removeStones(self, stones: List[List[int]]) -> int:
    #     g, N = collections.defaultdict(list), len(stones)
    #     for i in range(N):
    #         for j in range(i):
    #             (a, b), (c, d) = stones[i], stones[j]
    #             if a == c or b == d:
    #                 g[i] += j,
    #                 g[j] += i,
    #
    #     seen = set()
    #
    #     def dfs(a):
    #         seen.add(a)
    #         [dfs(b) for b in g[a] if b not in seen]
    #
    #     return N - sum(not dfs(i) for i in range(N) if i not in seen)

    #
    # As pointed out by solution, the main insight is to convert the problem to 'count the number of islands'.
    #
    # However, most answers, including the Solution and he highest voted one, use Union Find.
    # This bring us two inconvenience:
    # 1. you need a template
    # 2. The time complexity is a little hard to prove.
    #
    # Here we give a much more concise solution which avoids union find (though under the hood it is borrowing the idea)
    #
    # We want to build a graph of all points.
    #
    # The brute force is to connect the point to every point it "should" connect: Iterating the list, for each point, look back and see if traversed points are on the same row/column. Doing this is undesirable O(N^2).
    #
    # Since we only care about the connected component here, we can build the graph in a different way. we only connect every point to a 'representative' point on that row/column. And how do we find the representative point? Very easy. When iterating the list, the first time you encounter a point on that row/column, appoint it as the representative of that row/column.
    #
    # The graph buiding is O(N), and we end up with a graph of same connected component as brute-force.
    #
    # The DFS of "count the number of islands" is also easy-to-prove O(N).
    # So the overall Time Complexity is O(N)
    # Space complecity is also O(N), where N is the number of points
    #
    def removeStones(self, stones: List[List[int]]) -> int:
        row_repres = {}
        col_repres = {}
        graph = {}
        for x, y in stones:
            if x not in row_repres:
                row_repres[x] = (x, y)
            if y not in col_repres:
                col_repres[y] = (x, y)
            graph[(x, y)] = []
            if row_repres[x] != (x, y):
                graph[row_repres[x]].append((x, y))
                graph[(x, y)].append(row_repres[x])
            if col_repres[y] != (x, y):
                graph[col_repres[y]].append((x, y))
                graph[(x, y)].append(col_repres[y])

        def dfs(x, y, visited):
            visited.add((x, y))
            for nb_x, nb_y in graph[(x, y)]:
                if (nb_x, nb_y) not in visited:
                    dfs(nb_x, nb_y, visited)

        num_islands = 0
        visited = set()
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y, visited)
                num_islands += 1

        return len(stones) - num_islands

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_removeStones(self) -> None:
        sol = Solution()
        for stones, solution in (
            [
                [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]],
                5
            ],
            [
                [[0,0],[0,2],[1,1],[2,0],[2,2]],
                3
            ],
            [
                [[0,0]],
                0
            ]
        ):
            self.assertEqual(
                solution,
                sol.removeStones(stones)
            )


if __name__ == "__main__":
    unittest.main()
