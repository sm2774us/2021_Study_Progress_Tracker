# Google_Study_Progress_Tracker

Study Tracks:
* [1. Coding Interview](#1-coding-interview)
  - [a. Data Structures](#a-data-structures)
    - [a.1 Array](#a1-array)    
    - [a.2 String](#a2-string)    
    - [a.3 Linked List](#a3-linked-list)
    - [a.4 Stack and Queue](#a4-stack-and-queue)
    - [a.5 Tree](#a5-tree)
    - [a.6 Heap](#a6-heap)
    - [a.7 Hash Table](#a7-hash-table)
    - [a.8 Graph](#a8-graph)
    - [a.9 Union Find AKA Disjoint Set](#a9-union-find-aka-disjoint-set)
  - [b. Advanced Data Structures](#b-advanced-data-structures)
  - [c. Algorithms](#c-algorithms)
    - [c.1 Two Pointers](#c1-two-pointers)
    - [c.2 Sliding Window](#c2-sliding-window)
    - [c.3 BFS](#c3-bfs)
    - [c.4 DFS](#c4-dfs)
    - [c.5 Backtracking](#c5-backtracking)
    - [c.6 Dynamic Programming](#c6-dynamic-programming)
    - [c.7 Divide and Conquer](#c7-divide-and-conquer)
  - [d. Famous Algorithms](#d-algorithms)
  - [e. Game Theory](#e-algorithms)
    - [e.1 Minimax](#a1-minimax)
  - [f. Math](#f-math)
  - [g. Bit Manipulation](#g-bit-manipulation)
  - [h. Complexity Analysis](#h-complexity-analysis)
  - [h. NP Complete](#h-np-complete)
* [2. System Design Interview](#2-system-design-interview)
* [3. Behavioral Interview](#3-behavioral-interview)

## 1. Coding Interview

### a. Data Structures

#### a.1 Array
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Array | [LC-904 - Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_001_Array/001_LC-904-Solution.py) | Google          | :white_check_mark: |
| Array | **LC-683 - K Empty Slots** | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_001_Array/002_LC-683-Solution.py) | Google          | :white_check_mark: |
|       | ---------- | | | |
|       | There is a garden with N slots. In each slot, there is a flower.
|       | The N flowers will bloom one by one in N days. In each day,
|       | there will be exactly one flower blooming and it will be in the status of blooming since then.
|       | ---------- | | | |
|       | Given an array flowers consists of number from 1 to N.
|       | Each number in the array represents the place where the flower will open in that day.
|       | ---------- | | | |
|       | For example, flowers[i] = x means that the unique flower that blooms at day i
|       | will be at position x, where i and x will be in the range from 1 to N.
|       | ---------- | | | |
|       | Also given an integer k, you need to output in which day there exists two flowers
|       | in the status of blooming, and also the number of flowers between them is k and
|       | these flowers are not blooming.
|       | ---------- | | | |
|       | If there isn't such day, output -1.
|       | ---------- | | | |
|       | Example 1:
|       | Input: 
|       | flowers: [1,3,2]
|       | k: 1
|       | Output: 2
|       | Explanation: In the second day, the first and the third flower have become blooming.
|       | ---------- | | | |
|       | Example 2:
|       | Input: 
|       | flowers: [1,2,3]
|       | k: 1
|       | Output: -1
|       | Note:
|       | The given array will be in the range [1, 20000].
| Array | [LC-001 - Two Sum](https://leetcode.com/problems/two-sum/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_001_Array/003_LC-001-Solution.py) | Google          | :white_check_mark: |

#### a.2 String
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| String | [LC-929 - Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_002_String/001_LC-929-Solution.py) | Google    | :white_check_mark: |
| String | **LC-681 - Next Closest Time**  | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_002_String/002_LC-681-Solution.py) | Google    | :white_check_mark: |
|        | ---------- | | | |
|        | Given a time represented in the format “HH:MM”, form the next closest time by reusing the current digits.  | | | |
|        | There is no limit on how many times a digit can be reused.  | | | |
|        | You may assume the given input string is always valid. For example, “01:34”, “12:09” are all valid. “1:34”, “12:9” are all invalid.  | | | |
|        | ---------- | | | |
|        | **Example 1:** | | | |
|        | **Input:** "19:34" | | | |
|        | **Output:** "19:39" | | | |
|        | **Explanation:** The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.  | | | |
|        | **Example 2:**  | | | |
|        | **Input:** "23:59"  | | | |
|        | **Output:** "22:22"  | | | |
|        | **Explanation:** The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.  | | | |
| String | [LC-482 - License Key Formatting](https://leetcode.com/problems/license-key-formatting/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_002_String/003_LC-482-Solution.py) | Google    | :white_check_mark: |
| String | **LC-159 - Longest Substring with At Most Two Distinct Characters** | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_002_String/004_LC-159-Solution.py) | Google    | :white_check_mark: |
|        | ---------- | | | |
|        | Given a string s , find the length of the longest substring t that contains at most 2 distinct characters. | | | |
|        | Example 1:
|        | ---------- | | | |
|        | Input: "eceba"
|        | Output: 3
|        | Explanation: t is "ece" which its length is 3.
|        | ---------- | | | |
|        | Example 2:
|        | ---------- | | | |
|        | Input: "ccaabbb"
|        | Output: 5
|        | Explanation: t is "aabbb" which its length is 5.
| String | [LC-844 - Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_002_String/005_LC-844-Solution.py) | Google    | :white_check_mark: |

#### a.3 Linked List

#### a.4 Stack and Queue
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Stack and Queue | [LC-975 - Odd Even Jump](https://leetcode.com/problems/odd-even-jump/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_004_Stack_and_Queue/001_LC-975-Solution.py) | Google          | :white_check_mark: |

#### a.5 Tree
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Tree - BST | [LC-975 - Odd Even Jump](https://leetcode.com/problems/odd-even-jump/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_005_Tree/001_LC-975-Solution.py) | Google          | :white_check_mark: |

#### a.6 Heap
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Heap - Max Heap | [LC-857 - Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_006_Heap/001_LC-857-Solution.py)<br>[Proof](001_Coding_Interview/Google/a_Data_Structures/a_006_Heap/001_LC-857-Solution.md) | Google          | :white_check_mark: |

#### a.7 Hash Table

#### a.8 Graph

#### a.9 Union Find AKA Disjoint Set
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| UnionFind | [LC-399 - Evaluate Division](https://leetcode.com/problems/evaluate-division/) | [Solution](001_Coding_Interview/Google/a_Data_Structures/a_009_Union_Find_aka_Disjoint_Set/001_LC-399-Solution.py) | Google          | :white_check_mark: |

### b. Advanced Data Structures

### c. Algorithms

### c.1 Two Pointers
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Two Pointers | [LC-844 - Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | [Solution](001_Coding_Interview/Google/c_Algorithms/c_001_Two_Pointers/001_LC-844-Solution.py) | Google    | :white_check_mark: |

### c.2 Sliding Window

### c.3 BFS
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Graph - BFS | [LC-1197 - Minimum Knight Moves](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwihl_y6uoPuAhUrrVkKHdTBAiIQFjAAegQIBRAC&url=https%3A%2F%2Fleetcode.com%2Fproblems%2Fminimum-knight-moves%2F&usg=AOvVaw0G2kkPFMkczwckNHIlXhae) | [Solution](001_Coding_Interview/Google/c_Algorithms/c_003_BFS/001_LC-1197-Solution.py) | Google          | :white_check_mark: |

### c.4 DFS
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Graph - DFS | [LC-399 - Evaluate Division](https://leetcode.com/problems/evaluate-division/) | [Solution](001_Coding_Interview/Google/c_Algorithms/c_004_DFS/001_LC-399-Solution.py) | Google          | :white_check_mark: |
| Graph - DFS+Backtracking | [LC-489 - Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) | [Solution](001_Coding_Interview/Google/c_Algorithms/c_004_DFS/002_LC-489-Solution.py) | Google          | :white_check_mark: |
|        | ---------- | | | |
|        | Given a robot cleaner in a room modeled as a grid.  | | | |
|        | Each cell in the grid can be empty or blocked.  | | | |
|        | The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.  | | | |
|        | When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.  | | | |
|        | Design an algorithm to clean the entire room using only the 4 given APIs.  | | | |
|        | ---------- | | | |
|        | **Example:** | | | |
|        | ---------- | | | |
|        | **Input:** | | | |
|        | room = [ | | | |
|        |   [1,1,1,1,1,0,1,1], | | | |
|        |   [1,1,1,1,1,0,1,1], | | | |
|        |   [1,0,1,1,1,1,1,1], | | | |
|        |   [0,0,0,1,0,0,0,0], | | | |
|        |   [1,1,1,1,1,1,1,1] | | | |
|        | ], | | | |
|        | row = 1, | | | |
|        | col = 3 | | | |
|        | **Explanation:** | | | |
|        | All grids in the room are marked by either 0 or 1. | | | |
|        | 0 means the cell is blocked, while 1 means the cell is accessible. | | | |
|        | The robot initially starts at the position of row=1, col=3. | | | |
|        | From the top left corner, its position is one row below and three columns right.  | | | |
| Graph - DFS | [LC-947 - Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | [Solution](001_Coding_Interview/Google/c_Algorithms/c_004_DFS/003_LC-947-Solution.py) | Google          | :white_check_mark: |

### c.5 Backtracking

### c.6 Dynamic Programming
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Dynamic Programming | [LC-1197 - Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/) | [Solution](001_Coding_Interview/Google/c_Algorithms/c_006_Dynamic_Programming/001_LC-1197-Solution.py) | Google          | :white_check_mark: |

### c.7 Divide and Conquer
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |

### c.8 Prefix Summ
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |

### c.9 Range Sum
| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Range Sum Query | [LC-308- Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) | [Solution](001_Coding_Interview/Google/c_Algorithms/c_009_RangeSum/001_LC-308-Solution.py) | Google          | :white_check_mark: |

### d. Famous Algorithms

### e. Game Theory

### e.1 Minimax

| Topic  | Problems Attempted | Solutions | Companies | Completed Status  |
| ------ | -----------------  | --------- | --------- | ----------------- |
| Tree - BST | [LC-843 - Guess the Word](https://leetcode.com/problems/guess-the-word/) | [Solution](001_Coding_Interview/Google/e_Game_Theory/e_001_Minimax/001_LC-843-Solution.py) | Google          | :white_check_mark: |

## 2. System Design Interview

## 3. Behavioral Interview
