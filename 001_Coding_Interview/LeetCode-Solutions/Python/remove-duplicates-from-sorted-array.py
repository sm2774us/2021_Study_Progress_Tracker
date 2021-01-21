from typing import List

# Time:  O(n)
# Space: O(1)

# Solution - Visualization :
#
# nums = [1,1,1,2,2,3,3,4,4]
# removeDuplicates(nums)
#
# last=0; i=0; A[i]=1; A[last]=1
# [1, 1, 1, 2, 2, 3, 3, 4, 4]
# last=0; i=1; A[i]=1; A[last]=1
# [1, 1, 1, 2, 2, 3, 3, 4, 4]
# last=0; i=2; A[i]=1; A[last]=1
# [1, 1, 1, 2, 2, 3, 3, 4, 4]
# last=0; i=3; A[i]=2; A[last]=1
# [1, 1, 1, 2, 2, 3, 3, 4, 4]
# last=1; i=4; A[i]=2; A[last]=2
# [1, 2, 1, 2, 2, 3, 3, 4, 4]
# last=1; i=5; A[i]=3; A[last]=2
# [1, 2, 1, 2, 2, 3, 3, 4, 4]
# last=2; i=6; A[i]=3; A[last]=3
# [1, 2, 3, 2, 2, 3, 3, 4, 4]
# last=2; i=7; A[i]=4; A[last]=3
# [1, 2, 3, 2, 2, 3, 3, 4, 4]
# last=3; i=8; A[i]=4; A[last]=4
# [1, 2, 3, 4, 2, 3, 3, 4, 4]
# 4
class Solution(object):
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        last = 0
        for i in range(len(A)):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
        return last + 1

# Solution 2 - Two Pointers
#
# Time:  O(n)
# Space: O(1)
#
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:

        prev, size = None, len(nums)
        unique_pos, current_pos = 0, 0

        while current_pos < size:

            if nums[current_pos] != prev:
                # catch and move unique element
                nums[unique_pos] = nums[current_pos]

                # update index for next unique element
                unique_pos += 1

            # update previous element for next iteration
            prev = nums[current_pos]

            # update index for linear element scan
            current_pos += 1

        return unique_pos