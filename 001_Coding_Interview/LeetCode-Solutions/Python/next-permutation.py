# Time:  O(n)
# Space: O(1)

class Solution(object):
    #
    # According to Wikipedia: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order,
    # a man named Narayana Pandita presented the following simple algorithm to solve this problem
    # in the 14th century.
    #
    # 1) Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists,
    #    just reverse nums and done.
    # 2) Find the largest index l > k such that nums[k] < nums[l].
    # 3) Swap nums[k] and nums[l].
    # 4) Reverse the sub-array nums[k + 1:].
    #
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i+1]:
                k = i
                break
            else:
                nums.reverse()
                return

        for i in reversed(range(k+1, len(nums))):
            if nums[i] > nums[k]:
                l = i
                break
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]
        

# Time:  O(n)
# Space: O(1)
class Solution2(object):
    #
    # According to Wikipedia: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order,
    # a man named Narayana Pandita presented the following simple algorithm to solve this problem
    # in the 14th century.
    #
    # 1) Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists,
    #    just reverse nums and done.
    # 2) Find the largest index l > k such that nums[k] < nums[l].
    # 3) Swap nums[k] and nums[l].
    # 4) Reverse the sub-array nums[k + 1:].
    #
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i

        if k == -1:
            nums.reverse()
            return

        for i in range(k+1, len(nums)):
            if nums[i] > nums[k]:
                l = i
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]
