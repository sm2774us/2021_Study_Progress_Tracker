from typing import List

import collections

import unittest

class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]

        element m[i][j] in self.matrix means sum of previous elements in this row,
        namely sum(m[i][0] + m[i][1] + ... + m[i][j])
        """
        self.matrix = matrix
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col - 1]

    #
    # Solution  : Range Sum Approach
    #
    # Idea      : It should come out some way to store the computed results of sums and get region sum 
    #             based on the pre-computed results. “Range Sum” is a good idea in this case, because 
    #             every element in the matrix stores the sum of all previous elements in this row and 
    #             it can get the range sum by difference of end element and previous element 
    #             of start point.
    #
    # So the overall Time Complexity is O(N)
    # Space complecity is also O(N), where N is the number of points
    #    
    def update(self, row: int, col: int, val: int) -> None:
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void

        original means the single element value in original matrix
        """        
        original = self.matrix[row][col] - (self.matrix[row][col - 1] if col >= 1 else 0)
        for j in range(col, len(self.matrix[0])):
            self.matrix[row][j] += val - original

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int

        region sum is the sum of range sum in every row from row1 to row2
        as the above definition of self.matrix
        each range sum could be calculated as (m[row][col2] - m[row][col1 - 1])
        """        
        return sum(self.matrix[i][col2] - (self.matrix[i][col1 - 1] if col1 >= 1 else 0) for i in range(row1, row2 + 1))

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_rangeSum(self) -> None:
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ]

        numMatrix = NumMatrix(matrix)
        self.assertEqual(8, numMatrix.sumRegion(row1=2, col1=1, row2=4, col2=3))
        numMatrix.update(row=3, col=2, val=2)
        self.assertEqual(10, numMatrix.sumRegion(row1=2, col1=1, row2=4, col2=3))


if __name__ == "__main__":
    unittest.main()
