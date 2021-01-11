# LeetCode - Problem 973 - K Closest Points to Origin

#### Problem

We have a list of points on the plane.  Find the `K` closest points to the origin `(0, 0)`.

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 
```
Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
``` 

Note:

* `1 <= K <= points.length <= 10000`
* `-10000 < points[i][0] < 10000`
* `-10000 < points[i][1] < 10000`

#### Solution

Using a kd-tree to solve this problem is an overkill. 
However, it will be a nice approach for discussion if this follow up question comes up during interview.
**What if I have 10 million points now and I have to perform the search 10000 times? How would you optimize it?**

Let's first have a review of some solutions that we have already come across:

1. **Sorting - O(NlogN)**, since we need to sort the entire list of points
```python
from typing import List

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
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:K]
```
1. **Max Heap - O(NlogK)**, since we need to maintain a priority queue of size K and extract the closest K points with a bunch of heap push and pop
```python
from typing import List

import heapq

class Solution:


    # Solution 2 : Min Heap
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
    def kClosest_min_heap(self, points: List[List[int]], K: int) -> List[List[int]]:
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

    # Solution 2a : Max Heap
    #
    # TC: O(N * logK) ; SC: O(K)
    #
    def distance_from_origin(self, point: List[int]):
        return point[0] * point[0] + point[1] * point[1]

    def kClosest_max_heap(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        max_heap = []

        for i in range(K):
            dis = self.distance_from_origin(points[i])
            heapq.heappush(max_heap, (-dis, points[i]))

        for i in range(K, len(points)):
            dis = self.distance_from_origin(points[i])
            if max_heap[0][0] < -dis:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-dis, points[i]))

        return [point for (dis, point) in list(max_heap)]
```
1. **Quick Select - O(N) on average**, a modified quick-sort like algorithm (proof of complexity not shown here)
```python
from typing import List

class Solution:

    # Solution 3 : Quick Select
    #
    # Create tuple based on distance and index of each points.
    # Apply quick select on the list to find the Kth number.
    #
    # Average time: O(n)
    # Space: O(n)
    #
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
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
```

As we can see, if we have `N=10000000` and we have to perform the search over a large number of times, 
even **O(N)** solution may seem to be inefficient in this extreme case.

So, what can we do? We can make use of a data structure called **kd-tree** which are particularly good at searching 2D (or 3D,...,KD) points in **logarithmic time**.
Since the points on the 2D planes aren't going to change (in most cases) during the query, we can **prepocess** the points by constructing a kd-tree to store them for later queries.

kd-tree has the following comeplexity:

1. **Build the tree - O(NlogN)**, building the tree requires presorting the points and find the medians (but we only need to do this once).
1. **Search, Insert, Delete - O(logN)**, similar to how a normal binary tree works (with a tree balancing mechanism)

Now, as we can see, it greatly reduces the time complexity for each nearest neighbor query to **O(logN)**, and if we need to find the K closest points, the total complexity will be **O(KlogN)**. 
This is great if we have a lof of points and we are only interested in a few neighbors.

Coding a kd-tree seems daunting and not feasible in a 45-min interviews. 
However, in Python, there is some data science library which allows you to build a tree and perform the search in just a few lines of code! 
Since interviewers typically don't expect you to code an actual kd-tree, using the following code may not only show that you have insights of more advanced data structure, but also demostrate that you have practical experience implementing them with pre-existing libraries.

```python
from typing import List

from scipy import spatial

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        tree = spatial.KDTree(points)
		# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
        distance, idx = tree.query(x=[0,0], k=K, p=2) 
        return [points[i] for i in idx] if K > 1 else [points[idx]]
```

* Reference: [https://en.wikipedia.org/wiki/K-d_tree](https://en.wikipedia.org/wiki/K-d_tree)

NOTE: There is also a possible solution using the **Divide and Conquer** approach as shown below:

```python
from typing import List

class Solution:
    # Solution 5 : Divide and Conquer
    '''
    we use the divide and conquer method to find the kth largest number
    meanwhile due to the partition function
    after the kth number is found the points[0] to points[k-1] are all points are
    all answers
    '''
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
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
```