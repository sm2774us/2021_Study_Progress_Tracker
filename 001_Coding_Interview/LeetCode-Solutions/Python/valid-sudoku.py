# Time:  O(9^2)
# Space: O(9)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.isValidList([board[i][j] for j in range(9)]) or \
               not self.isValidList([board[j][i] for j in range(9)]):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isValidList([board[m][n] for n in range(3 * j, 3 * j + 3) \
                                                     for m in range(3 * i, 3 * i + 3)]):
                    return False
        return True

    def isValidList(self, xs):
        xs = filter(lambda x: x != '.', xs)
        return len(set(xs)) == len(xs)


