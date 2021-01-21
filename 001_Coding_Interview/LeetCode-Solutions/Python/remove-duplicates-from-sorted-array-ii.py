from typing import List

# Time:  O(n)
# Space: O(1)
#
# Solution - Visualization :
#
# nums = [1,1,1,2,2,3]
# removeDuplicates(nums)
# i=1 ; last=0; A[i]=1; A[last]=1; same=False
# [1, 1, 1, 2, 2, 3]
# i=2 ; last=1; A[i]=1; A[last]=1; same=True
# [1, 1, 1, 2, 2, 3]
# i=3 ; last=1; A[i]=2; A[last]=1; same=True
# [1, 1, 1, 2, 2, 3]
# i=4 ; last=2; A[i]=2; A[last]=2; same=False
# [1, 1, 2, 2, 2, 3]
# i=5 ; last=3; A[i]=3; A[last]=2; same=True
# [1, 1, 2, 2, 2, 3]
# 5
#
class Solution(object):
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        last, i, same = 0, 1, False
        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                last += 1
                A[last] = A[i]
            i += 1

        return last + 1


# Time:  O(n)
# Space: O(1)
#
#
# Solution 2
#
# For those who have trouble grasping the logic, the key is that num[i] is replaced by the value of the
# current element and i steps forward, but stops replacing if nums[i-2] = current,
# indicating that the current identical sequence has the maximum length of 2.
# Essentially, we are walking through the array and copying over each element to the left pointer
# unless the last sequence of identical elements hits the limit of length 2... then we wait
# until we find a new element and start copying over again.
#
# Complexity:
# time complexity is O(n)
# Space complexity is O(1): we do it in-place as asked.
#
#
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i

# Time:  O(n)
# Space: O(1)
#
# Solution 3: Two Pointers
#
# I think both Remove Duplicates from Sorted Array I and II could be solved in a consistent and more general way
# by allowing the duplicates to appear k times (k = 1 for problem I and k = 2 for problem II).
# Here is my way: we need a count variable to keep how many times the duplicated element appears,
# if we encounter a different element, just set counter to 1, if we encounter a duplicated one,
# we need to check this count, if it is already k, then we need to skip it, otherwise, we can keep this element.
# The following is the implementation:
#
# Complexity: time complexity is O(n), we move our two pointers only in one direction. Space complexity is O(1): we do it in-place as asked.
#
class Solution3:
    def removeDuplicates(self, nums):
        if not nums: return 0
        slow = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    continue
            else:
                count = 1
            nums[slow] = nums[i]
            slow += 1
        return slow