import unittest

# Segment Tree

# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
class NumArrayUsingSegmentTree(object):

    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        # x << 1 => x * 2 => x multiplied by 2
        # x >> 1 => x / 2 => x divided by 2
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, i, val):
        n = self.l + i
        self.tree[n] = val
        # x << 1 => x * 2 => x multiplied by 2
        # x >> 1 => x / 2 => x divided by 2

        # x ^ 1 => if x is even then x+1
        #       => is x is odd then x-1
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1

    def sumRange(self, i, j):
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res

# Fenwick Tree

# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
class NumArrayUsingBIT(object):
    def __init__(self, nums):
        self.nums = nums
        self.N = len(self.nums)
        self.tree = [0] * (self.N + 1)
        ## optimize initiate BIT in O(n)
        for j in range(1, self.N + 1):
            self.tree[j] += self.nums[j - 1]
            if (j + (j & (-j))) <= self.N:
                self.tree[j + (j & (-j))] += self.tree[j]

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.N:
            self.tree[i] += diff
            # to next
            # original number ANDed with 2's complement of number
            # add that back to the original number
            i += (i & (-i))

    def sumRange(self, i, j):
        return self.getSum(j) - self.getSum(i - 1)

    def getSum(self, i):
        sm = 0
        i += 1
        while i > 0:
            sm += self.tree[i]
            #i -= (i & (-i))
            # to parent
            # Drops the lowest set bit or right most bit to get the parent
            i &= i - 1
        return sm

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_range_sum_query_using_segment_tree(self) -> None:
        nums = [1, 3, 5]
        numArray = NumArrayUsingSegmentTree(nums)
        self.assertEqual(9, numArray.sumRange(0,2))
        numArray.update(1,2)
        self.assertEqual(8, numArray.sumRange(0,2))

    def test_range_sum_query_using_fenwick_tree_aka_BIT(self) -> None:
        nums = [1, 3, 5]
        numArray = NumArrayUsingBIT(nums)
        self.assertEqual(9, numArray.sumRange(0,2))
        numArray.update(1,2)
        self.assertEqual(8, numArray.sumRange(0,2))

if __name__ == "__main__":
    unittest.main()