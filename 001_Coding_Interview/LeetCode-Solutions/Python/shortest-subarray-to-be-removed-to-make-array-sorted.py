# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        j = -1
        for j in reversed(range(1, len(arr))):
            if arr[j-1] > arr[j]:
                break
        else:
            return 0
        result = j
        for i in range(j):
            if i and arr[i] < arr[i-1]:
                break
            while j < len(arr) and arr[i] > arr[j]:
                j += 1
            result = min(result, (j-i+1)-2)
        return result


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1, len(arr)):
            if arr[i-1] <= arr[i]:
                continue
            j = len(arr)-1
            while j > i and (j == len(arr)-1 or arr[j] <= arr[j+1]) and arr[i-1] <= arr[j]:
                j -= 1
            result = j-i+1
            break
        for j in reversed(range(len(arr)-1)):
            if arr[j] <= arr[j+1]:
                continue
            i = 0
            while i < j and (i == 0 or arr[i-1] <= arr[i]) and arr[i] <= arr[j+1]:
                i += 1
            result = min(result, j-i+1)
            break
        return result
