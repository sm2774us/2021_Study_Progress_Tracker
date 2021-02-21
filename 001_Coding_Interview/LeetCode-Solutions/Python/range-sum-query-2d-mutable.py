from typing import List

import unittest

# Time:  ctor:   O(m * n)
#        update: O(logm * logn)
#        query:  O(logm * logn)
# Space: O(m * n)

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.__matrix = matrix
        self.__bit = [[0] * (len(self.__matrix[0]) + 1) \
                      for _ in range(len(self.__matrix) + 1)]
        for i in range(1, len(self.__bit)):
            for j in range(1, len(self.__bit[0])):
                self.__bit[i][j] = matrix[i-1][j-1] + self.__bit[i-1][j] + \
                                   self.__bit[i][j-1] - self.__bit[i-1][j-1]
        for i in reversed(range(1, len(self.__bit))):
            for j in reversed(range(1, len(self.__bit[0]))):
                last_i, last_j = i - (i & -i), j - (j & -j)
                self.__bit[i][j] = self.__bit[i][j] - self.__bit[i][last_j] - \
                                   self.__bit[last_i][j] + self.__bit[last_i][last_j]

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if val - self.__matrix[row][col]:
            self.__add(row, col, val - self.__matrix[row][col])
            self.__matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.__sum(row2, col2) - self.__sum(row2, col1 - 1) - \
               self.__sum(row1 - 1, col2) + self.__sum(row1 - 1, col1 - 1)

    def __sum(self, row, col):
        row += 1
        col += 1
        ret = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                ret += self.__bit[i][j]
                #j -= (j & -j)
                # to parent
                # Drops the lowest set bit or right most bit to get the parent
                j &= j - 1
            #i -= (i & -i)
            # to parent
            # Drops the lowest set bit or right most bit to get the parent
            i &= i - 1
        return ret

    def __add(self, row, col, val):
        row += 1
        col += 1
        i = row
        while i <= len(self.__matrix):
            j = col
            while j <= len(self.__matrix[0]):
                self.__bit[i][j] += val
                # to next
                # original number ANDed with 2's complement of number
                # add that back to the original number
                j += (j & -j)
            # to next
            # original number ANDed with 2's complement of number
            # add that back to the original number
            i += (i & -i)


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

