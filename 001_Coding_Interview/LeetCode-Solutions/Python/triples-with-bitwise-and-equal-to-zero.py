# Time:  O(nlogn), n is the max of A
# Space: O(n)

import collections


# Reference: https://blog.csdn.net/john123741/article/details/76576925
# FWT solution
class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def FWT(A, v):
            B = A[:]
            d = 1
            while d < len(B):
                for i in range(0, len(B), d << 1):
                    for j in range(d):
                        B[i+j] += B[i+j+d] * v
                d <<= 1
            return B

        k = 3
        n, max_A = 1, max(A)
        while n <= max_A:
            n *= 2
        count = collections.Counter(A)
        B = [count[i] for i in range(n)]
        C = FWT(map(lambda x : x**k, FWT(B, 1)), -1)
        return C[0]


# Time:  O(n^3), n is the length of A
# Space: O(n^2)
import collections


class Solution2(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(len(A)):
                count[A[i]&A[j]] += 1
        result = 0
        for k in range(len(A)):
            for v in count:
                if A[k]&v == 0:
                    result += count[v]
        return result
