from typing import List
# Time:  O(n)
# Space: O(1)
# class Solution(object):
#     #
#     # According to Wikipedia: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order,
#     # a man named Narayana Pandita presented the following simple algorithm to solve this problem
#     # in the 14th century.
#     #
#     # 1) Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists,
#     #    just reverse nums and done.
#     # 2) Find the largest index l > k such that nums[k] < nums[l].
#     # 3) Swap nums[k] and nums[l].
#     # 4) Reverse the sub-array nums[k + 1:].
#     #
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         k, l = -1, 0
#         for i in reversed(range(len(nums)-1)):
#             if nums[i] < nums[i+1]:
#                 k = i
#                 break
#             else:
#                 nums.reverse()
#                 return
#
#         for i in reversed(range(k+1, len(nums))):
#             if nums[i] > nums[k]:
#                 l = i
#                 break
#         nums[k], nums[l] = nums[l], nums[k]
#         nums[k+1:] = nums[:k:-1]

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

'''
The largest permutation means all numbers are mono decreasing from left to right.
Try to find a number at index i, which is smaller than its right next, which is at index i + 1
Then from index i + 1 to the right end, find the smallest number which is larger than nums[i].
Let's say that number is at index j. Then swap nums[i] and nums[j].
Now from index i+1 to the right end, the numbers are still mono decreasing.
Because we want the lowest possible order, we reverse nums[i+1:]
Time: O(n)
Space: O(1)
May Binary search to speed up the process of find nums[j].
'''

'''
Example of "next lexicographic permutation":
--------------------------------------------
The next lexicographic permutation is the next largest number that can be formed from the given digits. 

Let us take an example:

We will write all permutations of the digits 0 1 2 3 4 5 in lexicographic order below:

0 1 2 3 4 5
0 1 2 3 5 4 # Note that always the last two digits are swapped if they are in order. Here 4 5 is changed to 5 4.
0 1 2 4 3 5
0 1 2 4 5 3
0 1 2 5 3 4
0 1 2 5 4 3 # Note that if last two digits are not in order, we have to look for change of order digit and go to the 
              next lexicographic number. Here 2 will become 3.
0 1 3 2 4 5 # After that 2 4 5 are in order...
0 1 3 2 5 4
0 1 3 4 2 5
0 1 3 4 5 2 # Note that if last two digits are not in order, we have to look for change of order digit and go 
              to the next lexicographic number. Here 4 will become 5.
0 1 3 5 2 4 # Always check this change of order from the right side. After this switch, 2 4 are put in order.
0 1 3 5 4 2
0 1 4 2 3 5
0 1 4 2 5 3
0 1 4 3 2 5
0 1 4 3 5 2 # Note again that always the last two digits are swapped if they are in order. Here 2 5 is changed to 5 2.
0 1 4 5 2 3
0 1 4 5 3 2 # Note that if last two digits are not in order (3 > 2), we have to look for change of order digit 
              and go to the next lexicographic number. Here 4 will become 5.
0 1 5 2 3 4 # After that 2 3 4 are in order...
0 1 5 2 4 3
0 1 5 3 2 4
0 1 5 3 4 2
0 1 5 4 2 3
0 1 5 4 3 2

....

Please try to fill in the next few ones.
'''
# Time:  O(n)
# Space: O(1)
class Solution2(object):
    # def nextPermutation(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     k, l = -1, 0
    #     for i in range(len(nums)-1):
    #         if nums[i] < nums[i+1]:
    #             k = i
    #
    #     if k == -1:
    #         nums.reverse()
    #         return
    #
    #     for i in range(k+1, len(nums)):
    #         if nums[i] > nums[k]:
    #             l = i
    #     nums[k], nums[l] = nums[l], nums[k]
    #     nums[k+1:] = nums[:k:-1]


    def nextPermutation(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        nums_len = len(nums)
        j = i = nums_len - 1
        while i >= 0:
            if i < nums_len-1 and nums[i] < nums[i+1]:
                break
            i -= 1
        if i == -1: # Current numbers are the largest permutation
            nums.reverse()
            return
        while j > i: # nums[i+1:] are mono decreasing, the first nums[j] we meet that is larger than nums[i] must be the answer.
            if nums[j] > nums[i]:
                break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        return