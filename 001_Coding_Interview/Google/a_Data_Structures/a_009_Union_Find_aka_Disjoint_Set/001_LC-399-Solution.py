from typing import List

import collections

import unittest

class UnionFind:
    def __init__(self):
        self.val = 1.0
        self.parent = self
        self.rank = 0

class Solution:

    # Solution 1: DFS - based Solution
    #
    # A series of equations A / B = k can be seen as a graph in which nodes are the dividend and divisor
    # A and B and weights are the result of the division. So we simply create the graph and traverse it
    # with DFS/BFS to get our result.
    #
    # Complexity is K * O(N + M) where N and M are the number of nodes and edges, and K is the number of queries.
    # How many nodes can we have? It's 2 * E, where E is the number of equations (2 different nodes
    # per each equation). We can have at most E edges in the graph.
    #
    # So total complexity is O(K * E), with O(E) additional space for the graph.
    #
    # Trick: The trick here is that the result is the product of the weights between the nodes.
    #
    # Video Explanation: https://youtu.be/GT-qB2FCZ64
    #
    def calcEquation_using_DFS(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G, W = collections.defaultdict(set), collections.defaultdict(float)
        # Example:
        # equations = [["a","b"],["b","c"]]
        # values = [2.0, 3.0]
        # queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        #
        # Output of the below for loop will look like:
        # a) Output of 1st for loop:
        # >>> G
        # defaultdict(<class 'set'>, {'a': {'b'}, 'b': {'c', 'a'}, 'c': {'b'}})
        # >>> W
        # defaultdict(<class 'float'>, {('a', 'b'): 2.0, ('b', 'a'): 0.5, ('b', 'c'): 3.0, ('c', 'b'): 0.3333333333333333})
        #
        # b) Output of 2nd for loop ( the actual answer, i.e., the product of the weights between the nodes ) :
        # >>> res
        # [6.0, 0.5, -1.0, 1.0, -1.0]
        #
        # where, G - node(s)/vertices
        #        W - value/weight of edge
        #
        for (A, B), V in zip(equations, values):
            G[A], G[B] = G[A] | {B}, G[B] | {A}
            W[A, B], W[B, A] = V, 1.0 / V

        res = []
        for X, Y in queries:
            #paths, vis = [-1.0], set()
            vis = set()
            r = self.dfs(G, W, X, Y, 1.0, vis)
            res.append(r)
        return res

    def dfs(self, G, W, start, end, path, vis):
        if start == end and start in G:
            return path
        if start in vis:
            return -1.0

        vis.add(start)
        for node in G[start]:
            r = self.dfs(G, W, node, end, path * W[start, node], vis)
            if r != -1:
                return r
        return -1.0

    # Solution 2: Union Find - Data Structure - based Solution
    #
    # Although this problem can easily be solved using DFS on the fly, there have been
    # follow-up questions in the past that asks for linear space complexity and constant time lookup.
    #
    # Union-Find meets this requirement perfectly. There are other Union-Find solutions on here as well,
    # but they didn't include Union by Rank.
    #
    # Think of a / b = 2.0 as a graph where a is the parent of b and 2.0 is the weight of the path.
    # Then each equation is just a union operation,
    # and each query a / b is just (common_root / b) / (common_root / a)).
    #
    # To implement path compression while keeping track of the path weight, given a node x,
    # just set x.val = x.val * x.parent.val when calling find.
    # For Union-By-Rank, just remember to invert the weight if switching order after rank comparison.
    # The rest should be pretty self-explanatory.
    #
    # Another key to note for this problem is this line:
    # yRoot.val = val * xVal / yVal.
    #
    # This deals with the case when x already exists in the graph.
    # An example scenario:
    # y / x = 2.0, z / x = 3.0.
    # In this order, y would be the parent of x with weight 2.0, and then we set y to be the parent of z as well,
    # with weight 2.0 / 3.0.
    #
    def calcEquation_using_UnionFind(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        uf = {}
        result = []
        if not equations or len(equations) == 0: return []
        for val, (a, b) in zip(values, equations):
            if a not in uf:
                uf[a] = UnionFind()
            if b not in uf:
                uf[b] = UnionFind()
            self.union(uf[a], uf[b], val)
            r1, val1 = self.find(uf[a])
            r2, val2 = self.find(uf[b])

        for (a, b) in queries:
            if a not in uf or b not in uf:
                result.append(-1.0)
            else:
                r1, val1 = self.find(uf[a])
                r2, val2 = self.find(uf[b])
                if r1 == r2:
                    res = val2 / val1
                    result.append(res)
                else:
                    result.append(-1.0)
        return result

    def find(self, x):
        val = 1.0
        while x.parent != x:
            val *= x.val
            p = x.parent
            x.val = x.val * p.val
            x.parent = p.parent
            x = p
        return x, val

    def union(self, x, y, val):
        xRoot, xVal = self.find(x)
        yRoot, yVal = self.find(y)
        if xRoot == yRoot: return
        if xRoot.rank < yRoot.rank:
            yRoot, xRoot = xRoot, yRoot
            yVal, xVal = xVal, yVal
            val = 1 / val
        yRoot.parent = xRoot
        yRoot.val = val * xVal / yVal
        if xRoot.rank == yRoot.rank:
            xRoot.rank += 1

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_oddEvenJumps(self) -> None:
        sol = Solution()
        for equations, values, queries, solution in (
            [
                [["a","b"],["b","c"]],
                [2.0, 3.0],
                [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],
                [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
            ],
            [
                [["a","b"],["b","c"],["bc","cd"]],
                [1.5,2.5,5.0],
                [["a","c"],["c","b"],["bc","cd"],["cd","bc"]],
                [3.75000,0.40000,5.00000,0.20000]
            ],
            [
                [["a", "b"]],
                [0.5],
                [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
                [0.50000, 2.00000, -1.00000, -1.00000]
            ]
        ):
            self.assertEqual(
                solution,
                sol.calcEquation_using_DFS(equations, values, queries)
            )
            self.assertEqual(
                solution,
                sol.calcEquation_using_UnionFind(equations, values, queries)
            )


if __name__ == "__main__":
    unittest.main()
