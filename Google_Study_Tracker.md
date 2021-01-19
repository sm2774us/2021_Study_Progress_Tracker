# Google_Study_Progress_Tracker

## Algorithms

* [Bit Manipulation](#bit-manipulation)
* [Array](#array)
* [String](#string)
* [Linked List](#linked-list)
* [Stack](#stack)
* [Queue](#queue)
* [Binary Heap](#binary-heap)
* [Tree](#tree)
* [Hash Table](#hash-table)
* [Math](#math)
* [Two Pointers](#two-pointers)
* [Sort](#sort)
* [Recursion](#recursion)
* [Binary Search](#binary-search)
* [Binary Search Tree](#binary-search-tree)
* [Breadth-First Search](#breadth-first-search)
* [Depth-First Search](#depth-first-search)
* [Backtracking](#backtracking)
* [Dynamic Programming](#dynamic-programming)
* [Greedy](#greedy)
* [Graph](#graph)
* [Geometry](#geometry)
* [Simulation](#simulation)
* [Design](#design)
* [Concurrency](#concurrency)

## Database

* [SQL](#sql)


## Shell

* [Shell Script](#shell-script)

## Reference

* C++
    * [STL Time Complexity (Detailed)](http://www.cplusplus.com/reference/stl/)
    * [STL Time Complexity (Summary)](http://john-ahlgren.blogspot.com/2013/10/stl-container-performance.html)
    * [Data Structure and Algorithms Cheat Sheet](https://github.com/gibsjose/cpp-cheat-sheet/blob/master/Data%20Structures%20and%20Algorithms.md)
* Python
    * [Time Complexity](https://wiki.python.org/moin/TimeComplexity)

## Bit Manipulation
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0136 | [Single Number](https://leetcode.com/problems/single-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/single-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/single-number.py) | _O(n)_       | _O(1)_          | Easy         |||
0137 | [Single Number II](https://leetcode.com/problems/single-number-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/single-number-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/single-number-ii.py) | _O(n)_ | _O(1)_          | Medium         |||
0190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-bits.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-bits.py) | _O(1)_        | _O(1)_          | Easy           |||
0191  |[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-1-bits.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-1-bits.py) | _O(1)_ | _O(1)_          | Easy           |||
0268| [Missing Number](https://leetcode.com/problems/missing-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/missing-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/missing-number.py)  | _O(n)_ |  _O(1)_ | Medium         | LintCode ||
0318| [Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-product-of-word-lengths.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-product-of-word-lengths.py)  | _O(n)_ ~ _O(n^2)_ |  _O(n)_ | Medium         || Bit Manipulation, Counting Sort, Pruning|
0393 | [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/utf-8-validation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/utf-8-validation.py) | _O(n)_ | _O(1)_ | Medium | |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Array
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0026 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-duplicates-from-sorted-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-duplicates-from-sorted-array.py) | _O(n)_       | _O(1)_         | Easy           || Two Pointers
0027 | [Remove Element](https://leetcode.com/problems/remove-element/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-element.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-element.py) | _O(n)_      | _O(1)_         | Easy           ||
0031 | [Next Permutation](https://leetcode.com/problems/next-permutation/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/next-permutation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/next-permutation.py) | _O(n)_  | _O(1)_          | Medium         || Tricky
0041 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/first-missing-positive.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/first-missing-positive.py) | _O(n)_ | _O(1)_ | Hard         || Tricky
0048 | [Rotate Image](https://leetcode.com/problems/rotate-image/)   | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rotate-image.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rotate-image.py) | _O(n^2)_      | _O(1)_         | Medium         ||
0054 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/spiral-matrix.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/spiral-matrix.py) | _O(m * n)_    | _O(1)_         | Medium         ||
0059 | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/spiral-matrix-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/spiral-matrix-ii.py) | _O(n^2)_ | _O(1)_      | Medium         ||
0066 | [Plus One](https://leetcode.com/problems/plus-one/)      | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/plus-one.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/plus-one.py)   | _O(n)_           | _O(1)_         | Easy           || 
0073 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/set-matrix-zeroes.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/set-matrix-zeroes.py) | _O(m * n)_ | _O(1)_    | Medium         ||
0080 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-duplicates-from-sorted-array-ii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-duplicates-from-sorted-array-ii.py) | _O(n)_       | _O(1)_         | Medium         || Two Pointers
0118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/pascals-triangle.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/pascals-triangle.py) | _O(n^2)_ | _O(1)_        | Easy           || 
0119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/pascals-triangle-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/pascals-triangle-ii.py) | _O(n^2)_ | _O(1)_  | Easy           ||
0121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/best-time-to-buy-and-sell-stock.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-time-to-buy-and-sell-stock.py) | _O(n)_ | _O(1)_ | Easy ||
0128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-consecutive-sequence.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-consecutive-sequence.py) | _O(n)_ | _O(n)_ | Hard         || Tricky
0157 | [Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/read-n-characters-given-read4.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/read-n-characters-given-read4.py) | _O(n)_ | _O(1)_ | Easy           |🔒|
0158 | [Read N Characters Given Read4 II - Call multiple times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/read-n-characters-given-read4-ii-call-multiple-times.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/read-n-characters-given-read4-ii-call-multiple-times.py) | _O(n)_ | _O(1)_ | Hard |🔒|
0163 | [Missing Ranges](https://leetcode.com/problems/missing-ranges/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/missing-ranges.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/missing-ranges.py) | _O(n)_      | _O(1)_          | Medium         | 🔒 |
0169 | [Majority Element](https://leetcode.com/problems/majority-element/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/majority-element.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/majority-element.py) | _O(n)_ | _O(1)_          | Easy           | | `Boyer–Moore Majority Vote Algorithm`
0215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/kth-largest-element-in-an-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/kth-largest-element-in-an-array.py)| _O(n)_ on average | _O(1)_ |  Medium | EPI| Quick Select, Tri Partition
0228 | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/summary-ranges.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/summary-ranges.py)| _O(n)_ | _O(1)_ | Medium | |
0229 | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/majority-element-ii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/majority-element-ii.py) | _O(n)_ | _O(1)_          | Medium           | |
0238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/product-of-array-except-self.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/product-of-array-except-self.py) | _O(n)_ | _O(1)_          | Medium           | LintCode |
0240 | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/search-a-2d-matrix-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/search-a-2d-matrix-ii.py) | _O(m + n)_ | _O(1)_ | Medium   | EPI, LintCode |
0243| [Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/shortest-word-distance.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/shortest-word-distance.py)  | _O(n)_ |  _O(1)_ | Easy         |🔒||
0277| [Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-the-celebrity.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-the-celebrity.py)  | _O(n)_ |  _O(1)_ | Medium         |🔒, EPI ||
0289| [Game of Life](https://leetcode.com/problems/game-of-life/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/game-of-life.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/game-of-life.py)  | _O(m * n)_ |  _O(1)_ | Medium         |||
0296| [Best Meeting Point](https://leetcode.com/problems/best-meeting-point/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/best-meeting-point.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-meeting-point.py)  | _O(m * n)_ |  _O(m + n)_ | Hard         |🔒||
0334| [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/increasing-triplet-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/increasing-triplet-subsequence.py)  | _O(n)_ |  _O(1)_ | Medium         |||
0370| [Range Addition](https://leetcode.com/problems/range-addition/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-addition.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-addition.py)  | _O(k + n)_ |  _O(1)_ | Medium         |🔒||
0384| [Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/shuffle-an-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/shuffle-an-array.py)  | _O(n)_ |  _O(n)_ | Medium         | EPI ||
0412| [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/fizz-buzz.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/fizz-buzz.py)  | _O(n)_ |  _O(1)_ | Easy         |||
0414| [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/third-maximum-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/third-maximum-number.py)  | _O(n)_ |  _O(1)_ | Easy         |||
0419| [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/battleships-in-a-board.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/battleships-in-a-board.py)  | _O(m * n)_ |  _O(1)_ | Medium         |||
0448| [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-all-numbers-disappeared-in-an-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-all-numbers-disappeared-in-an-array.py)  | _O(n)_ |  _O(1)_ | Easy         |||
0665| [Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/non-decreasing-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/non-decreasing-array.py)  | _O(n)_ |  _O(1)_ | Easy         |||
0674 | [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-continuous-increasing-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-continuous-increasing-subsequence.py) | _O(n)_ | _O(1)_ | Easy ||
0683 | [K Empty Slots](https://leetcode.com/problems/k-empty-slots/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/k-empty-slots.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/k-empty-slots.py) | _O(n)_ | _O(n)_ | Hard ||
0717 | [1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/1-bit-and-2-bit-characters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/1-bit-and-2-bit-characters.py) | _O(n)_ | _O(1)_ | Easy || Greedy
0723 | [Candy Crush](https://leetcode.com/problems/candy-crush/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/candy-crush.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/candy-crush.py) | _O((R * C)^2)_ | _O(1)_ | Medium ||
0724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-pivot-index.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-pivot-index.py) | _O(n)_ | _O(1)_ | Easy ||
0729 | [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/my-calendar-i.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/my-calendar-i.py) | _O(nlogn)_ | _O(n)_ | Medium ||
0731 | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/my-calendar-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/my-calendar-ii.py) | _O(n^2)_ | _O(n)_ | Medium ||
0732 | [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/my-calendar-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/my-calendar-iii.py) | _O(nlogn)_ ~ _O(n^2)_ | _O(n)_ | Hard ||
0766 | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/toeplitz-matrix.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/toeplitz-matrix.py) | _O(m * n)_ | _O(1)_ | Easy ||
0768 | [Max Chunks To Make Sorted II](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-chunks-to-make-sorted-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-chunks-to-make-sorted-ii.py) | _O(n)_ | _O(n)_ | Hard || Mono Stack
0769 | [Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-chunks-to-make-sorted.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-chunks-to-make-sorted.py) | _O(n)_ | _O(1)_ | Medium ||
0792 | [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-matching-subsequences.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-matching-subsequences.py) | _O(n + w)_ | _O(k)_ | Medium ||
0794 | [Valid Tic-Tac-Toe State](https://leetcode.com/problems/valid-tic-tac-toe-state/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-tic-tac-toe-state.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-tic-tac-toe-state.py) | _O(1)_ | _O(1)_ | Medium ||
0803 | [Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/bricks-falling-when-hit.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/bricks-falling-when-hit.py) | _O(r * c)_ | _O(r * c)_ | Hard || Union Find
0807 | [Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-increase-to-keep-city-skyline.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-increase-to-keep-city-skyline.py) | _O(n^2)_ | _O(n)_ | Medium ||
0821 | [Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/shortest-distance-to-a-character.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/shortest-distance-to-a-character.py) | _O(n)_ | _O(1)_ | Easy ||
0830 | [Positions of Large Groups](https://leetcode.com/problems/positions-of-large-groups/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/positions-of-large-groups.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/positions-of-large-groups.py) | _O(n)_ | _O(1)_ | Easy ||
0832 | [Flipping an Image](https://leetcode.com/problems/flipping-an-image/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/flipping-an-image.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/flipping-an-image.py) | _O(n^2)_ | _O(1)_ | Easy ||
0835 | [Image Overlap](https://leetcode.com/problems/image-overlap/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/image-overlap.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/image-overlap.py) | _O(n^4)_ | _O(n^2)_ | Medium ||
0840 | [Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/magic-squares-in-grid.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/magic-squares-in-grid.py) | _O(m * n)_ | _O(1)_ | Easy ||
0845 | [Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-mountain-in-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-mountain-in-array.py) | _O(n)_ | _O(1)_ | Medium ||
0849 | [Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximize-distance-to-closest-person.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximize-distance-to-closest-person.py) | _O(n)_ | _O(1)_ | Easy ||
0905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sort-array-by-parity.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sort-array-by-parity.py) | _O(n)_ | _O(1)_      | Easy         ||
0941 | [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-mountain-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-mountain-array.py) | _O(n)_ | _O(1)_      | Easy         ||
0947 | [Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/most-stones-removed-with-same-row-or-column.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/most-stones-removed-with-same-row-or-column.py) | _O(n)_ | _O(n)_      | Medium         || Union Find
1007 | [Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-domino-rotations-for-equal-row.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-domino-rotations-for-equal-row.py) | _O(n)_ | _O(1)_      | Medium         ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## String
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0005| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-palindromic-substring.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-palindromic-substring.py) | _O(n)_ | _O(n)_ |  Medium || `Manacher's Algorithm`
0006| [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/zigzag-conversion.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/zigzag-conversion.py) | _O(n)_ | _O(1)_        | Easy           ||
0008| [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/string-to-integer-atoi.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/string-to-integer-atoi.py) | _O(n)_ | _O(1)_ | Easy      ||
0014| [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-common-prefix.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-common-prefix.py) | _O(n * k)_   | _O(1)_  | Easy           ||
0028| [Implement strStr()](https://leetcode.com/problems/implement-strstr/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/implement-strstr.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/implement-strstr.py) | _O(n + k)_   | _O(k)_  | Easy           || `KMP Algorithm`
0038| [Count and Say](https://leetcode.com/problems/count-and-say/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/count-and-say.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/count-and-say.py)| _O(n * 2^n)_  | _O(2^n)_        | Easy           ||
0043| [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/multiply-strings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/multiply-strings.py) | _O(m * n)_ | _O(m + n)_  | Medium         ||
0067| [Add Binary](https://leetcode.com/problems/add-binary/)    | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/add-binary.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/add-binary.py) | _O(n)_          | _O(1)_          | Easy           ||
0068| [Text Justification](https://leetcode.com/problems/text-justification/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/text-justification.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/text-justification.py) | _O(n)_ | _O(1)_      | Hard           ||
0125| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-palindrome.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-palindrome.py) | _O(n)_  | _O(1)_         | Easy           ||
0161| [One Edit Distance](https://leetcode.com/problems/one-edit-distance/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/one-edit-distance.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/one-edit-distance.py) | _O(m + n)_ | _O(1)_    | Medium         |🔒 |
0165| [Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/compare-version-numbers.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/compare-version-numbers.py) | _O(n)_ | _O(1)_ | Easy     ||
0242| [Valid Anagram](https://leetcode.com/problems/valid-anagram/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-anagram.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-anagram.py) | _O(n)_       | _O(1)_         | Easy         | LintCode |
0271| [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/encode-and-decode-strings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/encode-and-decode-strings.py) | _O(n)_ | _O(1)_ | Medium         | 🔒 |
0273| [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/integer-to-english-words.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/integer-to-english-words.py) | _O(1)_ | _O(1)_ | Hard         | |
0415| [Add Strings](https://leetcode.com/problems/add-strings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/add-strings.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/add-strings.py) | _O(n)_ | _O(1)_ | Easy         | |
0443| [String Compression](https://leetcode.com/problems/string-compression/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/string-compression.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/string-compression.py) | _O(n)_ | _O(1)_ | Easy         | |
0459| [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/repeated-substring-pattern.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/repeated-substring-pattern.py) | _O(n)_ | _O(n)_ | Easy         || `KMP Algorithm` |
0468| [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/validate-ip-address.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/validate-ip-address.py) | _O(1)_ | _O(1)_ | Medium         | |
0482| [License Key Formatting](https://leetcode.com/problems/license-key-formatting/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/license-key-formatting.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/license-key-formatting.py) | _O(n)_ | _O(1)_ | Easy | |
0524| [Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-word-in-dictionary-through-deleting.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-word-in-dictionary-through-deleting.py) | _O((d * l)  * logd)_ | _O(1)_ | Medium         | | Sort
0527| [Word Abbreviation](https://leetcode.com/problems/word-abbreviation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-abbreviation.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-abbreviation.py) | _O(n * l)_ ~ _O(n^2 * l^2)_  | _O(n * l)_ | Hard         |🔒|
0539| [Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-time-difference.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-time-difference.py) | _O(nlogn)_ | _O(n)_ | Medium         | |
0556| [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/next-greater-element-iii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/next-greater-element-iii.py) | _O(1)_ | _O(1)_ | Medium         | |
0564| [Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-the-closest-palindrome.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-the-closest-palindrome.py) | _O(l)_ | _O(l)_ | Hard         | |
0591| [Tag Validator](https://leetcode.com/problems/tag-validator/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/tag-validator.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/tag-validator.py) | _O(n)_ | _O(n)_ | Hard         | |
0616| [Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/add-bold-tag-in-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/add-bold-tag-in-string.py) | _O(n * d * l)_ | _O(n)_ |  Medium | 🔒 |
0647| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindromic-substrings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindromic-substrings.py) | _O(n)_ | _O(n)_ |  Medium || `Manacher's Algorithm`
0680| [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-palindrome-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-palindrome-ii.py) | _O(n)_  | _O(1)_         | Easy           ||
0681| [Next Closest Time](https://leetcode.com/problems/next-closest-time/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/next-closest-time.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/next-closest-time.py) | _O(1)_  | _O(1)_         | Medium           ||
0686 | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/repeated-string-match.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/repeated-string-match.py) | _O(n + m)_ | _O(1)_ | Easy || `Rabin-Karp Algorithm` |
0720| [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-word-in-dictionary.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-word-in-dictionary.py) | _O(n)_ | _O(t)_ | Easy         || Trie |
0722| [Remove Comments](https://leetcode.com/problems/remove-comments/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-comments.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-comments.py) | _O(n)_ | _O(k)_ | Medium         |||
0751| [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/ip-to-cidr.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/ip-to-cidr.py) | _O(n)_ | _O(1)_ | Medium         |||
0804| [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/unique-morse-code-words.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/unique-morse-code-words.py) | _O(n)_ | _O(n)_ | Easy         |||
0806| [Number of Lines To Write String](https://leetcode.com/problems/number-of-lines-to-write-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-lines-to-write-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-lines-to-write-string.py) | _O(n)_ | _O(1)_ | Easy         |||
0809| [Expressive Words](https://leetcode.com/problems/expressive-words/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/expressive-words.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/expressive-words.py) | _O(n + s)_ | _O(l + s)_ | Medium         |||
0819| [Most Common Word](https://leetcode.com/problems/most-common-word/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/most-common-word.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/most-common-word.py) | _O(m + n)_ | _O(m + n)_ | Easy         |||
0833| [Find And Replace in String](https://leetcode.com/problems/find-and-replace-in-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-and-replace-in-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-and-replace-in-string.py) | _O(n + m)_ | _O(n)_ | Medium         |||
0859 | [Buddy Strings](https://leetcode.com/problems/buddy-strings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/buddy-strings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/buddy-strings.py) | _O(n)_ | _O(1)_ | Easy ||
0890 | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-and-replace-pattern.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-and-replace-pattern.py) | _O(n * l)_ | _O(1)_ | Medium ||
0929 | [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/unique-email-addresses.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/unique-email-addresses.py) | _O(n * l)_ | _O(n * l)_ | Easy ||
0939 | [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-area-rectangle.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-area-rectangle.py) | _O(n^1.5)_ on average | _O(n)_ | Medium ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Linked List
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0002| [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/add-two-numbers.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/add-two-numbers.py) | _O(n)_   | _O(1)_          | Medium         ||
0021| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/merge-two-sorted-lists.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/merge-two-sorted-lists.py) | _O(n)_ | _O(1)_ | Easy         ||
0023| [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/merge-k-sorted-lists.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/merge-k-sorted-lists.py) | _O(nlogk)_| _O(1)_| Hard          | | Heap, Divide and Conquer
0024| [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/swap-nodes-in-pairs.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/swap-nodes-in-pairs.py)   | _O(n)_          | _O(1)_          | Easy         ||
0025| [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-nodes-in-k-group.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-nodes-in-k-group.py) | _O(n)_       | _O(1)_         | Hard         ||
0082| [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-duplicates-from-sorted-list-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-duplicates-from-sorted-list-ii.py) | _O(n)_       | _O(1)_         | Medium         ||
0083| [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-duplicates-from-sorted-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-duplicates-from-sorted-list.py) | _O(n)_       | _O(1)_         | Easy           ||
0092| [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-linked-list-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-linked-list-ii.py) | _O(n)_       | _O(1)_         | Medium         || 
0138| [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/copy-list-with-random-pointer.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/copy-list-with-random-pointer.py) | _O(n)_   | _O(1)_          | Medium         ||
0160| [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/intersection-of-two-linked-lists.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/intersection-of-two-linked-lists.py) | _O(m + n)_ | _O(1)_         | Easy           ||
0203| [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-linked-list-elements.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-linked-list-elements.py) | _O(n)_       | _O(1)_         | Easy         || 
0206| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-linked-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-linked-list.py) | _O(n)_       | _O(1)_         | Easy         || 
0234| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindrome-linked-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-linked-list.py) | _O(n)_       | _O(1)_         | Easy         ||
0237| [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/delete-node-in-a-linked-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/delete-node-in-a-linked-list.py) | _O(1)_       | _O(1)_         | Easy         | LintCode |
0328| [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/odd-even-linked-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/odd-even-linked-list.py) | _O(n)_       | _O(1)_         | Medium         | |
0369| [Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/plus-one-linked-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/plus-one-linked-list.py) | _O(n)_       | _O(1)_         | Medium         | 🔒 | Two Pointers |
0725 | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/split-linked-list-in-parts.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/split-linked-list-in-parts.py) | _O(n + k)_ | _O(1)_ | Medium ||
0817 | [Linked List Components](https://leetcode.com/problems/linked-list-components/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/linked-list-components.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/linked-list-components.py) | _O(m + n)_ | _O(m)_ | Medium ||
0986 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/interval-list-intersections.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/interval-list-intersections.py) | _O(m + n)_ | _O(1)_ | Medium ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Stack
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0020| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-parentheses.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-parentheses.py) | _O(n)_        | _O(n)_          | Easy           ||
0032| [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-valid-parentheses.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-valid-parentheses.py) | _O(n)_ | _O(1)_ | Hard   ||
0084| [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/largest-rectangle-in-histogram.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/largest-rectangle-in-histogram.py) | _O(n)_ | _O(n)_ | Hard || Mono Stack, DP
0085| [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximal-rectangle.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximal-rectangle.py)| _O(m * n)_ | _O(n)_         | Hard           | EPI | Mono Stack
0101| [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/symmetric-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/symmetric-tree.py) | _O(n)_      | _O(h)_          | Easy           ||
0150| [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/evaluate-reverse-polish-notation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/evaluate-reverse-polish-notation.py)| _O(n)_| _O(n)_| Medium          ||
0155| [Min Stack](https://leetcode.com/problems/min-stack/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/min-stack.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/min-stack.py)  | _O(n)_          | _O(1)_          | Easy           ||
0224| [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/basic-calculator.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/basic-calculator.py) | _O(n)_| _O(n)_| Hard || 
0227| [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/basic-calculator-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/basic-calculator-ii.py) | _O(n)_| _O(n)_| Medium || 
0232| [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/implement-queue-using-stacks.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/implement-queue-using-stacks.py) | _O(1), amortized_| _O(n)_| Easy | EPI, LintCode | 
0341| [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/flatten-nested-list-iterator.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/flatten-nested-list-iterator.py) | _O(n)_        | _O(h)_          | Medium           |🔒| Iterator |
0394| [Decode String](https://leetcode.com/problems/decode-string/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/decode-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/decode-string.py) | _O(n)_        | _O(n)_          | Medium           |||
0636| [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/exclusive-time-of-functions.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/exclusive-time-of-functions.py) | _O(n)_  | _O(n)_         | Medium           ||
0736| [Parse Lisp Expression](https://leetcode.com/problems/parse-lisp-expression/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/parse-lisp-expression.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/parse-lisp-expression.py) | _O(n^2)_  | _O(n^2)_         | Hard           ||
0739| [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/daily-temperatures.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/daily-temperatures.py) | _O(n)_  | _O(n)_         | Medium           ||
0770| [Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/basic-calculator-iv.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/basic-calculator-iv.py) | add: _O(d * t)_<br> sub: _O(d * t)_<br> mul: _O(d * t^2)_<br> eval: _O(d * t)_ <br> to_list: _O(d * tlogt)_  | _O(e + d * t)_ | Hard           ||
0772| [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/basic-calculator-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/basic-calculator-iii.py) | _O(n)_  | _O(n)_         | Hard           ||
0853| [Car Fleet](https://leetcode.com/problems/car-fleet/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/car-fleet.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/car-fleet.py) | _O(nlogn)_  | _O(n)_         | Medium           ||
0872| [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/leaf-similar-trees.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/leaf-similar-trees.py) | _O(n)_  | _O(h)_         | Easy           ||


<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Queue
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0239| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sliding-window-maximum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sliding-window-maximum.py) | _O(n)_        | _O(k)_          | Hard           | EPI, LintCode | Mono Deque |
0281| [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/zigzag-iterator.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/zigzag-iterator.py) | _O(n)_        | _O(k)_          | Medium           |🔒||
0346| [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/moving-average-from-data-stream.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/moving-average-from-data-stream.py) | _O(1)_        | _O(w)_          | Easy           |🔒||
0933| [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-recent-calls.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-recent-calls.py) | _O(1)_ on average       | _O(w)_          | Easy           |||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Binary Heap
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0264| [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/ugly-number-ii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/ugly-number-ii.py)  | _O(n)_ | _O(1)_ | Medium         | CTCI, LintCode | BST, Heap |
0295| [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-median-from-data-stream.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-median-from-data-stream.py)  | _O(nlogn)_ | _O(n)_ | Hard         | EPI, LintCode | BST, Heap |
0358| [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rearrange-string-k-distance-apart.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rearrange-string-k-distance-apart.py) | _O(n)_        | _O(n)_          | Hard           |🔒| Greedy, Heap |
0373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-k-pairs-with-smallest-sums.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-k-pairs-with-smallest-sums.py) | _O(k * log(min(n, m, k)))_ | _O(min(n, m, k))_ | Medium |||
0378 | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/kth-smallest-element-in-a-sorted-matrix.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/kth-smallest-element-in-a-sorted-matrix.py) | _O(k * log(min(n, m, k)))_ | _O(min(n, m, k))_ | Medium | LintCode ||
0407 | [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/trapping-rain-water-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/trapping-rain-water-ii.py) | _O(m * n * (logm + logn))_ | _O(m * n)_ | Hard | LintCode ||
0632 | [Smallest Range](https://leetcode.com/problems/smallest-range/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/smallest-range.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/smallest-range.py) | _O(nlogk)_ | _O(k)_ | Hard |||
0703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/kth-largest-element-in-a-stream.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/kth-largest-element-in-a-stream.py) | _O(nlogk)_ | _O(k)_ | Easy |||
0846 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/hand-of-straights.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/hand-of-straights.py) | _O(nlogn)_ | _O(n)_ | Medium |||
0855 | [Exam Room](https://leetcode.com/problems/exam-room/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/exam-room.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/exam-room.py) | seat: _O(logn)_ <br> leave: _O(logn)_ | _O(n)_ | Medium || BST, Hash |
0857 | [Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-cost-to-hire-k-workers.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-cost-to-hire-k-workers.py) | _O(nlogn)_ | _O(n)_ | Hard || Sort |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Tree
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0094 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-inorder-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-inorder-traversal.py) | _O(n)_| _O(1)_| Medium           || `Morris Traversal` | 
0099 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/recover-binary-search-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/recover-binary-search-tree.py) | _O(n)_| _O(1)_| Hard  || `Morris Traversal` 
0144 | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-preorder-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-preorder-traversal.py) | _O(n)_| _O(1)_| Medium || `Morris Traversal` 
0208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/implement-trie-prefix-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/implement-trie-prefix-tree.py) | _O(n)_ | _O(1)_ | Medium || Trie
0211 | [Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/add-and-search-word-data-structure-design.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/add-and-search-word-data-structure-design.py) | _O(min(n, h))_ | _O(min(n, h))_ | Medium || Trie, DFS
0226| [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/invert-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/invert-binary-tree.py) | _O(n)_ | _O(h)_, _O(w)_ | Easy ||
0297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/serialize-and-deserialize-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/serialize-and-deserialize-binary-tree.py) | _O(n)_ | _O(h)_ | Hard | LintCode | DFS
0307 | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-sum-query-mutable.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-sum-query-mutable.py) | ctor: _O(n)_, update: _O(logn)_, query:  _O(logn)_ | _O(n)_ | Medium | LintCode | DFS, Segment Tree, BIT, Fenwick Tree
0308 | [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-sum-query-2d-mutable.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-sum-query-2d-mutable.py) | ctor: _O(m * n)_, update: _O(logm * logn)_, query:  _O(logm * logn)_ | _O(m * n)_ | Hard | 🔒 | DFS, Quad Tree, 2D BIT, 2D Fenwick Tree
0315|[Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/count-of-smaller-numbers-after-self.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/count-of-smaller-numbers-after-self.py)| _O(nlogn)_ | _O(n)_ | Hard | LintCode | BST, BIT, Fenwick Tree, Divide and Conquer, Merge Sort |
0529 | [Minesweeper](https://leetcode.com/problems/minesweeper/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minesweeper.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minesweeper.py) | _O(m * n)_ | _O(m + n)_ | Medium    || 
0543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/diameter-of-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/diameter-of-binary-tree.py) | _O(n)_ | _O(h)_ | Easy    || 
0572 |[Subtree of Another Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/subtree-of-another-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/subtree-of-another-tree.py)| _O(m * n)_ | _O(h)_ | Easy | | |
0652 |[Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-duplicate-subtrees.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-duplicate-subtrees.py)| _O(n)_ | _O(n)_ | Medium | | DFS, Hash |
0653 |[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/two-sum-iv-input-is-a-bst.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/two-sum-iv-input-is-a-bst.py)| _O(n)_ | _O(h)_ | Easy | | Two Pointers |
0662 | [Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-width-of-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-width-of-binary-tree.py) | _O(n)_ | _O(h)_ | Medium | | DFS
0684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/redundant-connection.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/redundant-connection.py) | _O(n)_ | _O(n)_ | Medium || Union Find
0685 | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/redundant-connection-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/redundant-connection-ii.py) | _O(n)_ | _O(n)_ | Hard || Union Find
0687 | [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-univalue-path.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-univalue-path.py) | _O(n)_ | _O(h)_ | Easy ||
0850 | [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rectangle-area-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rectangle-area-ii.py) | _O(nlogn)_ | _O(n)_ | Hard || Segment Tree |
0863 | [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/all-nodes-distance-k-in-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/all-nodes-distance-k-in-binary-tree.py) | _O(n)_ | _O(n)_ | Medium || DFS + BFS |
0889 | [Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/construct-binary-tree-from-preorder-and-postorder-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/construct-binary-tree-from-preorder-and-postorder-traversal.py) | _O(n)_ | _O(h)_ | Medium || DFS, stack |
0938| [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-sum-of-bst.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-sum-of-bst.py) | _O(n)_          | _O(h)_          | Medium           || DFS |
0951| [Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/flip-equivalent-binary-trees.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/flip-equivalent-binary-trees.py) | _O(n)_          | _O(h)_          | Medium           || DFS |
0979| [Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/distribute-coins-in-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/distribute-coins-in-binary-tree.py) | _O(n)_          | _O(h)_          | Medium           || DFS |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Hash Table
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0001| [Two Sum](https://leetcode.com/problems/two-sum/)      | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/two-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/two-sum.py)      | _O(n)_         | _O(n)_          | Easy         ||
0003| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-substring-without-repeating-characters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-substring-without-repeating-characters.py) | _O(n)_ | _O(1)_ | Medium ||
0030| [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/substring-with-concatenation-of-all-words.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/substring-with-concatenation-of-all-words.py) | _O((m + n) * k)_ | _O(n * k)_ | Hard          ||
0036| [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-sudoku.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-sudoku.py) | _O(9^2)_         | _O(9)_          | Easy           ||
0049| [Group Anagrams](https://leetcode.com/problems/group-anagrams/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/group-anagrams.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/group-anagrams.py)   | _O(n * glogg)_          | _O(n)_          | Medium         ||
0076| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-window-substring.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-window-substring.py) | _O(n)_ | _O(k)_ | Hard          ||
0149| [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-points-on-a-line.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-points-on-a-line.py) | _O(n^2)_ | _O(n)_ | Hard          ||
0159| [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-substring-with-at-most-two-distinct-characters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-substring-with-at-most-two-distinct-characters.py) | _O(n)_ | _O(1)_ | Hard         |🔒|
0187| [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/repeated-dna-sequences.py) | _O(n)_       | _O(n)_          | Medium         ||
0202| [Happy Number](https://leetcode.com/problems/happy-number/)      | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/happy-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/happy-number.py)   | _O(k)_  | _O(k)_          | Easy          ||
0204| [Count Primes](https://leetcode.com/problems/count-primes/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/count-primes.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/count-primes.py) | _O(nlog(logn))_        | _O(n)_          | Easy           || `Sieve of Eratosthenes`
0205| [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/isomorphic-strings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/isomorphic-strings.py) | _O(n)_ | _O(1)_       | Easy           || 
0217| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/contains-duplicate.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/contains-duplicate.py) | _O(n)_        | _O(n)_          | Easy           ||
0219| [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/contains-duplicate-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/contains-duplicate-ii.py) | _O(n)_        | _O(n)_          | Easy           ||
0246| [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/strobogrammatic-number.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/strobogrammatic-number.py)  | _O(n)_ | _O(1)_ | Easy         |🔒||
0249| [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/group-shifted-strings.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/group-shifted-strings.py)  | _O(nlogn)_ | _O(n)_ | Easy         |🔒||
0266| [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindrome-permutation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-permutation.py)  | _O(n)_ |  _O(1)_ | Easy         |🔒||
0288| [Unique Word Abbreviation](https://leetcode.com/problems/unique-word-abbreviation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/unique-word-abbreviation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/unique-word-abbreviation.py)  | ctor: _O(n)_, lookup: _O(1)_ | _O(k)_ | Easy         |🔒||
0290| [Word Pattern](https://leetcode.com/problems/word-pattern/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-pattern.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-pattern.py)  | _O(n)_ | _O(c)_ | Easy         | variant of [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) ||
0299| [Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/bulls-and-cows.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/bulls-and-cows.py)  | _O(n)_ | _O(1)_ | Easy         |||
0305| [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-islands-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-islands-ii.py) | _O(k)_ | _O(k)_| Hard         | LintCode, 🔒 | Union Find
0336| [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindrome-pairs.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-pairs.py) | _O(n * k^2)_          | _O(n * k)_          | Hard             | | |
0340| [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)|  [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-substring-with-at-most-k-distinct-characters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-substring-with-at-most-k-distinct-characters.py) | _O(n)_ | _O(1)_ | Hard         |🔒|
0387| [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/first-unique-character-in-a-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/first-unique-character-in-a-string.py) | _O(n)_| _O(n)_| Easy |||
0388| [Longest Absolute File Path](https://leetcode.com/problems/longest-absolute-file-path/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-absolute-file-path.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-absolute-file-path.py) | _O(n)_| _O(d)_| Medium || Stack |
0438| [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-all-anagrams-in-a-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-all-anagrams-in-a-string.py) | _O(n)_          | _O(1)_          | Easy           ||
0447| [Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-boomerangs.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-boomerangs.py) | _O(n^2)_          | _O(n)_          | Easy           ||
0470| [Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/implement-rand10-using-rand7.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/implement-rand10-using-rand7.py) | _O(1)_          | _O(1)_          | Medium           ||
0560| [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/subarray-sum-equals-k.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/subarray-sum-equals-k.py) | _O(n)_ | _O(n)_ | Medium         | |
0721| [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/accounts-merge.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/accounts-merge.py) | _O(nlogn)_ | _O(n)_| Medium         || Union Find
0734| [Sentence Similarity](https://leetcode.com/problems/sentence-similarity/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sentence-similarity.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sentence-similarity.py) | _O(n + p)_ | _O(p)_| Easy         ||
0737| [Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sentence-similarity-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sentence-similarity-ii.py) | _O(n + p)_ | _O(p)_| Medium         || Union Find
0760 | [Find Anagram Mappings](https://leetcode.com/problems/find-anagram-mappings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-anagram-mappings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-anagram-mappings.py) | _O(n)_ | _O(n)_ | Easy ||
0771 | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/jewels-and-stones.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/jewels-and-stones.py) | _O(m + n)_ | _O(n)_ | Easy ||
0811 | [Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/subdomain-visit-count.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/subdomain-visit-count.py) | _O(n)_ | _O(n)_ | Easy ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Math
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0007| [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-integer.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-integer.py) | _O(1)_ | _O(1)_         | Easy           ||
0009| [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindrome-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-number.py) | _O(1)_ | _O(1)_        | Easy           ||
0012| [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/integer-to-roman.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/integer-to-roman.py) | _O(n)_ | _O(1)_          | Medium         ||
0013| [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/roman-to-integer.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/roman-to-integer.py) | _O(n)_ | _O(1)_          | Easy           ||
0029| [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/divide-two-integers.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/divide-two-integers.py)    | _O(1)_       | _O(1)_         | Medium         ||
0050| [Pow(x, n)](https://leetcode.com/problems/powx-n/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/powx-n.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/powx-n.py)     | _O(1)_       | _O(1)_       | Medium         ||
0060| [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/permutation-sequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/permutation-sequence.py) | _O(n^2)_ | _O(n)_  | Medium         || `Cantor Ordering`
0065| [Valid Number](https://leetcode.com/problems/valid-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-number.py) | _O(n)_         | _O(1)_          | Hard           || `Automata`
0089| [Gray Code](https://leetcode.com/problems/gray-code/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/gray-code.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/gray-code.py)  | _O(2^n)_        | _O(1)_          | Medium         ||
0166| [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/fraction-to-recurring-decimal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/fraction-to-recurring-decimal.py)  | _O(logn)_ | _O(1)_ | Medium         ||
0168| [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/excel-sheet-column-title.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/excel-sheet-column-title.py) | _O(logn)_ | _O(1)_ | Easy ||
0171| [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/excel-sheet-column-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/excel-sheet-column-number.py) | _O(n)_ | _O(1)_ | Easy  ||
0248| [Strobogrammatic Number III](https://leetcode.com/problems/strobogrammatic-number-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/strobogrammatic-number-iii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/strobogrammatic-number-iii.py)  | _O(5^(n/2))_ | _O(n)_ | Hard         |🔒||
0343 | [Integer Break](https://leetcode.com/problems/integer-break/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/integer-break.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/integer-break.py) | _O(logn)_ | _O(1)_ | Medium || Tricky, DP |
0365 | [Water and Jug Problem](https://leetcode.com/problems/water-and-jug-problem/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/water-and-jug-problem.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/water-and-jug-problem.py) | _O(logn)_ | _O(1)_ | Medium || `Bézout's identity` |
0386 | [Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/lexicographical-numbers.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/lexicographical-numbers.py) | _O(n)_ | _O(1)_ | Medium |||
0398 | [Random Pick Index](https://leetcode.com/problems/random-pick-index/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/random-pick-index.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/random-pick-index.py) | _O(n)_ | _O(1)_ | Medium || `Reservoir Sampling` |
0400 | [Nth Digit](https://leetcode.com/problems/nth-digit/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/nth-digit.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/nth-digit.py) | _O(logn)_ | _O(1)_ | Easy |||
0470 | [Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/implement-rand10-using-rand7.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/implement-rand10-using-rand7.py) | _O(1)_ | _O(1)_ | Medium |||
0497 | [Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/random-point-in-non-overlapping-rectangles.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/random-point-in-non-overlapping-rectangles.py) | ctor: _O(n)_ <br> pick: _O(logn)_ | _O(n)_ | Medium |||
0528 | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/random-pick-with-weight.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/random-pick-with-weight.py) | ctor: _O(n)_ <br> pick: _O(logn)_ | _O(n)_ | Medium |||
0640| [Solve the Equation](https://leetcode.com/problems/solve-the-equation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/solve-the-equation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/solve-the-equation.py) | _O(n)_ | _O(n)_ | Medium || |
0800 | [Similar RGB Color](https://leetcode.com/problems/similar-rgb-color/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/similar-rgb-color.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/similar-rgb-color.py) | _O(1)_ | _O(1)_ | Easy |🔒||
0836 | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rectangle-overlap.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rectangle-overlap.py) | _O(1)_ | _O(1)_ | Easy |||
0858 | [Mirror Reflection](https://leetcode.com/problems/mirror-reflection/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/mirror-reflection.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/mirror-reflection.py) | _O(1)_ | _O(1)_ | Medium |||
0914 | [X of a Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/x-of-a-kind-in-a-deck-of-cards.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/x-of-a-kind-in-a-deck-of-cards.py) | _O(n * (logn)^2)_ | _O(n)_      | Easy         ||
0963 | [Minimum Area Rectangle II](https://leetcode.com/problems/minimum-area-rectangle-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-area-rectangle-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-area-rectangle-ii.py) | _O(n^2)_ ~ _O(n^3)_ | _O(n^2)_      | Medium         ||
0972 | [Equal Rational Numbers](https://leetcode.com/problems/equal-rational-numbers/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/equal-rational-numbers.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/equal-rational-numbers.py) | _O(1)_ | _O(1)_      | Hard         ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Sort
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0056| [Merge Intervals](https://leetcode.com/problems/merge-intervals/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/merge-intervals.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/merge-intervals.py) | _O(nlogn)_  | _O(1)_        | Hard           ||
0057| [Insert Interval](https://leetcode.com/problems/insert-interval/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/insert-interval.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/insert-interval.py) | _O(n)_    | _O(1)_          | Hard           ||
0075| [Sort Colors](https://leetcode.com/problems/sort-colors/)   | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sort-colors.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sort-colors.py) | _O(n)_         | _O(1)_          | Medium         || Tri Partition
0148| [Sort List](https://leetcode.com/problems/sort-list/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sort-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sort-list.py)  | _O(nlogn)_      | _O(logn)_       | Medium         ||
0218| [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/the-skyline-problem.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/the-skyline-problem.py) | _O(nlogn)_   | _O(n)_        | Hard         || Sort, BST|
0253| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/meeting-rooms-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/meeting-rooms-ii.py) | _O(nlogn)_   | _O(n)_        | Medium         |🔒| |
0274| [H-Index](https://leetcode.com/problems/h-index/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/h-index.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/h-index.py)  | _O(n)_ | _O(n)_ | Medium         || Counting Sort |
0280| [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/wiggle-sort.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/wiggle-sort.py) | _O(n)_   | _O(1)_        | Medium         |🔒| |
0324| [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/wiggle-sort-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/wiggle-sort-ii.py) | _O(n)_  on average | _O(1)_        | Medium         | variant of [Sort Colors](https://leetcode.com/problems/sort-colors/) | Tri Partition |
0347| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/top-k-frequent-elements.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/top-k-frequent-elements.py) | _O(n)_ | _O(n)_        | Medium         | | Quick Select, Heap, Bucket Sort |
0406| [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/queue-reconstruction-by-height.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/queue-reconstruction-by-height.py) | _O(n * sqrt(n))_ | _O(n)_        | Medium         | | Tricky |
0451| [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sort-characters-by-frequency.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sort-characters-by-frequency.py) | _O(n)_ | _O(n)_        | Medium         | | |
0692| [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/top-k-frequent-words.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/top-k-frequent-words.py) | _O(n + klogk)_ on average | _O(n)_        | Medium         | | Quick Select, Heap, Bucket Sort |
0973| [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/k-closest-points-to-origin.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/k-closest-points-to-origin.py) | _O(n)_ on average | _O(1)_        | Easy         | | Quick Select, Heap|

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Two Pointers
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0016 | [3 Sum Closest](https://leetcode.com/problems/3sum-closest/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/3sum-closest.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/3sum-closest.py) | _O(n^2)_       | _O(1)_          | Medium         || Two Pointers
0018| [4 Sum](https://leetcode.com/problems/4sum/)         | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/4sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/4sum.py)        | _O(n^3)_    | _O(1)_    | Medium         || Two Pointers
0019| [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-nth-node-from-end-of-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-nth-node-from-end-of-list.py) | _O(n)_       | _O(1)_         | Medium         || 
0141| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/linked-list-cycle.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/linked-list-cycle.py) | _O(n)_ | _O(1)_         | Easy         || 
0142| [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/linked-list-cycle-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/linked-list-cycle-ii.py) | _O(n)_ | _O(1)_   | Medium         ||
0143| [Reorder List](https://leetcode.com/problems/reorder-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reorder-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reorder-list.py) | _O(n)_          |  _O(1)_         | Medium         ||  
0167| [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/two-sum-ii-input-array-is-sorted.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/two-sum-ii-input-array-is-sorted.py) | _O(n)_   | _O(1)_         | Medium         | |
0209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-size-subarray-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-size-subarray-sum.py) | _O(n)_ | _O(1)_ |  Medium | | Binary Search, Sliding Window
0259 | [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/3sum-smaller.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/3sum-smaller.py) | _O(n^2)_ | _O(1)_          | Medium         | 🔒, LintCode |
0283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/move-zeroes.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/move-zeroes.py) | _O(n)_ | _O(1)_          | Easy         | |
0287| [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-the-duplicate-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-the-duplicate-number.py)   | _O(n)_          | _O(1)_          | Hard       | | Binary Search, Two Pointers |
0344| [Reverse String](https://leetcode.com/problems/reverse-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-string.py) | _O(n)_ | _O(1)_ | Easy         | |
0349| [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/intersection-of-two-arrays.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/intersection-of-two-arrays.py) | _O(m + n)_ | _O(min(m, n))_ | Easy         | EPI | Hash, Binary Search
0350| [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/intersection-of-two-arrays-ii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/intersection-of-two-arrays-ii.py) | _O(m + n)_ | _O(1)_ | Easy         | EPI | Hash, Binary Search
0360| [Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sort-transformed-array.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sort-transformed-array.py) | _O(n)_ | _O(1)_ | Medium         |🔒|
0424| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-repeating-character-replacement.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-repeating-character-replacement.py) | _O(n)_| _O(1)_| Medium || Sliding Window |
0457| [Circular Array Loop](https://leetcode.com/problems/circular-array-loop/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/circular-array-loop.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/circular-array-loop.py) | _O(n)_ | _O(1)_ | Medium         ||
0567| [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/permutation-in-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/permutation-in-string.py) | _O(n)_ | _O(1)_ | Medium         ||
0777| [Swap Adjacent in LR String](https://leetcode.com/problems/swap-adjacent-in-lr-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/swap-adjacent-in-lr-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/swap-adjacent-in-lr-string.py) | _O(n)_ | _O(1)_ | Medium         ||
0844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/backspace-string-compare.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/backspace-string-compare.py) | _O(m + n)_ | _O(1)_ | Easy ||
0904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/fruit-into-baskets.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/fruit-into-baskets.py) | _O(n)_ | _O(1)_ | Medium || Sliding Window
0977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/squares-of-a-sorted-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/squares-of-a-sorted-array.py) | _O(n)_ | _O(1)_ | Easy ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Recursion
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0095| [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/unique-binary-search-trees-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/unique-binary-search-trees-ii.py) | _O(4^n / n^(3/2)_      | _O(4^n / n^(3/2)_         | Medium         ||
0098| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|[C++](./001_Coding_Interview/LeetCode-Solutions/C++/validate-binary-search-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/validate-binary-search-tree.py)| _O(n)_ | _O(1)_ | Medium ||
0100| [Same Tree](https://leetcode.com/problems/same-tree/)      |[C+](./001_Coding_Interview/LeetCode-Solutions/C++/same-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/same-tree.py)  | _O(n)_          | _O(h)_        | Easy          ||
0104| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-depth-of-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-depth-of-binary-tree.py)| _O(n)_ | _O(h)_ | Easy ||
0105| [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/construct-binary-tree-from-preorder-and-inorder-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/construct-binary-tree-from-preorder-and-inorder-traversal.py) | _O(n)_        | _O(n)_          | Medium   ||
0108| [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/convert-sorted-array-to-binary-search-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/convert-sorted-array-to-binary-search-tree.py) | _O(n)_        | _O(logn)_          | Medium         ||
0109| [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/convert-sorted-list-to-binary-search-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/convert-sorted-list-to-binary-search-tree.py) | _O(n)_        | _O(logn)_          | Medium         ||
0110| [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/balanced-binary-tree.py) | _O(n)_| _O(h)_   | Easy           ||
0114| [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/flatten-binary-tree-to-linked-list.py)| _O(n)_        | _O(h)_          | Medium         ||
0116| [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/populating-next-right-pointers-in-each-node.py)| _O(n)_ | _O(1)_ | Medium ||
0124| [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-maximum-path-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-maximum-path-sum.py) | _O(n)_| _O(h)_| Hard  ||  
0129| [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sum-root-to-leaf-numbers.py) | _O(n)_ | _O(h)_ | Medium ||
0156| [Binary Tree Upside Down](https://leetcode.com/problems/binary-tree-upside-down/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-upside-down.py) | _O(n)_ | _O(1)_ | Medium    |🔒|
0241| [Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/different-ways-to-add-parentheses.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/different-ways-to-add-parentheses.py) | _O(n * 4^n / n^(3/2))_ | _O(n * 4^n / n^(3/2))_ | Medium    || 
0298 | [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-longest-consecutive-sequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-longest-consecutive-sequence.py) | _O(n)_ | _O(h)_ | Medium    |🔒|
0333 | [Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/largest-bst-subtree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/largest-bst-subtree.py) | _O(n)_ | _O(h)_ | Medium    |🔒|
0337| [House Robber III](https://leetcode.com/problems/house-robber-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/house-robber-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/house-robber-iii.py) | _O(n)_          | _O(h)_          | Medium           ||
0395| [Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-substring-with-at-least-k-repeating-characters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-substring-with-at-least-k-repeating-characters.py) | _O(n)_          | _O(1)_          | Medium           ||
0404| [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sum-of-left-leaves.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sum-of-left-leaves.py) | _O(n)_          | _O(h)_          | Easy           ||
0544| [Output Contest Matches](https://leetcode.com/problems/output-contest-matches/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/output-contest-matches.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/output-contest-matches.py) | _O(n)_          | _O(n)_          | Medium           ||
0549 | [Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-longest-consecutive-sequence-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-longest-consecutive-sequence-ii.py) | _O(n)_ | _O(h)_ | Medium    |🔒|
0761| [Special Binary String](https://leetcode.com/problems/special-binary-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/special-binary-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/special-binary-string.py) | _O(n^2)_          | _O(n)_          | Hard           ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Binary Search
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0004| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/median-of-two-sorted-arrays.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/median-of-two-sorted-arrays.py) | _O(log(min(m, n)))_ | _O(1)_ | Hard         ||
0033| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/search-in-rotated-sorted-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/search-in-rotated-sorted-array.py) | _O(logn)_ | _O(1)_   | Medium         | CTCI |
0035| [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/search-insert-position.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/search-insert-position.py) | _O(logn)_ | _O(1)_   | Medium         ||
0069| [Sqrt(x)](https://leetcode.com/problems/sqrtx/)       | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sqrtx.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sqrtx.py)      | _O(logn)_        | _O(1)_         | Medium         ||
0074| [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/search-a-2d-matrix.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/search-a-2d-matrix.py) | _O(logm + logn)_ | _O(1)_ | Medium   ||
0081| [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/search-in-rotated-sorted-array-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/search-in-rotated-sorted-array-ii.py) | _O(logn)_ ~ _O(n)_ | _O(1)_   | Medium         | CTCI |
0153| [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)         | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-minimum-in-rotated-sorted-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-minimum-in-rotated-sorted-array.py)       | _O(logn)_        | _O(1)_          | Medium         ||
0154| [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)      | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-minimum-in-rotated-sorted-array-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-minimum-in-rotated-sorted-array-ii.py)       | _O(logn)_ ~ _O(n)_        | _O(1)_          | Hard         ||
0162| [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-peak-element.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-peak-element.py)        | _O(logn)_       | _O(1)_          | Medium         ||
0222| [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/count-complete-tree-nodes.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/count-complete-tree-nodes.py) | _O((logn)^2)_       | _O(1)_          | Medium         ||
0278| [First Bad Version](https://leetcode.com/problems/first-bad-version/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/first-bad-version.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/first-bad-version.py)  | _O(logn)_ | _O(1)_ | Easy         | LintCode ||
0300| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-increasing-subsequence.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-increasing-subsequence.py)  | _O(nlogn)_ | _O(n)_ | Medium         | CTCI, LintCode | Binary Search, Segment Tree, DP|
0302| [Smallest Rectangle Enclosing Black Pixels](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/smallest-rectangle-enclosing-black-pixels.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/smallest-rectangle-enclosing-black-pixels.py)   | _O(nlogn)_          | _O(1)_          | Hard         | 🔒 |
0354| [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/russian-doll-envelopes.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/russian-doll-envelopes.py)  | _O(nlogn)_ | _O(1)_ | Hard         |||
0363| [Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-sub-matrix-no-larger-than-k/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-sum-of-sub-matrix-no-larger-than-k.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-sum-of-sub-matrix-no-larger-than-k.py)  | _O(min(m, n)^2 * max(m, n) * logn(max(m, n)))_ | _O(max(m, n))_ | Hard         |||
0374| [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/guess-number-higher-or-lower.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/guess-number-higher-or-lower.py)   | _O(logn)_          | _O(1)_          | Easy         | |
0410| [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/split-array-largest-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/split-array-largest-sum.py)   | _O(nlogs)_          | _O(1)_          | Hard         | |
0475 | [Heaters](https://leetcode.com/problems/heaters/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/heaters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/heaters.py) | _O((m + n) * logn)_ | _O(1)_ | Easy | |
0540|[Single Element in a Sorted Array](https://leetcode.com/problems/dsingle-element-in-a-sorted-array/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/single-element-in-a-sorted-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/single-element-in-a-sorted-array.py)| _O(logn)_ | _O(1)_ | Medium | |
0668 | [Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/kth-smallest-number-in-multiplication-table.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/kth-smallest-number-in-multiplication-table.py) | _O(m * log(m * n))_ | _O(1)_ | Hard | |
0774 | [Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimize-max-distance-to-gas-station.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimize-max-distance-to-gas-station.py) | _O(nlogr)_ | _O(1)_ | Hard | |
0852 | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/peak-index-in-a-mountain-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/peak-index-in-a-mountain-array.py) | _O(logn)_ | _O(1)_ | Easy | |
0894| [All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/all-possible-full-binary-trees.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/all-possible-full-binary-trees.py) | _O(n * 4^n / n^(3/2))_ | _O(n * 4^n / n^(3/2))_ | Medium    || 
0911| [Online Election](https://leetcode.com/problems/online-election/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/online-election.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/online-election.py) | ctor: _O(n)_<br> query : _O(logn)_ | _O(n)_ | Medium    || 
0981| [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/time-based-key-value-store.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/time-based-key-value-store.py) | set: _O(1)_<br> get : _O(logn)_ | _O(n)_ | Medium    || 
1011 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/capacity-to-ship-packages-within-d-days.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/capacity-to-ship-packages-within-d-days.py) | _O(nlogr)_ | _O(1)_ | Medium | |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Binary Search Tree
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/kth-smallest-element-in-a-bst.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/kth-smallest-element-in-a-bst.py) | _O(max(h, k))_ | _O(min(h, k))_ | Medium ||
0235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/lowest-common-ancestor-of-a-binary-search-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/lowest-common-ancestor-of-a-binary-search-tree.py) | _O(h)_ | _O(1)_ | Easy | EPI |
0270| [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/closest-binary-search-tree-value.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/closest-binary-search-tree-value.py)   | _O(h)_          | _O(1)_          | Easy         | 🔒 |
0285| [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/inorder-successor-in-bst.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/inorder-successor-in-bst.py)   | _O(h)_          | _O(1)_          | Medium         | 🔒 |
0449|[Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/serialize-and-deserialize-bst.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/serialize-and-deserialize-bst.py)| _O(n)_ | _O(h)_ | Medium | | |
0450|[Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/delete-node-in-a-bst.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/delete-node-in-a-bst.py)| _O(h)_ | _O(h)_ | Medium | | |
0776|[Split BST](https://leetcode.com/problems/split-bst/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/split-bst.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/split-bst.py)| _O(n)_ | _O(h)_ | Medium | 🔒 | |
0510| [Inorder Successor in BST II](https://leetcode.com/problems/inorder-successor-in-bst-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/inorder-successor-in-bst-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/inorder-successor-in-bst-ii.py)   | _O(h)_          | _O(1)_          | Medium         | 🔒 | |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Breadth-First Search
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0102| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-level-order-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-level-order-traversal.py)| _O(n)_| _O(n)_| Easy  || 
0103| [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-zigzag-level-order-traversal.py) | _O(n)_| _O(n)_| Medium  ||  
0117| [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/populating-next-right-pointers-in-each-node-ii.py)| _O(n)_ | _O(1)_ | Hard ||
0127| [Word Ladder](https://leetcode.com/problems/word-ladder/)|[C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-ladder.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-ladder.py) | _O(b^(d/2))_      | _O(w * l)_          | Medium         | CTCI | Bi-BFS
0130| [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)|[C++](./001_Coding_Interview/LeetCode-Solutions/C++/surrounded-regions.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/surrounded-regions.py)| _O(m * n)_ | _O(m + n)_ | Medium         ||
0133| [Clone Graph](https://leetcode.com/problems/clone-graph/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/clone-graph.py)   | _O(n)_          | _O(n)_          | Medium         ||
0207| [Course Schedule](https://leetcode.com/problems/course-schedule/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/course-schedule.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/course-schedule.py)   | _O(\|V\| + \|E\|)_          | _O(\|E\|)_          | Medium         || Topological Sort |
0210| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/course-schedule-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/course-schedule-ii.py)   | _O(\|V\| + \|E\|)_          | _O(\|E\|)_          | Medium         || Topological Sort |
0261| [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/graph-valid-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/graph-valid-tree.py)   | _O(\|V\| + \|E\|)_          | _O(\|V\| + \|E\|)_          | Medium         | 🔒 |
0269| [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/alien-dictionary.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/alien-dictionary.py)  | _O(n)_ | _O(1)_ | Hard         |🔒| Topological Sort, BFS, DFS |
0310| [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-height-trees.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-height-trees.py)   | _O(n)_          | _O(n)_          | Medium         ||
0317| [Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/shortest-distance-from-all-buildings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/shortest-distance-from-all-buildings.py)   | _O(k * m * n)_          | _O(m * n)_          | Hard         | 🔒 |
0433| [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-genetic-mutation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-genetic-mutation.py)   | _O(n * b)_          | _O(b)_          | Medium         ||
0444| [Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sequence-reconstruction.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sequence-reconstruction.py)   | _O(n * s)_          | _O(n)_          | Medium         |🔒| Topological Sort |
0490| [The Maze](https://leetcode.com/problems/the-maze/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/the-maze.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/the-maze.py) | _O(max(r, c) * w)_ | _O(w)_ | Medium | | |
0505| [The Maze II](https://leetcode.com/problems/the-maze-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/the-maze-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/the-maze-ii.py) | _O(max(r, c) * wlogw)_ | _O(w)_ | Medium | | |
0542| [01 Matrix](https://leetcode.com/problems/01-matrix/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/01-matrix.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/01-matrix.py)   | _O(m * n)_          | _O(1)_          | Medium         || DP
0742|[Closest Leaf in a Binary Tree](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/closest-leaf-in-a-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/closest-leaf-in-a-binary-tree.py)| _O(n)_ | _O(n)_ | Medium | | |
0743|[Network Delay Time](https://leetcode.com/problems/network-delay-time/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/network-delay-time.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/network-delay-time.py)| _O(\|E\| * log\|V\|)_ | _O(\|E\|)_ | Medium | | `Dijkstra's Algorithm` |
0752|[Open the Lock](https://leetcode.com/problems/open-the-lock/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/open-the-lock.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/open-the-lock.py)| _O(k * n^k + d)_ | _O(k * n^k + d)_ | Medium | | |
0773|[Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sliding-puzzle.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sliding-puzzle.py)| _O((m * n) * (m * n)!)_ | _O((m * n) * (m * n)!)_ | Hard | | `A* Search Algorithm` |
0787|[Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/cheapest-flights-within-k-stops.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/cheapest-flights-within-k-stops.py)| _O(\|E\| * log\|V\|)_ | _O(\|E\|)_ | Medium | | `Dijkstra's Algorithm` |
0815|[Bus Routes](https://leetcode.com/problems/bus-routes/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/bus-routes.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/bus-routes.py)| _O(\|E\| + \|V\|)_ | _O(\|E\| + \|V\|)_ | Hard | | |
0854|[K-Similar Strings](https://leetcode.com/problems/k-similar-strings/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/k-similar-strings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/k-similar-strings.py)| _O(n * n!/(c_a!*...*c_z!))_ | _O(n * n!/(c_a!*...*c_z!))_ | Hard | | |
0913| [Cat and Mouse](https://leetcode.com/problems/cat-and-mouse/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/cat-and-mouse.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/cat-and-mouse.py) | _O(n^3)_          | _O(n^2)_          | Hard           || MiniMax, Topological Sort |
0994|[Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rotting-oranges.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rotting-oranges.py)| _O(m * n)_ | _O(m * n)_ | Easy | | |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Depth-First Search
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0113| [Path Sum II](https://leetcode.com/problems/path-sum-ii/)   | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/path-sum-ii.py) | _O(n)_         | _O(h)_          | Medium         ||
0199| [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-right-side-view.py) | _O(n)_     | _O(h)_ | Medium  ||
0200| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-islands.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-islands.py) | _O(m * n)_ | _O(m * n)_| Medium         || BFS, DFS, Union Find
0236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/lowest-common-ancestor-of-a-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/lowest-common-ancestor-of-a-binary-tree.py) | _O(n)_ | _O(h)_ | Medium | EPI |
0247| [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/strobogrammatic-number-ii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/strobogrammatic-number-ii.py)  | _O(n * 5^(n/2))_ | _O(n)_ | Medium         |🔒||
0250| [Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/count-univalue-subtrees.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/count-univalue-subtrees.py)  | _O(n)_ | _O(h)_ | Medium         |🔒||
0282| [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/expression-add-operators.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/expression-add-operators.py)  | _O(4^n)_ | _O(n)_ | Hard         |||
0301| [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-invalid-parentheses.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-invalid-parentheses.py)  | _O(C(n, c))_ | _O(c)_ | Hard         |||
0329| [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-increasing-path-in-a-matrix.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-increasing-path-in-a-matrix.py)  | _O(m * n)_ | _O(m * n)_ | Hard         || DFS, Topological Sort |
0332| [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reconstruct-itinerary.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reconstruct-itinerary.py)  | _O(t! / (n1! * n2! * ... nk!))_ | _O(t)_ | Medium         |||
0366| [Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-leaves-of-binary-tree.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-leaves-of-binary-tree.py)  | _O(n)_ | _O(h)_ | Medium         |🔒||
0417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/pacific-atlantic-water-flow.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/pacific-atlantic-water-flow.py) | _O(m * n)_ | _O(m * n)_ | Medium ||
0464| [Can I Win](https://leetcode.com/problems/can-i-win/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/can-i-win.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/can-i-win.py) | _O(n!)_          | _O(n)_          | Medium           ||
0690| [Employee Importance](https://leetcode.com/problems/employee-importance/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/employee-importance.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/employee-importance.py) | _O(n)_          | _O(h)_          | Easy           || DFS, BFS
0694| [Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-distinct-islands.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-distinct-islands.py) | _O(m * n)_          | _O(m * n)_          | Medium           |🔒||
0695| [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-area-of-island.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-area-of-island.py) | _O(m * n)_          | _O(m * n)_          | Easy           ||
0733| [Max Area of Island](https://leetcode.com/problems/flood-fill/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/flood-fill.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/flood-fill.py) | _O(m * n)_          | _O(m * n)_          | Easy           ||
0753| [Cracking the Safe](https://leetcode.com/problems/cracking-the-safe/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/cracking-the-safe.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/cracking-the-safe.py) | _O(k^n)_          | _O(k^n)_          | Hard           || `de Bruijn sequences`, `Lyndon word`, Rolling Hash, Backtracking, Greedy |
0785| [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/is-graph-bipartite.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/is-graph-bipartite.py) | _O(\|V\| + \|E\|)_          | _O(\|V\|)_          | Medium           |||
0827| [Making A Large Island](https://leetcode.com/problems/making-a-large-island/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/making-a-large-island.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/making-a-large-island.py) | _O(n^2)_          | _O(n^2)_          | Hard           |||
0834| [Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sum-of-distances-in-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sum-of-distances-in-tree.py) | _O(n)_          | _O(n)_          | Hard           |||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Backtracking
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0017| [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/letter-combinations-of-a-phone-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/letter-combinations-of-a-phone-number.py) | _O(n * 4^n)_ | _O(1)_ | Medium ||
0022| [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/generate-parentheses.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/generate-parentheses.py)| _O(4^n / n^(3/2))_ | _O(n)_   | Medium         ||
0037| [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sudoku-solver.py) | _O((9!)^9)_  | _O(1)_          | Hard           ||
0039| [Combination Sum](https://leetcode.com/problems/combination-sum/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/combination-sum.py) | _O(k * n^k)_    | _O(k)_          | Medium         ||
0046| [Permutations](https://leetcode.com/problems/permutations/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/permutations.py) | _O(n * n!)_         | _O(n)_          | Medium         ||
0077| [Combinations](https://leetcode.com/problems/combinations/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/combinations.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/combinations.py) | _O(O(k * C(n, k)))_ | _O(k)_           | Medium         ||
0079| [Word Search](https://leetcode.com/problems/word-search/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-search.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-search.py) | _O(m * n * 3^l)_ | _O(l)_ | Medium         ||
0078| [Subsets](https://leetcode.com/problems/subsets/)       | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/subsets.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/subsets.py)    | _O(n * 2^n)_    | _O(1)_          | Medium         ||
0126| [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)   |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-ladder-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-ladder-ii.py) | _O(b^(d/2))_ | _O(w * l)_         | Hard         | CTCI | Bi-BFS
0131| [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-partitioning.py) | _O(n^2)_ ~ _O(2^n)_ | _O(n^2)_ | Medium ||
0140| [Word Break II](https://leetcode.com/problems/word-break-ii/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-break-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-break-ii.py) |  _O(n * l^2 + n * r)_      | _O(n^2)_       | Hard           ||
0212| [Word Search II](https://leetcode.com/problems/word-search-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-search-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-search-ii.py) | _O(m * n * 3^h)_ | _O(t)_  | Hard         | LintCode | Trie, DFS
0294| [Flip Game II](https://leetcode.com/problems/flip-game-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/flip-game-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/flip-game-ii.py)  | _O(n + c^2)_ | _O(c)_ | Medium         |🔒| DP, Hash |
0320| [Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/generalized-abbreviation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/generalized-abbreviation.py)  | _O(n * 2^n)_ | _O(n)_ | Medium         |🔒||
0425| [Word Squares](https://leetcode.com/problems/word-squares/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-squares.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-squares.py)  | _O(n^2 * n!)_ | _O(n^2)_ | Hard         |🔒||
0526| [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/beautiful-arrangement.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/beautiful-arrangement.py) | _O(n!)_ | _O(n)_  | Medium       ||
0676| [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/implement-magic-dictionary.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/implement-magic-dictionary.py) | _O(n)_ | _O(d)_  | Medium       || Trie, DFS
0679| [24 Game](https://leetcode.com/problems/24-game/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/24-game.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/24-game.py) | _O(1)_ | _O(1)_  | Hard       || DFS
0698| [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/partition-to-k-equal-sum-subsets.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/partition-to-k-equal-sum-subsets.py) | _O(n * 2^n)_ | _O(2^n)_ | Medium || DFS, DP, Memoization

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Dynamic Programming
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0010| [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/regular-expression-matching.py) | _O(m * n)_ | _O(n)_ | Hard ||
0044| [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/wildcard-matching.py) | _O(m * n)_ | _O(1)_    | Hard           || Greedy
0053| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|[C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-subarray.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-subarray.py)| _O(n)_     | _O(1)_         | Medium         ||
0062| [Unique Paths](https://leetcode.com/problems/unique-paths/)    | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/unique-paths.py)| _O(m * n)_      | _O(m + n)_   | Medium         ||
0063| [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/unique-paths-ii.py) |  _O(m * n)_ | _O(m + n)_   | Medium         ||
0064| [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-path-sum.py)| _O(m * n)_ | _O(m + n)_     | Medium         ||
0070| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/climbing-stairs.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/climbing-stairs.py) | _O(logn)_    | _O(1)_          | Easy           || Matrix Exponentiation
0072| [Edit Distance](https://leetcode.com/problems/edit-distance/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/edit-distance.py)| _O(m * n)_      | _O(m + n)_      | Hard           ||
0087| [Scramble String](https://leetcode.com/problems/scramble-string/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/scramble-string.py) | _O(n^4)_ | _O(n^3)_        | Hard           ||
0091| [Decode Ways](https://leetcode.com/problems/decode-ways/)   | [C++](./001_Coding_Interview/LeetCode-Solutions/Python/decode-ways.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/decode-ways.py)| _O(n)_          | _O(1)_          | Medium         ||
0096| [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/unique-binary-search-trees.py) | _O(n)_      | _O(1)_         | Medium         || Math
0097| [Interleaving String](https://leetcode.com/problems/interleaving-string/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/interleaving-string.py)| _O(m * n)_ | _O(m + n)_ | Hard         ||
0115| [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/distinct-subsequences.py)| _O(n^2)_ | _O(n)_ | Hard           ||
0120| [Triangle](https://leetcode.com/problems/triangle/)       | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/triangle.py)   | _O(m * n)_      | _O(n)_         | Medium         ||
0132| [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-partitioning-ii.py) | _O(n^2)_ | _O(n^2)_ | Hard ||
0139| [Word Break](https://leetcode.com/problems/word-break/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-break.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-break.py) |  _O(n * l^2)_         | _O(n)_       | Medium         ||
0152| [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)|[C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-product-subarray.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-product-subarray.py)| _O(n)_ | _O(1)_ | Medium     ||
0188| [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/best-time-to-buy-and-sell-stock-iv.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-time-to-buy-and-sell-stock-iv.py) | _O(n)_ | _O(n)_ | Hard || Quick Select, Mono Stack
0198| [House Robber](https://leetcode.com/problems/house-robber/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/house-robber.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/house-robber.py) | _O(n)_          | _O(1)_          | Easy           ||
0213| [House Robber II](https://leetcode.com/problems/house-robber-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/house-robber-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/house-robber-ii.py) | _O(n)_          | _O(1)_          | Medium           ||
0221| [Maximal Square](https://leetcode.com/problems/maximal-square/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximal-square.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximal-square.py) | _O(n^2)_         | _O(n)_          | Medium           | EPI |
0265| [Paint House II](https://leetcode.com/problems/paint-house-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/paint-house-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/paint-house-ii.py) | _O(n * k)_| _O(k)_| Hard |🔒||
0279| [Perfect Squares](https://leetcode.com/problems/perfect-squares/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/perfect-squares.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/perfect-squares.py) | _O(n * sqrt(n))_         | _O(n)_          | Medium           ||  Hash |
0304| [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-sum-query-2d-immutable.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-sum-query-2d-immutable.py) | ctor: _O(m * n)_, lookup: _O(1)_          | _O(m * n)_          | Medium           ||
0312| [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/burst-balloons.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/burst-balloons.py) | _O(n^3)_ | _O(n^2)_ | Hard ||
0322| [Coin Change](https://leetcode.com/problems/coin-change/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/coin-change.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/coin-change.py) | _O(n * k)_ | _O(k)_ | Medium ||
0351| [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/android-unlock-patterns.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/android-unlock-patterns.py) | _O(9^2 * 2^9)_ | _O(9 * 2^9)_ | Medium | 🔒 | Backtracking |
0361| [Bomb Enemy](https://leetcode.com/problems/bomb-enemy/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/bomb-enemy.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/bomb-enemy.py) | _O(m * n)_ | _O(m * n)_ | Medium | 🔒 | |
0368| [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/largest-divisible-subset.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/largest-divisible-subset.py) | _O(n^2)_ | _O(n)_ | Medium | | |
0375| [Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/guess-number-higher-or-lower-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/guess-number-higher-or-lower-ii.py)   | _O(n^2)_          | _O(n^2)_          | Medium         | |
0403 | [Frog Jump](https://leetcode.com/problems/frog-jump/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/frog-jump.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/frog-jump.py) | _O(n^2)_ | _O(n^2)_ | Hard ||
0416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/partition-equal-subset-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/partition-equal-subset-sum.py) | _O(n * s)_ | _O(s)_ | Medium ||
0418 | [Sentence Screen Fitting](https://leetcode.com/problems/sentence-screen-fitting/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sentence-screen-fitting.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sentence-screen-fitting.py) | _O(r + n * c)_ | _O(n)_ | Medium |🔒|
0465 | [Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/optimal-account-balancing.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/optimal-account-balancing.py) | _O(n * 2^n)_ | _O(2^n)_ | Hard |🔒|
0471 | [Encode String with Shortest Length](https://leetcode.com/problems/encode-string-with-shortest-length/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/encode-string-with-shortest-length.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/encode-string-with-shortest-length.py) | _O(n^3)_ on average | _O(n^2)_ | Medium |🔒|
0486 | [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/predict-the-winner.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/predict-the-winner.py) | _O(n^2)_ | _O(n)_ | Medium | | |
0552 | [Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/student-attendance-record-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/student-attendance-record-ii.py) | _O(n)_ | _O(1)_ | Hard |||
0562 | [Longest Line of Consecutive One in Matrix](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-line-of-consecutive-one-in-matrix.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-line-of-consecutive-one-in-matrix.py) | _O(m * n)_ | _O(n)_ | Medium |🔒||
0568 | [Maximum Vacation Days](https://leetcode.com/problems/maximum-vacation-days/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-vacation-days.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-vacation-days.py) | _O(n^2 * k)_ | _O(k)_ | Hard |🔒||
0688 | [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/knight-probability-in-chessboard.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/knight-probability-in-chessboard.py) | _O(k * n^2)_ | _O(n^2)_ | Medium ||
0689 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-sum-of-3-non-overlapping-subarrays.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-sum-of-3-non-overlapping-subarrays.py) | _O(n)_ | _O(n)_ | Hard ||
0727 | [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-window-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-window-subsequence.py) | _O(s * t)_ | _O(s)_ | Hard |🔒|
0730 | [Count Different Palindromic Subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/count-different-palindromic-subsequences.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/count-different-palindromic-subsequences.py) | _O(n^2)_ | _O(n)_ | Hard ||
0750 | [Number Of Corner Rectangles](https://leetcode.com/problems/number-of-corner-rectangles/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-corner-rectangles.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-corner-rectangles.py) | _O(n * m^2)_ | _O(n * m)_ | Medium ||
0788 | [Rotated Digits](https://leetcode.com/problems/rotated-digits/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rotated-digits.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rotated-digits.py) | _O(logn)_ | _O(logn)_ | Easy || Memoization |
0799 | [Champagne Tower](https://leetcode.com/problems/champagne-tower/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/champagne-tower.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/champagne-tower.py) | _O(n^2)_ | _O(n)_ | Medium |||
0805 | [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/split-array-with-same-average.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/split-array-with-same-average.py) | _O(n^4)_ | _O(n^3)_ | Hard |||
0818 | [Race Car](https://leetcode.com/problems/race-car/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/race-car.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/race-car.py) | _O(nlogn)_ | _O(n)_ | Hard || |
0837 | [New 21 Game](https://leetcode.com/problems/new-21-game/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/new-21-game.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/new-21-game.py) | _O(n)_ | _O(n)_ | Medium || |
0877 | [Stone Game](https://leetcode.com/problems/stone-game/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/stone-game.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/stone-game.py) | _O(n^2)_ | _O(n)_ | Medium | variant of [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | |
0920 | [Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-music-playlists.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-music-playlists.py) | _O(n * l)_ | _O(l)_ | Hard || |
0926| [Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/flip-string-to-monotone-increasing.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/flip-string-to-monotone-increasing.py) | _O(n)_ | _O(1)_ | Medium ||
0931| [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-falling-path-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-falling-path-sum.py) | _O(n^2)_ | _O(1)_ | Medium ||
0935| [Knight Dialer](https://leetcode.com/problems/knight-dialer/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/knight-dialer.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/knight-dialer.py) | _O(logn)_ | _O(1)_ | Medium || Matrix Exponentiation |
0940| [Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/distinct-subsequences-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/distinct-subsequences-ii.py) | _O(n)_ | _O(1)_ | Hard |||
0943| [Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-the-shortest-superstring.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-the-shortest-superstring.py) | _O(n^2 * (l^2 + 2^n))_ | _O(n^2)_ | Hard |||
0975 | [Odd Even Jump](https://leetcode.com/problems/odd-even-jump/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/odd-even-jump.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/odd-even-jump.py) | _O(nlogn)_ | _O(n)_ | Hard|| Mono Stack, BST

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Greedy
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0011| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/container-with-most-water.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/container-with-most-water.py) | _O(n)_ | _O(1)_ | Medium ||
0042| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/trapping-rain-water.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/trapping-rain-water.py) | _O(n)_ | _O(1)_ | Hard || Tricky
0045| [Jump Game II](https://leetcode.com/problems/jump-game-ii/)  | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/jump-game-ii.py) | _O(n)_        | _O(1)_          | Hard           ||
0055| [Jump Game](https://leetcode.com/problems/jump-game/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/jump-game.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/jump-game.py)  | _O(n)_          | _O(1)_          | Medium         ||
0122| [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/best-time-to-buy-and-sell-stock-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-time-to-buy-and-sell-stock-ii.py) | _O(n)_ | _O(1)_ | Easy ||
0134| [Gas Station](https://leetcode.com/problems/gas-station/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/gas-station.py)   | _O(n)_          | _O(1)_          | Medium         ||
0135| [Candy](https://leetcode.com/problems/candy/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/candy.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/candy.py) | _O(n)_ | _O(n)_ | Hard ||
0316| [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-duplicate-letters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-duplicate-letters.py) | _O(n)_| _O(1)_| Hard || Mono Stack |
0392| [Is Subsequence](https://leetcode.com/problems/is-subsequence/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/is-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/is-subsequence.py)   | _O(n)_          | _O(1)_          | Medium         ||
0435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/non-overlapping-intervals.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/non-overlapping-intervals.py) | _O(nlogn)_ | _O(1)_ | Medium | | Line Sweep
0621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/task-scheduler.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/task-scheduler.py) | _O(n)_ | _O(1)_ | Medium | |
0630 | [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/course-schedule-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/course-schedule-iii.py) | _O(nlogn)_ | _O(k)_ | Hard ||
0659 | [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/split-array-into-consecutive-subsequences.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/split-array-into-consecutive-subsequences.py) | _O(n)_ | _O(1)_ | Medium | |
0759 | [Employee Free Time](https://leetcode.com/problems/employee-free-time/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/employee-free-time.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/employee-free-time.py) | _O(m * logn)_ | _O(n)_ | Hard | |
0767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reorganize-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reorganize-string.py) | _O(n)_ | _O(1)_ | Medium | |
0843 | [Guess the Word](https://leetcode.com/problems/guess-the-word/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/guess-the-word.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/guess-the-word.py) | _O(n)_ | _O(n)_ | Hard || MinMax, Math |
0881 | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/boats-to-save-people.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/boats-to-save-people.py) | _O(nlogn)_ | _O(n)_ | Medium ||
0936 | [Stamping The Sequence](https://leetcode.com/problems/stamping-the-sequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/stamping-the-sequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/stamping-the-sequence.py) | _O((n - m) * m)_ | _O((n - m) * m)_ | Hard ||
0968 | [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-cameras.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-cameras.py) | _O(n)_ | _O(h)_ | Hard || DFS

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Graph
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0399| [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/evaluate-division.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/evaluate-division.py)  | _O(e + q)_ | _O(e)_ | Medium         || `Floyd-Warshall Algorithm`, BFS, Union Find|
0765 | [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/couples-holding-hands.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/couples-holding-hands.py) | _O(n)_| _O(n)_| Hard           ||| 

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Geometry
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Simulation
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Design
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0146| [LRU Cache](https://leetcode.com/problems/lru-cache/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/lru-cache.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/lru-cache.py)  | _O(1)_ | _O(k)_ | Hard || OrderedDict
0173| [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-search-tree-iterator.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-search-tree-iterator.py) | _O(1)_, amortized | _O(h)_| Medium ||   
0284| [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/peeking-iterator.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/peeking-iterator.py) | _O(1)_ | _O(1)_ | Medium ||
0348| [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/design-tic-tac-toe.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/design-tic-tac-toe.py) | _O(1)_ | _O(n^2)_ | Medium |🔒||
0353| [Design Snake Game](https://leetcode.com/problems/design-snake-game/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/design-snake-game.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/design-snake-game.py) | _O(1)_ | _O(s)_ | Medium |🔒| Deque |
0359| [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/logger-rate-limiter.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/logger-rate-limiter.py) | _O(1), amortized_ | _O(k)_ | Easy |🔒| Deque |
0362| [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/design-hit-counter.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/design-hit-counter.py) | _O(1), amortized_ | _O(k)_ | Medium |🔒| Deque |
0379| [Design Phone Directory](https://leetcode.com/problems/design-phone-directory/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/design-phone-directory.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/design-phone-directory.py) | _O(1)_ | _O(n)_ | Medium |🔒| |
0380| [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/insert-delete-getrandom-o1.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/insert-delete-getrandom-o1.py) | _O(1)_ | _O(n)_| Hard || |
0381| [Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/insert-delete-getrandom-o1-duplicates-allowed.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/insert-delete-getrandom-o1-duplicates-allowed.py) | _O(1)_ | _O(n)_ | Hard || |
0460| [LFU Cache](https://leetcode.com/problems/lfu-cache/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/lfu-cache.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/lfu-cache.py) | _O(1)_ | _O(k)_ | Hard || |
0489| [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/robot-room-cleaner.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/robot-room-cleaner.py) | _O(n)_ | _O(n)_ | Hard |🔒| |
0535| [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/encode-and-decode-tinyurl.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/encode-and-decode-tinyurl.py) | _O(1)_ | _O(n)_ | Medium || |
0635| [Design Log Storage System](https://leetcode.com/problems/design-log-storage-system/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/design-log-storage-system.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/design-log-storage-system.py) | put: _O(1)_<br> retrieve: _O(n + dlogd)_ | _O(n)_ | Medium |🔒| |
0642| [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/design-search-autocomplete-system.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/design-search-autocomplete-system.py) | _O(p^2)_ | _O(p * t + s)_ | Hard |🔒| |
0715| [Range Module](https://leetcode.com/problems/range-module/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-module.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-module.py) | add: _O(n)_<br> remove: _O(n)_<br> query: _O(logn)_ | _O(n)_ | Hard || |
0716| [Max Stack](https://leetcode.com/problems/max-stack/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-stack.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-stack.py) | push: _O(logn)_<br> pop: _O(logn)_<br> popMax: _O(logn)_<br> top: _O(1)_<br> peekMax: _O(1)_ | _O(n)_ | Easy || |
0745| [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/prefix-and-suffix-search.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/prefix-and-suffix-search.py) | ctor: _O(w * l^2)_<br> search : _O(p + s)_ | _O(t)_ | Hard || Trie |
0900| [RLE Iterator](https://leetcode.com/problems/rle-iterator/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rle-iterator.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rle-iterator.py) | _O(n)_ | _O(1)_ | Medium |||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## SQL
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0175| [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) | [MySQL](./001_Coding_Interview/MySQL/combine-two-tables.sql) | _O(m + n)_   | _O(m + n)_ | Easy     ||
0176| [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | [MySQL](./001_Coding_Interview/MySQL/second-highest-salary.sql) | _O(n)_ | _O(1)_ | Easy         ||
0177| [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) | [MySQL](./001_Coding_Interview/MySQL/nth-highest-salary.sql) | _O(n^2)_   | _O(n)_ | Medium         ||
0178| [Rank Scores](https://leetcode.com/problems/rank-scores/) | [MySQL](./001_Coding_Interview/MySQL/rank-scores.sql) | _O(n^2)_        | _O(n)_          | Medium         ||
0180| [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) | [MySQL](./001_Coding_Interview/MySQL/consecutive-numbers.sql) | _O(n)_   | _O(n)_ | Medium         ||
0181| [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) | [MySQL](./001_Coding_Interview/MySQL/employees-earning-more-than-their-managers.sql) | _O(n^2)_   | _O(1)_ | Easy     ||
0182| [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) | [MySQL](./001_Coding_Interview/MySQL/duplicate-emails.sql) | _O(n^2)_ | _O(n)_       | Easy           ||
0183| [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | [MySQL](./001_Coding_Interview/MySQL/customers-who-never-order.sql) | _O(n^2)_ | _O(1)_       | Easy           ||
0184| [Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) | [MySQL](./001_Coding_Interview/MySQL/department-highest-salary.sql) | _O(n^2)_   | _O(n)_ | Medium         ||
0185| [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | [MySQL](./001_Coding_Interview/MySQL/department-top-three-salaries.sql) | _O(n^2)_   | _O(n)_ | Hard         ||
0196| [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) | [MySQL](./001_Coding_Interview/MySQL/delete-duplicate-emails.sql) | _O(n^2)_ | _O(n)_       | Easy           ||
0197| [Rising Temperature](https://leetcode.com/problems/rising-temperature/) | [MySQL](./001_Coding_Interview/MySQL/rising-temperature.sql) | _O(n^2)_ | _O(n)_       | Easy           ||
0262| [Trips and Users](https://leetcode.com/problems/trips-and-users/) | [MySQL](./001_Coding_Interview/MySQL/trips-and-users.sql) | _O((t * u) + tlogt)_ | _O(t)_       | Hard           ||
0511| [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | [MySQL](./001_Coding_Interview/MySQL/game-play-analysis-i.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
0512| [Game Play Analysis II](https://leetcode.com/problems/game-play-analysis-ii/) | [MySQL](./001_Coding_Interview/MySQL/game-play-analysis-ii.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
0534| [Game Play Analysis III](https://leetcode.com/problems/game-play-analysis-iii/) | [MySQL](./001_Coding_Interview/MySQL/game-play-analysis-iii.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒| |
0550| [Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/) | [MySQL](./001_Coding_Interview/MySQL/game-play-analysis-iv.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1045| [Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/) | [MySQL](./001_Coding_Interview/MySQL/customers-who-bought-all-products.sql) | _O(n + k)_ | _O(n + k)_       | Medium           |🔒| |
1050| [Actors and Directors Who Cooperated At Least Three Times](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/) | [MySQL](./001_Coding_Interview/MySQL/actors-and-directors-who-cooperated-at-least-three-times.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1068| [Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i/) | [MySQL](./001_Coding_Interview/MySQL/product-sales-analysis-i.sql) | _O(m + n)_ | _O(m + n)_       | Easy           |🔒| |
1069| [Product Sales Analysis II](https://leetcode.com/problems/product-sales-analysis-ii/) | [MySQL](./001_Coding_Interview/MySQL/product-sales-analysis-ii.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1070| [Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/) | [MySQL](./001_Coding_Interview/MySQL/product-sales-analysis-iii.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1075| [Project Employees I](https://leetcode.com/problems/project-employees-i/) | [MySQL](./001_Coding_Interview/MySQL/project-employees-i.sql) | _O(m + n)_ | _O(m + n)_       | Easy           |🔒| |
1076| [Project Employees II](https://leetcode.com/problems/project-employees-ii/) | [MySQL](./001_Coding_Interview/MySQL/project-employees-ii.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1077| [Project Employees III](https://leetcode.com/problems/project-employees-iii/) | [MySQL](./001_Coding_Interview/MySQL/project-employees-iii.sql) | _O((m + n)^2)_ | _O(m + n)_       | Medium           |🔒| |
1082| [Sales Analysis I](https://leetcode.com/problems/sales-analysis-i/) | [MySQL](./001_Coding_Interview/MySQL/sales-analysis-i.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1083| [Sales Analysis II](https://leetcode.com/problems/sales-analysis-ii/) | [MySQL](./001_Coding_Interview/MySQL/sales-analysis-ii.sql) | _O(m + n)_ | _O(m + n)_       | Easy           |🔒| |
1084| [Sales Analysis III](https://leetcode.com/problems/sales-analysis-iii/) | [MySQL](./001_Coding_Interview/MySQL/sales-analysis-iii.sql) | _O(m + n)_ | _O(m + n)_       | Easy           |🔒| |
1097| [Game Play Analysis V](https://leetcode.com/problems/game-play-analysis-v/) | [MySQL](./001_Coding_Interview/MySQL/game-play-analysis-v.sql) | _O(n^2)_ | _O(n)_       | Hard           |🔒| |
1098| [Unpopular Books](https://leetcode.com/problems/unpopular-books/) | [MySQL](./001_Coding_Interview/MySQL/unpopular-books.sql) | _O(m + n)_ | _O(n)_       | Medium           |🔒| |
1107| [New Users Daily Count](https://leetcode.com/problems/new-users-daily-count/) | [MySQL](./001_Coding_Interview/MySQL/new-users-daily-count.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1112| [Highest Grade For Each Student](https://leetcode.com/problems/highest-grade-for-each-student/) | [MySQL](./001_Coding_Interview/MySQL/highest-grade-for-each-student.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒| |
1113| [Reported Posts](https://leetcode.com/problems/reported-posts/) | [MySQL](./001_Coding_Interview/MySQL/reported-posts.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1126| [Active Businesses](https://leetcode.com/problems/active-businesses/) | [MySQL](./001_Coding_Interview/MySQL/active-businesses.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1127| [User Purchase Platform](https://leetcode.com/problems//user-purchase-platform/) | [MySQL](./001_Coding_Interview/MySQL//user-purchase-platform.sql) | _O(n)_ | _O(n)_       | Hard           |🔒| |
1132| [Reported Posts II](https://leetcode.com/problems/reported-posts-ii/) | [MySQL](./001_Coding_Interview/MySQL/reported-posts-ii.sql) | _O(m + n)_ | _O(n)_       | Medium           |🔒| |
1141| [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) | [MySQL](./001_Coding_Interview/MySQL/user-activity-for-the-past-30-days-i.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1142| [User Activity for the Past 30 Days II](https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/) | [MySQL](./001_Coding_Interview/MySQL/user-activity-for-the-past-30-days-ii.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1148| [Article Views I](https://leetcode.com/problems/article-views-i/) | [MySQL](./001_Coding_Interview/MySQL/article-views-i.sql) | _O(nlogn)_ | _O(n)_       | Easy           |🔒| |
1149| [Article Views II](https://leetcode.com/problems/article-views-ii/) | [MySQL](./001_Coding_Interview/MySQL/article-views-ii.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒| |
1158| [Market Analysis I](https://leetcode.com/problems/market-analysis-i/) | [MySQL](./001_Coding_Interview/MySQL/market-analysis-i.sql) | _O(m + n)_ | _O(m + n)_       | Medium           |🔒| |
1159| [Market Analysis II](https://leetcode.com/problems/market-analysis-ii/) | [MySQL](./001_Coding_Interview/MySQL/market-analysis-ii.sql) | _O(m + n)_ | _O(m + n)_       | Hard           |🔒| |
1164| [Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date/) | [MySQL](./001_Coding_Interview/MySQL/product-price-at-a-given-date.sql) | _O(mlogn)_ | _O(m)_       | Medium           |🔒| |
1173| [Immediate Food Delivery I](https://leetcode.com/problems/immediate-food-delivery-i/) | [MySQL](./001_Coding_Interview/MySQL/immediate-food-delivery-i.sql) | _O(n)_ | _O(1)_       | Easy           |🔒| |
1174| [Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/) | [MySQL](./001_Coding_Interview/MySQL/immediate-food-delivery-ii.sql) | _O(n)_ | _O(m)_       | Medium           |🔒| |
1179| [Reformat Department Table](https://leetcode.com/problems/reformat-department-table/) | [MySQL](./001_Coding_Interview/MySQL/reformat-department-table.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1193| [Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/) | [MySQL](./001_Coding_Interview/MySQL/monthly-transactions-i.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1194| [Tournament Winners](https://leetcode.com/problems/tournament-winners/) | [MySQL](./001_Coding_Interview/MySQL/tournament-winners.sql) | _O(m + n + nlogn)_ | _O(m + n)_       | Hard           |🔒| |
1204| [Last Person to Fit in the Elevator](https://leetcode.com/problems/last-person-to-fit-in-the-elevator/) | [MySQL](./001_Coding_Interview/MySQL/last-person-to-fit-in-the-elevator.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒| |
1205| [Monthly Transactions II](https://leetcode.com/problems/monthly-transactions-ii/) | [MySQL](./001_Coding_Interview/MySQL/monthly-transactions-ii.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1211| [Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/) | [MySQL](./001_Coding_Interview/MySQL/queries-quality-and-percentage.sql) | _O(n)_ | _O(n)_       | Easy           || |
1212| [Team Scores in Football Tournament](https://leetcode.com/problems/team-scores-in-football-tournament/) | [MySQL](./001_Coding_Interview/MySQL/team-scores-in-football-tournament.sql) | _O(nlogn)_ | _O(n)_       | Medium           || |
1225| [Report Contiguous Dates](https://leetcode.com/problems/report-contiguous-dates/) | [MySQL](./001_Coding_Interview/MySQL/report-contiguous-dates.sql) | _O(nlogn)_ | _O(n)_       | Hard           |🔒| |
1241| [Number of Comments per Post](https://leetcode.com/problems/number-of-comments-per-post/) | [MySQL](./001_Coding_Interview/MySQL/number-of-comments-per-post.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1251| [Average Selling Price](https://leetcode.com/problems/average-selling-price/) | [MySQL](./001_Coding_Interview/MySQL/average-selling-price.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1264| [Page Recommendations](https://leetcode.com/problems/page-recommendations/) | [MySQL](./001_Coding_Interview/MySQL/page-recommendations.sql) | _O(m + n)_ | _O(m)_       | Medium           |🔒| |
1270| [All People Report to the Given Manager](https://leetcode.com/problems/all-people-report-to-the-given-manager/) | [MySQL](./001_Coding_Interview/MySQL/all-people-report-to-the-given-manager.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1280| [Students and Examinations](https://leetcode.com/problems/students-and-examinations/) | [MySQL](./001_Coding_Interview/MySQL/students-and-examinations.sql) | _O((m * n) * log(m * n))_ | _O(m * n)_       | Easy           |🔒| |
1285| [Find the Start and End Number of Continuous Ranges](https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/) | [MySQL](./001_Coding_Interview/MySQL/find-the-start-and-end-number-of-continuous-ranges.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1294| [Weather Type in Each Country](https://leetcode.com/problems/weather-type-in-each-country/) | [MySQL](./001_Coding_Interview/MySQL/weather-type-in-each-country.sql) | _O(m + n)_ | _O(n)_       | Easy           |🔒| |
1303| [Find the Team Size](https://leetcode.com/problems/find-the-team-size/) | [MySQL](./001_Coding_Interview/MySQL/find-the-team-size.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1308| [Running Total for Different Genders](https://leetcode.com/problems/running-total-for-different-genders/) | [MySQL](./001_Coding_Interview/MySQL/running-total-for-different-genders.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒| |
1321| [Restaurant Growth](https://leetcode.com/problems/restaurant-growth/) | [MySQL](./001_Coding_Interview/MySQL/restaurant-growth.sql) | _O(n^2)_ | _O(n)_       | Medium           |🔒| |
1322| [Ads Performance](https://leetcode.com/problems/ads-performance/) | [MySQL](./001_Coding_Interview/MySQL/ads-performance.sql) | _O(nlogn)_ | _O(n)_       | Easy           |🔒| |
1327| [List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period/) | [MySQL](./001_Coding_Interview/MySQL/list-the-products-ordered-in-a-period.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1336| [Number of Transactions per Visit](https://leetcode.com/problems/number-of-transactions-per-visit/) | [MySQL](./001_Coding_Interview/MySQL/number-of-transactions-per-visit.sql) | _O(m + n)_ | _O(m + n)_       | Medium           |🔒| |
1341| [Movie Rating](https://leetcode.com/problems/movie-rating/) | [MySQL](./001_Coding_Interview/MySQL/movie-rating.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒| |
1350| [Students With Invalid Departments](https://leetcode.com/problems/students-with-invalid-departments/) | [MySQL](./001_Coding_Interview/MySQL/students-with-invalid-departments.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1355| [Activity Participants](https://leetcode.com/problems/activity-participants/) | [MySQL](./001_Coding_Interview/MySQL/activity-participants.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1364| [Number of Trusted Contacts of a Customer](https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/) | [MySQL](./001_Coding_Interview/MySQL/number-of-trusted-contacts-of-a-customer.sql) | _O(n + m + l + nlogn)_ | _O(n + m + l)_       | Medium           |🔒| |
1369| [Get the Second Most Recent Activity](https://leetcode.com/problems/get-the-second-most-recent-activity/) | [MySQL](./001_Coding_Interview/MySQL/get-the-second-most-recent-activity.sql) | _O(nlogn)_ | _O(n)_       | Hard           |🔒| |
1378| [Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/) | [MySQL](./001_Coding_Interview/MySQL/replace-employee-id-with-the-unique-identifier.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1384| [Total Sales Amount by Year](https://leetcode.com/problems/total-sales-amount-by-year/) | [MySQL](./001_Coding_Interview/MySQL/total-sales-amount-by-year.sql) | _O(nlogn)_ | _O(n)_       | Hard           |🔒| |
1393| [Capital Gain/Loss](https://leetcode.com/problems/capital-gainloss/) | [MySQL](./001_Coding_Interview/MySQL/capital-gainloss.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1398| [Customers Who Bought Products A and B but Not C](https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/) | [MySQL](./001_Coding_Interview/MySQL/customers-who-bought-products-a-and-b-but-not-c.sql) | _O(m + n)_ | _O(m + n)_       | Medium           |🔒| |
1407| [Top Travellers](https://leetcode.com/problems/top-travellers/) | [MySQL](./001_Coding_Interview/MySQL/top-travellers.sql) | _O(m + nlogn)_ | _O(m + n)_       | Easy           |🔒| |
1412| [Find the Quiet Students in All Exams](https://leetcode.com/problems/find-the-quiet-students-in-all-exams/) | [MySQL](./001_Coding_Interview/MySQL/find-the-quiet-students-in-all-exams.sql) | _O(m + nlogn)_ | _O(m + n)_       | Hard           |🔒| |
1421| [NPV Queries](https://leetcode.com/problems/npv-queries/) | [MySQL](./001_Coding_Interview/MySQL/npv-queries.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1435| [Create a Session Bar Chart](https://leetcode.com/problems/create-a-session-bar-chart/) | [MySQL](./001_Coding_Interview/MySQL/create-a-session-bar-chart.sql) | _O(n)_ | _O(1)_       | Easy           |🔒| |
1440| [Evaluate Boolean Expression](https://leetcode.com/problems/evaluate-boolean-expression/) | [MySQL](./001_Coding_Interview/MySQL/evaluate-boolean-expression.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1445| [Apples & Oranges](https://leetcode.com/problems/apples-oranges/) | [MySQL](./001_Coding_Interview/MySQL/apples-oranges.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1454| [Active Users](https://leetcode.com/problems/active-users/) | [MySQL](./001_Coding_Interview/MySQL/active-users.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒| |
1459| [Rectangles Area](https://leetcode.com/problems/rectangles-area/) | [MySQL](./001_Coding_Interview/MySQL/rectangles-area.sql) | _O(n^2)_ | _O(n^2)_       | Medium           |🔒| |
1468| [Calculate Salaries](https://leetcode.com/problems/calculate-salaries/) | [MySQL](./001_Coding_Interview/MySQL/calculate-salaries.sql) | _O(m + n)_ | _O(m + n)_       | Easy           |🔒| |
1479| [Sales by Day of the Week](https://leetcode.com/problems/sales-by-day-of-the-week/) | [MySQL](./001_Coding_Interview/MySQL/sales-by-day-of-the-week.sql) | _O(m + n)_ | _O(n)_       | Hard           |🔒| |
1484| [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/) | [MySQL](./001_Coding_Interview/MySQL/group-sold-products-by-the-date.sql) | _O(nlogn)_ | _O(n)_       | Easy           |🔒| |
1495| [Friendly Movies Streamed Last Month](https://leetcode.com/problems/friendly-movies-streamed-last-month/) | [MySQL](./001_Coding_Interview/MySQL/friendly-movies-streamed-last-month.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1501| [Countries You Can Safely Invest In](https://leetcode.com/problems/countries-you-can-safely-invest-in/) | [MySQL](./001_Coding_Interview/MySQL/countries-you-can-safely-invest-in.sql) | _O(n)_ | _O(n)_       | Medium           |🔒| |
1511| [Customer Order Frequency](https://leetcode.com/problems/customer-order-frequency/) | [MySQL](./001_Coding_Interview/MySQL/customer-order-frequency.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| |
1517| [Find Users With Valid E-Mails](https://leetcode.com/problems/find-users-with-valid-e-mails/) | [MySQL](./001_Coding_Interview/MySQL/find-users-with-valid-e-mails.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| Regex |
1527| [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/) | [MySQL](./001_Coding_Interview/MySQL/patients-with-a-condition.sql) | _O(n)_ | _O(n)_       | Easy           |🔒| Regex |
1532| [The Most Recent Three Orders](https://leetcode.com/problems/the-most-recent-three-orders/) | [MySQL](./001_Coding_Interview/MySQL/the-most-recent-three-orders.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒||
1543| [Fix Product Name Format](https://leetcode.com/problems/fix-product-name-format/) | [MySQL](./001_Coding_Interview/MySQL/fix-product-name-format.sql) | _O(nlogn)_ | _O(n)_       | Easy           |🔒||
1549| [The Most Recent Orders for Each Product](https://leetcode.com/problems/the-most-recent-orders-for-each-product/) | [MySQL](./001_Coding_Interview/MySQL/the-most-recent-orders-for-each-product.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒||
1555| [Bank Account Summary](https://leetcode.com/problems/bank-account-summary/) | [MySQL](./001_Coding_Interview/MySQL/bank-account-summary.sql) | _O(m + n)_ | _O(m + n)_       | Medium           |🔒||
1565| [Unique Orders and Customers Per Month](https://leetcode.com/problems/unique-orders-and-customers-per-month/) | [MySQL](./001_Coding_Interview/MySQL/unique-orders-and-customers-per-month.sql) | _O(n)_ | _O(n)_       | Easy           |🔒||
1571| [Warehouse Manager](https://leetcode.com/problems/warehouse-manager/) | [MySQL](./001_Coding_Interview/MySQL/warehouse-manager.sql) | _O(n)_ | _O(n)_       | Medium           |🔒||
1581| [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) | [MySQL](./001_Coding_Interview/MySQL/customer-who-visited-but-did-not-make-any-transactions.sql) | _O(n)_ | _O(n)_       | Easy           |🔒||
1587| [Bank Account Summary II](https://leetcode.com/problems/bank-account-summary-ii/) | [MySQL](./001_Coding_Interview/MySQL/bank-account-summary-ii.sql) | _O(m + n)_ | _O(m + n)_       | Easy           |🔒||
1596| [The Most Frequently Ordered Products for Each Customer](https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer/) | [MySQL](./001_Coding_Interview/MySQL/the-most-frequently-ordered-products-for-each-customer.sql) | _O(n)_ | _O(n)_       | Medium           |🔒||
1607| [Sellers With No Sales](https://leetcode.com/problems/sellers-with-no-sales/) | [MySQL](./001_Coding_Interview/MySQL/sellers-with-no-sales.sql) | _O(nlogm)_ | _O(n + m)_       | Medium           |🔒||
1613| [Find the Missing IDs](https://leetcode.com/problems/find-the-missing-ids/) | [MySQL](./001_Coding_Interview/MySQL/find-the-missing-ids.sql) | _O(n^2)_ | _O(n)_       | Medium           |🔒||
1623| [All Valid Triplets That Can Represent a Country](https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/) | [MySQL](./001_Coding_Interview/MySQL/all-valid-triplets-that-can-represent-a-country.sql) | _O(n^3)_ | _O(n^3)_       | Easy           |🔒||
1633| [Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest/) | [MySQL](./001_Coding_Interview/MySQL/percentage-of-users-attended-a-contest.sql) | _O(m + nlogn)_ | _O(n)_       | Easy           |🔒||
1635| [Hopper Company Queries I](https://leetcode.com/problems/hopper-company-queries-i/) | [MySQL](./001_Coding_Interview/MySQL/hopper-company-queries-i.sql) | _O(d + r + tlogt)_ | _O(d + r + t)_       | Hard           |🔒||
1645| [Hopper Company Queries II](https://leetcode.com/problems/hopper-company-queries-ii/) | [MySQL](./001_Coding_Interview/MySQL/hopper-company-queries-ii.sql) | _O(d + r + tlogt)_ | _O(d + r + t)_       | Hard           |🔒||
1651| [Hopper Company Queries III](https://leetcode.com/problems/hopper-company-queries-iii/) | [MySQL](./001_Coding_Interview/MySQL/hopper-company-queries-iii.sql) | _O(d + r + tlogt)_ | _O(d + r + t)_       | Hard           |🔒||
1661| [Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine/) | [MySQL](./001_Coding_Interview/MySQL/average-time-of-process-per-machine.sql) | _O(n)_ | _O(n)_       | Easy           |🔒||
1667| [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/) | [MySQL](./001_Coding_Interview/MySQL/fix-names-in-a-table.sql) | _O(nlogn)_ | _O(n)_       | Easy           |🔒||
1677| [Product's Worth Over Invoices](https://leetcode.com/problems/products-worth-over-invoices/) | [MySQL](./001_Coding_Interview/MySQL/products-worth-over-invoices.sql) | _O(nlogn)_ | _O(n)_       | Easy           |🔒||
1683| [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/) | [MySQL](./001_Coding_Interview/MySQL/invalid-tweets.sql) | _O(n)_ | _O(n)_       | Easy           |🔒||
1693| [Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners/) | [MySQL](./001_Coding_Interview/MySQL/daily-leads-and-partners.sql) | _O(n)_ | _O(n)_       | Easy           |🔒||
1699| [Number of Calls Between Two Persons](https://leetcode.com/problems/number-of-calls-between-two-persons/) | [MySQL](./001_Coding_Interview/MySQL/number-of-calls-between-two-persons.sql) | _O(n)_ | _O(n)_       | Medium           |🔒||
1709| [Biggest Window Between Visits](https://leetcode.com/problems/biggest-window-between-visits/) | [MySQL](./001_Coding_Interview/MySQL/biggest-window-between-visits.sql) | _O(nlogn)_ | _O(n)_       | Medium           |🔒||
1715| [Count Apples and Oranges](https://leetcode.com/problems/count-apples-and-oranges/) | [MySQL](./001_Coding_Interview/MySQL/count-apples-and-oranges.sql) | _O(n)_ | _O(n)_       | Medium           |🔒||
1729| [Find Followers Count](https://leetcode.com/problems/find-followers-count/) | [MySQL](./001_Coding_Interview/MySQL/find-followers-count.sql) | _O(nlogn)_ | _O(n)_       | Easy           |🔒||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Shell Script
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0192 | [Word Frequency](https://leetcode.com/problems/word-frequency/) | [Shell](./001_Coding_Interview/Shell/word-frequency.sh) | _O(n)_     | _O(k)_          | Medium         ||
0193 | [Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/) | [Shell](./001_Coding_Interview/Shell/valid-phone-numbers.sh) | _O(n)_ | _O(1)_    | Easy           ||
0194 | [Transpose File](https://leetcode.com/problems/transpose-file/) | [Shell](./001_Coding_Interview/Shell/transpose-file.sh) | _O(n^2)_   | _O(n^2)_        | Medium         ||
0195 | [Tenth Line](https://leetcode.com/problems/tenth-line/) | [Shell](./001_Coding_Interview/Shell/tenth-line.sh)    | _O(n)_          | _O(1)_          | Easy           ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## 2. System Design Interview

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## 3. Behavioral Interview

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>
