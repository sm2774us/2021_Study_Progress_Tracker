# LeetCode - Problem 560 - Subarray Sum Equals K - LeetCode

#### Solution 
##### **1. Hash Table**

Summary of algo:
The overall structure is similar to that of [1. Two Sum](https://leetcode.com/problems/two-sum/discuss/444887/Python3C%2B%2B-hash-table). 
For the given array of integers, progressively compute the prefix sum. 
For a given step with prefix sum prefix, check if prefix-k has been 
seen before (tracked in a dictionary). If so, add the number of times 
prefix-k was seen to the answer.

Although no number was seen in the beginning, this is effective to 
seeing a 0, and thus seen was initialized to be {0:1}.

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = prefix = 0
        seen = {0:1}
        for num in nums: 
            prefix += num #prefix sum 
            ans += seen.get(prefix-k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
        return ans 
```

#### **Complexity Analysis:**
* **Time complexity :** `O(N)`. 
  
We traverse the list containing n elements once. Each look up in a hash table costs `O(1)` time.
So `n` insertions and `n` lookups in a hash table takes expected time of `O(N)`.
  
* **Space complexity :** `O(N)`.
  
The extra space required depends on the number of items stored in the dictionary, 
which stores at most n elements.
