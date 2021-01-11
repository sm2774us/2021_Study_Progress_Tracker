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
1. **Max Heap - O(NlogK)**, since we need to maintain a priority queue of size K and extract the closest K points with a bunch of heap push and pop
1. **Quick Select - O(N) on average**, a modified quick-sort like algorithm (proof of complexity not shown here)

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
from scipy import spatial
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        tree = spatial.KDTree(points)
		# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
        distance, idx = tree.query(x=[0,0], k=K, p=2) 
        return [points[i] for i in idx] if K > 1 else [points[idx]]
```

* Reference: [https://en.wikipedia.org/wiki/K-d_tree](https://en.wikipedia.org/wiki/K-d_tree)