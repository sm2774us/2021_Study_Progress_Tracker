# LeetCode - Problem 158 - Read N Characters Given Read4 II - Call multiple times

The return value is the actual number of characters read. For example, it returns `3` 
if there is only `3` characters left in the file.
By using the `read4` API, implement the function `int read(char *buf, int n)` that 
reads `n` characters from the file.

#### Examples

```
Example 1:
Given buf = "abc"
read("abc", 1) // returns "a"
read("abc", 2); // returns "bc"
read("abc", 1); // returns ""

Example 2:
Given buf = "abc"
read("abc", 4) // returns "abc"
read("abc", 1); // returns ""
```

**Note:**

The read function may be called multiple times.

**Intuition:**

**The meaning of the problem:** This title differs from the [previous question - LeetCode Problem 157 - Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4/) 
is repeatedly calling `read()` function, so you need to store 4 character cache `buffer` defined as **Global Variable**. 
In addition, we also need to define the **start index** and **length of the buffer** `buffer[]` as  global variables. 
In this problem, it is necessary to note that, once it finished calling `read()`, 
there may be nothing left in the buffer to read at all, 
so consider the next call to `read()` function, the operation on the buffer. 

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
