# Time:  O(m^2*n), m is min(r, c), n is max(r, c)
# Space: O(n), which doesn't include transposed space

import collections


class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        if len(matrix) > len(matrix[0]):
            return self.numSubmatrixSumTarget(map(list, zip(*matrix)), target)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])-1):
                matrix[i][j+1] += matrix[i][j]

        result = 0
        for i in range(len(matrix)):
            prefix_sum = [0]*len(matrix[i])
            for j in range(i, len(matrix)):
                lookup = collections.defaultdict(int)
                lookup[0] = 1
                for k in range(len(matrix[j])):
                    prefix_sum[k] += matrix[j][k]
                    if prefix_sum[k]-target in lookup:
                        result += lookup[prefix_sum[k]-target]
                    lookup[prefix_sum[k]] += 1
        return result
