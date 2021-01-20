# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = sum(A)
        fi = 0
        for i in range(len(A)):
            fi += i * A[i]

        result = fi
        for i in range(1, len(A)+1):
            fi += s - len(A) * A[-i]
            result = max(result, fi)
        return result

