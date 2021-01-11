from typing import List

import heapq

import unittest

class Solution:

    # Solution 1 : Sorting
    #
    # Even though this algorighm has not optimal algorithmic complexity (it is O(n log n) vs heaps O(n log k)), on leetcode it can work faster. 
    # Just sort points by distances and choose the smallest K of them.
    #
    # good one for the initial submit at the interview.
    #
    # TC: O(N*logN)
    #
    def kClosest_sorting_solution_1(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:K]

    # Solution 2 : Max Heap
    #
    # IDEA   : We keep a max heap of size K.
    #          For each item, we insert an item to our heap.
    #          If inserting an item makes heap size larger than k, then we immediately pop an item 
    #          after inserting ( heappushpop ).
    # 
    # Runtime: Inserting an item to a heap of size k take O(logK) time.
    #          And we do this for each item points.
    #          So runtime is O(N * logK) where N is the length of points.
    # Space  : O(K) for our heap. 
    #
    # TC: O(N * logK) ; SC: O(K)
    #
    def kClosest_max_heap_solution_2(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-dist, point))
            if len(heap) > K:
                heapq.heappop(heap)
    
        return [tuple[1] for tuple in heap]

    # Solution 3 : Quick Select
    #
    # Create tuple based on distance and index of each points.
    # Apply quick select on the list to find the Kth number.
    #
    # Average time: O(n)
    # Space: O(n)
    #
    def kClosest_quick_select_solution_3(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) <= K:
            return points
        
        dis_lst = [(p[0]*p[0]+p[1]*p[1], idx) for idx, p in enumerate(points)]
            
        s, e = 0, len(points)-1
        while True:
            pivot = self.Q_select(dis_lst, s, e)
            if pivot == K:
                break
            if pivot > K:
                e = pivot - 1
            else:
                s = pivot + 1
        return [points[i] for _, i in dis_lst[:K]]
    
    def Q_select(self, lst, s, e):
        left, right, pivot = s, e-1, e
        while left <= right:
            if lst[left] <= lst[pivot]:
                left += 1
            elif lst[right] >= lst[pivot]:
                right -= 1
            else:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        lst[left], lst[pivot] = lst[pivot], lst[left]
        return left

    # Solution 4 : Divide and Conquer
    '''
    we use the divide and conquer method to find the kth largest number
    meanwhile due to the partition function
    after the kth number is found the points[0] to points[k-1] are all points are
    all answers
    '''
    def kClosest_divide_and_conquer_solution_4(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        l = []
        ans = self.findkth(points, 0, len(points) - 1, K)
        for i in range(0, K, 1):
            l.append([])
            l[i].append(points[i][0])
            l[i].append(points[i][1])
        
        return l
        
    def findkth(self, points, low, high, k):
        pivot = self.partition(points, low, high)
        if pivot == k - 1:
            return points[k-1]
        if pivot > k - 1:
            return self.findkth(points, low, pivot - 1, k)
        return self.findkth(points, pivot + 1, high, k)
    '''
	the partition function is the same as the quicksort with median of three partition function
	and return the pivot
	'''
    def partition(self, points, low, high):
        mid = self.mid3(points, low, high)
        self.swap(points, low, mid)
        key = points[low][0] * points[low][0] + points[low][1] * points[low][1]
        while (low < high):
            while (low < high and key <= points[high][0] * points[high][0] + points[high][1] * points[high][1]):
                high -= 1
            self.swap(points, low, high)
            
            while (low < high and key >= points[low][0] * points[low][0] + points[low][1] * points[low][1]):
                low += 1
            self.swap(points, low, high)
        return low
    
    def mid3(self, nums, low, high):
        mid = (low + high) // 2
        l = []
        l.append(nums[low])
        l.append(nums[mid])
        l.append(nums[high])
        l.sort()
        if l[1] == nums[low]:
            return low
        elif l[1] == nums[mid]:
            return mid
        return high

    def swap(self, nums, index1, index2):
        tmp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = tmp
        return


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_kClosest(self) -> None:
        sol = Solution()
        for points, K, solution in (
            [
                [[1,3],[-2,2]],
                1,
                [[-2,2]]
            ],
            [
                [[3,3],[5,-1],[-2,4]],
                2,
                [[-2,4],[3,3]]
            ]
        ):
            self.assertEqual(
                sorted(solution),
                sorted(sol.kClosest_sorting_solution_1(points, K))
            )
            self.assertEqual(
                sorted(solution),
                sorted(sol.kClosest_max_heap_solution_2(points, K))
            )
            self.assertEqual(
                sorted(solution),
                sorted(sol.kClosest_quick_select_solution_3(points, K))
            )
            self.assertEqual(
                sorted(solution),
                sorted(sol.kClosest_divide_and_conquer_solution_4(points, K))
            )

 
if __name__ == "__main__":
    unittest.main()
