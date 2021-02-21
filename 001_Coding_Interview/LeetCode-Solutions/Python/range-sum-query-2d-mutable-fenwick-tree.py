from typing import List

import unittest

# Solution : Using Fenwick Tree
#
# Time:  ctor:   O(m * n)
#        update: O(logm * logn)
#        query:  O(logm * logn)
# Space: O(m * n)

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        if n == 0: return
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.BIT2D = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        m = len(self.matrix)
        n = len(self.matrix[0])
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= m:
            j = col + 1
            while j <= n:
                self.BIT2D[i][j] += diff
                # to next
                # original number ANDed with 2's complement of number
                # add that back to the original number
                j += (j & (-j))
            # to next
            # original number ANDed with 2's complement of number
            # add that back to the original number
            i += (i & (-i))

    def getSum(self, row, col):
        ans = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                ans += self.BIT2D[i][j]
                # to parent
                # Drop the lowest set bit or right most bit to get the parent
                j -= (j & (-j))
            # to parent
            # Drop the lowest set bit or right most bit to get the parent
            i -= (i & (-i))
        return ans

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getSum(row2, col2) - self.getSum(row2, col1 - 1) - self.getSum(row1 - 1, col2) + self.getSum(
            row1 - 1, col1 - 1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_range_sum_query_2d_mutable(self) -> None:
        matrix = [
                    [3, 0, 1, 4, 2],
                    [5, 6, 3, 2, 1],
                    [1, 2, 0, 1, 5],
                    [4, 1, 0, 1, 7],
                    [1, 0, 3, 0, 5]
                 ]
        numMatrix = NumMatrix(matrix)
        self.assertEqual(8, numMatrix.sumRegion(2, 1, 4, 3))
        numMatrix.update(3, 2, 2)
        self.assertEqual(10, numMatrix.sumRegion(2, 1, 4, 3))

if __name__ == "__main__":
    unittest.main()

