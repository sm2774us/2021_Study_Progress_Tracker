# Time:  O(n^3)
# Space: O(1)

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        return sum(abs(arr[i]-arr[j]) <= a and
                   abs(arr[j]-arr[k]) <= b and
                   abs(arr[k]-arr[i]) <= c 
                   for i in range(len(arr)-2)
                       for j in range(i+1, len(arr)-1)
                           for k in range(j+1, len(arr)))
  
