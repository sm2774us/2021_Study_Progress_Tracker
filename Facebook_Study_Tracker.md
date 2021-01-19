# Facebook_Study_Progress_Tracker

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
0260 | [Single Number III](https://leetcode.com/problems/single-number-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/single-number-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/single-number-iii.py) | _O(n)_ | _O(1)_          | Medium         ||
0371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sum-of-two-integers.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sum-of-two-integers.py) | _O(1)_ | _O(1)_ | Easy | LintCode |
0393 | [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/utf-8-validation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/utf-8-validation.py) | _O(n)_ | _O(1)_ | Medium | |
0477 | [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/total-hamming-distance.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/total-hamming-distance.py) | _O(n)_ | _O(1)_ | Medium ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Array
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0026 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-duplicates-from-sorted-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-duplicates-from-sorted-array.py) | _O(n)_       | _O(1)_         | Easy           || Two Pointers
0031 | [Next Permutation](https://leetcode.com/problems/next-permutation/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/next-permutation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/next-permutation.py) | _O(n)_  | _O(1)_          | Medium         || Tricky
0048 | [Rotate Image](https://leetcode.com/problems/rotate-image/)   | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rotate-image.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rotate-image.py) | _O(n^2)_      | _O(1)_         | Medium         ||
0054 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/spiral-matrix.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/spiral-matrix.py) | _O(m * n)_    | _O(1)_         | Medium         ||
0066 | [Plus One](https://leetcode.com/problems/plus-one/)      | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/plus-one.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/plus-one.py)   | _O(n)_           | _O(1)_         | Easy           || 
0073 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/set-matrix-zeroes.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/set-matrix-zeroes.py) | _O(m * n)_ | _O(1)_    | Medium         ||
0118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/pascals-triangle.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/pascals-triangle.py) | _O(n^2)_ | _O(1)_        | Easy           || 
0121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/best-time-to-buy-and-sell-stock.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-time-to-buy-and-sell-stock.py) | _O(n)_ | _O(1)_ | Easy ||
0128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-consecutive-sequence.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-consecutive-sequence.py) | _O(n)_ | _O(n)_ | Hard         || Tricky
0157 | [Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/read-n-characters-given-read4.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/read-n-characters-given-read4.py) | _O(n)_ | _O(1)_ | Easy           |🔒|
0158 | [Read N Characters Given Read4 II - Call multiple times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/read-n-characters-given-read4-ii-call-multiple-times.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/read-n-characters-given-read4-ii-call-multiple-times.py) | _O(n)_ | _O(1)_ | Hard |🔒|
0163 | [Missing Ranges](https://leetcode.com/problems/missing-ranges/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/missing-ranges.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/missing-ranges.py) | _O(n)_      | _O(1)_          | Medium         | 🔒 |
0189 | [Rotate Array](https://leetcode.com/problems/rotate-array/)   | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/rotate-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/rotate-array.py) | _O(n)_        | _O(1)_         | Easy           ||
0215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/kth-largest-element-in-an-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/kth-largest-element-in-an-array.py)| _O(n)_ on average | _O(1)_ |  Medium | EPI| Quick Select, Tri Partition
0238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/product-of-array-except-self.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/product-of-array-except-self.py) | _O(n)_ | _O(1)_          | Medium           | LintCode |
0240 | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/search-a-2d-matrix-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/search-a-2d-matrix-ii.py) | _O(m + n)_ | _O(1)_ | Medium   | EPI, LintCode |
0251| [Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/flatten-2d-vector.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/flatten-2d-vector.py)  | _O(1)_ |  _O(1)_ | Medium         |🔒||
0277| [Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-the-celebrity.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-the-celebrity.py)  | _O(n)_ |  _O(1)_ | Medium         |🔒, EPI ||
0296| [Best Meeting Point](https://leetcode.com/problems/best-meeting-point/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/best-meeting-point.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-meeting-point.py)  | _O(m * n)_ |  _O(m + n)_ | Hard         |🔒||
0311| [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sparse-matrix-multiplication.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sparse-matrix-multiplication.py)  | _O(m * n * l)_ |  _O(m * l)_ | Medium         |🔒||
0334| [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/increasing-triplet-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/increasing-triplet-subsequence.py)  | _O(n)_ |  _O(1)_ | Medium         |||
0414| [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/third-maximum-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/third-maximum-number.py)  | _O(n)_ |  _O(1)_ | Easy         |||
0419| [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/battleships-in-a-board.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/battleships-in-a-board.py)  | _O(m * n)_ |  _O(1)_ | Medium         |||
0448| [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-all-numbers-disappeared-in-an-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-all-numbers-disappeared-in-an-array.py)  | _O(n)_ |  _O(1)_ | Easy         |||
0670| [Maximum Swap](https://leetcode.com/problems/maximum-swap/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-swap.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-swap.py)  | _O(logn)_ |  _O(logn)_ | Medium         |||
0674 | [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-continuous-increasing-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-continuous-increasing-subsequence.py) | _O(n)_ | _O(1)_ | Easy ||
0724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-pivot-index.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-pivot-index.py) | _O(n)_ | _O(1)_ | Easy ||
0766 | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/toeplitz-matrix.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/toeplitz-matrix.py) | _O(m * n)_ | _O(1)_ | Easy ||
0885 | [Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/spiral-matrix-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/spiral-matrix-iii.py) | _O(max(m, n)^2)_ | _O(1)_      | Medium         ||
0896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/monotonic-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/monotonic-array.py) | _O(n)_ | _O(1)_      | Easy         ||
0918 | [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-sum-circular-subarray.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-sum-circular-subarray.py) | _O(n)_ | _O(1)_      | Medium         ||

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
0151| [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-words-in-a-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-words-in-a-string.py) | _O(n)_ | _O(1)_ | Medium         ||
0161| [One Edit Distance](https://leetcode.com/problems/one-edit-distance/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/one-edit-distance.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/one-edit-distance.py) | _O(m + n)_ | _O(1)_    | Medium         |🔒 |
0242| [Valid Anagram](https://leetcode.com/problems/valid-anagram/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-anagram.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-anagram.py) | _O(n)_       | _O(1)_         | Easy         | LintCode |
0273| [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/integer-to-english-words.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/integer-to-english-words.py) | _O(1)_ | _O(1)_ | Hard         | |
0405| [Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/convert-a-number-to-hexadecimal.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/convert-a-number-to-hexadecimal.py) | _O(n)_ | _O(1)_ | Easy         | |
0408| [Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-word-abbreviation.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-word-abbreviation.py) | _O(n)_ | _O(1)_ | Easy         | 🔒 |
0415| [Add Strings](https://leetcode.com/problems/add-strings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/add-strings.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/add-strings.py) | _O(n)_ | _O(1)_ | Easy         | |
0443| [String Compression](https://leetcode.com/problems/string-compression/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/string-compression.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/string-compression.py) | _O(n)_ | _O(1)_ | Easy         | |
0468| [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/validate-ip-address.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/validate-ip-address.py) | _O(1)_ | _O(1)_ | Medium         | |
0556| [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/next-greater-element-iii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/next-greater-element-iii.py) | _O(1)_ | _O(1)_ | Medium         | |
0564| [Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-the-closest-palindrome.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-the-closest-palindrome.py) | _O(l)_ | _O(l)_ | Hard         | |
0647| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindromic-substrings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindromic-substrings.py) | _O(n)_ | _O(n)_ |  Medium || `Manacher's Algorithm`
0678| [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-parenthesis-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-parenthesis-string.py) | _O(n)_ | _O(1)_ | Medium         | |
0680| [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-palindrome-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-palindrome-ii.py) | _O(n)_  | _O(1)_         | Easy           ||
0681| [Next Closest Time](https://leetcode.com/problems/next-closest-time/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/next-closest-time.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/next-closest-time.py) | _O(1)_  | _O(1)_         | Medium           ||
0686 | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/repeated-string-match.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/repeated-string-match.py) | _O(n + m)_ | _O(1)_ | Easy || `Rabin-Karp Algorithm` |
0722| [Remove Comments](https://leetcode.com/problems/remove-comments/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-comments.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-comments.py) | _O(n)_ | _O(k)_ | Medium         |||
0791| [Custom Sort String](https://leetcode.com/problems/custom-sort-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/custom-sort-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/custom-sort-string.py) | _O(n)_ | _O(1)_ | Medium         |||
0809| [Expressive Words](https://leetcode.com/problems/expressive-words/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/expressive-words.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/expressive-words.py) | _O(n + s)_ | _O(l + s)_ | Medium         |||
0824| [Goat Latin](https://leetcode.com/problems/goat-latin/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/goat-latin.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/goat-latin.py) | _O(n + w^2)_ | _O(l)_ | Easy         |||
0939 | [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-area-rectangle.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-area-rectangle.py) | _O(n^1.5)_ on average | _O(n)_ | Medium ||
0953 | [Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/verifying-an-alien-dictionary.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/verifying-an-alien-dictionary.py) | _O(n * l)_ | _O(1)_      | Easy         ||

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
0092| [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-linked-list-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-linked-list-ii.py) | _O(n)_       | _O(1)_         | Medium         || 
0138| [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/copy-list-with-random-pointer.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/copy-list-with-random-pointer.py) | _O(n)_   | _O(1)_          | Medium         ||
0160| [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/intersection-of-two-linked-lists.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/intersection-of-two-linked-lists.py) | _O(m + n)_ | _O(1)_         | Easy           ||
0206| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-linked-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-linked-list.py) | _O(n)_       | _O(1)_         | Easy         || 
0234| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindrome-linked-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-linked-list.py) | _O(n)_       | _O(1)_         | Easy         ||
0445| [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/add-two-numbers-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/add-two-numbers-ii.py) | _O(m + n)_       | _O(m + n)_         | Medium         |||
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
0071| [Simplify Path](https://leetcode.com/problems/simplify-path/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/simplify-path.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/simplify-path.py) | _O(n)_        | _O(n)_          | Medium         ||
0084| [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/largest-rectangle-in-histogram.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/largest-rectangle-in-histogram.py) | _O(n)_ | _O(n)_ | Hard || Mono Stack, DP
0101| [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/symmetric-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/symmetric-tree.py) | _O(n)_      | _O(h)_          | Easy           ||
0155| [Min Stack](https://leetcode.com/problems/min-stack/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/min-stack.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/min-stack.py)  | _O(n)_          | _O(1)_          | Easy           ||
0224| [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/basic-calculator.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/basic-calculator.py) | _O(n)_| _O(n)_| Hard || 
0227| [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/basic-calculator-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/basic-calculator-ii.py) | _O(n)_| _O(n)_| Medium || 
0341| [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/flatten-nested-list-iterator.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/flatten-nested-list-iterator.py) | _O(n)_        | _O(h)_          | Medium           |🔒| Iterator |
0394| [Decode String](https://leetcode.com/problems/decode-string/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/decode-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/decode-string.py) | _O(n)_        | _O(n)_          | Medium           |||
0636| [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/exclusive-time-of-functions.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/exclusive-time-of-functions.py) | _O(n)_  | _O(n)_         | Medium           ||
0772| [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/basic-calculator-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/basic-calculator-iii.py) | _O(n)_  | _O(n)_         | Hard           ||
0872| [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/leaf-similar-trees.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/leaf-similar-trees.py) | _O(n)_  | _O(h)_         | Easy           ||
0921 | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-add-to-make-parentheses-valid.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-add-to-make-parentheses-valid.py) | _O(n)_ | _O(1)_      | Medium         ||


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

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Binary Heap
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0295| [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-median-from-data-stream.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-median-from-data-stream.py)  | _O(nlogn)_ | _O(n)_ | Hard         | EPI, LintCode | BST, Heap |
0632 | [Smallest Range](https://leetcode.com/problems/smallest-range/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/smallest-range.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/smallest-range.py) | _O(nlogk)_ | _O(k)_ | Hard |||
0703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/kth-largest-element-in-a-stream.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/kth-largest-element-in-a-stream.py) | _O(nlogk)_ | _O(k)_ | Easy |||

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
0145 | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-postorder-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-postorder-traversal.py) | _O(n)_| _O(1)_| Hard  || `Morris Traversal` 
0208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/implement-trie-prefix-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/implement-trie-prefix-tree.py) | _O(n)_ | _O(1)_ | Medium || Trie
0211 | [Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/add-and-search-word-data-structure-design.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/add-and-search-word-data-structure-design.py) | _O(min(n, h))_ | _O(min(n, h))_ | Medium || Trie, DFS
0226| [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/invert-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/invert-binary-tree.py) | _O(n)_ | _O(h)_, _O(w)_ | Easy ||
0297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/serialize-and-deserialize-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/serialize-and-deserialize-binary-tree.py) | _O(n)_ | _O(h)_ | Hard | LintCode | DFS
0307 | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-sum-query-mutable.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-sum-query-mutable.py) | ctor: _O(n)_, update: _O(logn)_, query:  _O(logn)_ | _O(n)_ | Medium | LintCode | DFS, Segment Tree, BIT, Fenwick Tree
0308 | [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-sum-query-2d-mutable.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-sum-query-2d-mutable.py) | ctor: _O(m * n)_, update: _O(logm * logn)_, query:  _O(logm * logn)_ | _O(m * n)_ | Hard | 🔒 | DFS, Quad Tree, 2D BIT, 2D Fenwick Tree
0315|[Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/count-of-smaller-numbers-after-self.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/count-of-smaller-numbers-after-self.py)| _O(nlogn)_ | _O(n)_ | Hard | LintCode | BST, BIT, Fenwick Tree, Divide and Conquer, Merge Sort |
0529 | [Minesweeper](https://leetcode.com/problems/minesweeper/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minesweeper.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minesweeper.py) | _O(m * n)_ | _O(m + n)_ | Medium    || 
0536 | [Construct Binary Tree from String](https://leetcode.com/problems/construct-binary-tree-from-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/construct-binary-tree-from-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/construct-binary-tree-from-string.py) | _O(n)_ | _O(h)_ | Medium    | 🔒 |
0543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/diameter-of-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/diameter-of-binary-tree.py) | _O(n)_ | _O(h)_ | Easy    || 
0548 | [Split Array with Equal Sum](https://leetcode.com/problems/split-array-with-equal-sum/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/split-array-with-equal-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/split-array-with-equal-sum.py) | _O(n^2)_ | _O(n)_ | Medium    |🔒|
0572 |[Subtree of Another Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/subtree-of-another-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/subtree-of-another-tree.py)| _O(m * n)_ | _O(h)_ | Easy | | |
0617 |[Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/merge-two-binary-trees.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/merge-two-binary-trees.py)| _O(n)_ | _O(h)_ | Easy | | |
0637 |[Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/average-of-levels-in-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/average-of-levels-in-binary-tree.py)| _O(n)_ | _O(h)_ | Easy | | |
0654 |[Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-binary-tree.py)| _O(n)_ | _O(n)_ | Medium | LintCode | Mono Stack,  Cartesian Tree |
0663 | [Equal Tree Partition](https://leetcode.com/problems/strange-printer/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/equal-tree-partition.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/equal-tree-partition.py) | _O(n)_ | _O(n)_ | Medium | 🔒 | Hash
0863 | [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/all-nodes-distance-k-in-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/all-nodes-distance-k-in-binary-tree.py) | _O(n)_ | _O(n)_ | Medium || DFS + BFS |
0889 | [Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/construct-binary-tree-from-preorder-and-postorder-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/construct-binary-tree-from-preorder-and-postorder-traversal.py) | _O(n)_ | _O(h)_ | Medium || DFS, stack |
0897| [Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/increasing-order-search-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/increasing-order-search-tree.py) | _O(n)_          | _O(h)_          | Easy           || DFS |
0958| [Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/check-completeness-of-a-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/check-completeness-of-a-binary-tree.py) | _O(n)_          | _O(w)_          | Medium           || BFS |
0987| [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/vertical-order-traversal-of-a-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/vertical-order-traversal-of-a-binary-tree.py) | _O(nlogn)_          | _O(n)_          | Medium           || DFS |
1008 |[Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/construct-binary-search-tree-from-preorder-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/construct-binary-search-tree-from-preorder-traversal.py)| _O(n)_ | _O(h)_ | Medium |||

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
0159| [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-substring-with-at-most-two-distinct-characters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-substring-with-at-most-two-distinct-characters.py) | _O(n)_ | _O(1)_ | Hard         |🔒|
0170| [Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/two-sum-iii-data-structure-design.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/two-sum-iii-data-structure-design.py) | _O(n)_ | _O(n)_ | Easy | 🔒 |
0202| [Happy Number](https://leetcode.com/problems/happy-number/)      | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/happy-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/happy-number.py)   | _O(k)_  | _O(k)_          | Easy          ||
0246| [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/strobogrammatic-number.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/strobogrammatic-number.py)  | _O(n)_ | _O(1)_ | Easy         |🔒||
0249| [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/group-shifted-strings.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/group-shifted-strings.py)  | _O(nlogn)_ | _O(n)_ | Easy         |🔒||
0266| [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindrome-permutation.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-permutation.py)  | _O(n)_ |  _O(1)_ | Easy         |🔒||
0305| [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-islands-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-islands-ii.py) | _O(k)_ | _O(k)_| Hard         | LintCode, 🔒 | Union Find
0314| [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-vertical-order-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-vertical-order-traversal.py) | _O(n)_ | _O(n)_| Medium         | 🔒 | BFS
0325| [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-size-subarray-sum-equals-k.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-size-subarray-sum-equals-k.py) | _O(n)_ | _O(n)_|  Medium         | 🔒 |
0336| [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/palindrome-pairs.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/palindrome-pairs.py) | _O(n * k^2)_          | _O(n * k)_          | Hard             | | |
0340| [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)|  [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-substring-with-at-most-k-distinct-characters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-substring-with-at-most-k-distinct-characters.py) | _O(n)_ | _O(1)_ | Hard         |🔒|
0387| [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/first-unique-character-in-a-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/first-unique-character-in-a-string.py) | _O(n)_| _O(n)_| Easy |||
0438| [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-all-anagrams-in-a-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-all-anagrams-in-a-string.py) | _O(n)_          | _O(1)_          | Easy           ||
0523| [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/continuous-subarray-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/continuous-subarray-sum.py) | _O(n)_          | _O(k)_          | Medium           ||
0554| [Brick Wall](https://leetcode.com/problems/brick-wall/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/brick-wall.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/brick-wall.py) | _O(n)_ | _O(m)_ | Medium         | |
0560| [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/subarray-sum-equals-k.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/subarray-sum-equals-k.py) | _O(n)_ | _O(n)_ | Medium         | |
0721| [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/accounts-merge.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/accounts-merge.py) | _O(nlogn)_ | _O(n)_| Medium         || Union Find
0825 | [Friends Of Appropriate Ages](https://leetcode.com/problems/friends-of-appropriate-ages/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/friends-of-appropriate-ages.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/friends-of-appropriate-ages.py) | _O(a^2 + n)_ | _O(a)_ | Medium ||

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
0065| [Valid Number](https://leetcode.com/problems/valid-number/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/valid-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/valid-number.py) | _O(n)_         | _O(1)_          | Hard           || `Automata`
0166| [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/fraction-to-recurring-decimal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/fraction-to-recurring-decimal.py)  | _O(logn)_ | _O(1)_ | Medium         ||
0248| [Strobogrammatic Number III](https://leetcode.com/problems/strobogrammatic-number-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/strobogrammatic-number-iii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/strobogrammatic-number-iii.py)  | _O(5^(n/2))_ | _O(n)_ | Hard         |🔒||
0319 | [Bulb Switcher](https://leetcode.com/problems/bulb-switcher/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/bulb-switcher.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/bulb-switcher.py) | _O(1)_ | _O(1)_ | Medium |||
0382 | [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/linked-list-random-node.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/linked-list-random-node.py) | _O(n)_ | _O(1)_ | Medium || `Reservoir Sampling` |
0386 | [Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/lexicographical-numbers.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/lexicographical-numbers.py) | _O(n)_ | _O(1)_ | Medium |||
0398 | [Random Pick Index](https://leetcode.com/problems/random-pick-index/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/random-pick-index.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/random-pick-index.py) | _O(n)_ | _O(1)_ | Medium || `Reservoir Sampling` |
0478 | [Generate Random Point in a Circle](https://leetcode.com/problems/generate-random-point-in-a-circle/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/generate-random-point-in-a-circle.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/generate-random-point-in-a-circle.py) | _O(1)_ | _O(1)_ | Medium |||
0528 | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/random-pick-with-weight.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/random-pick-with-weight.py) | ctor: _O(n)_ <br> pick: _O(logn)_ | _O(n)_ | Medium |||

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
0088| [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/merge-sorted-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/merge-sorted-array.py) | _O(n)_ | _O(1)_       | Easy           ||
0148| [Sort List](https://leetcode.com/problems/sort-list/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sort-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sort-list.py)  | _O(nlogn)_      | _O(logn)_       | Medium         ||
0218| [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/the-skyline-problem.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/the-skyline-problem.py) | _O(nlogn)_   | _O(n)_        | Hard         || Sort, BST|
0252| [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/meeting-rooms.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/meeting-rooms.py) | _O(nlogn)_   | _O(n)_        | Easy         |🔒| |
0253| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/meeting-rooms-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/meeting-rooms-ii.py) | _O(nlogn)_   | _O(n)_        | Medium         |🔒| |
0280| [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/wiggle-sort.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/wiggle-sort.py) | _O(n)_   | _O(1)_        | Medium         |🔒| |
0324| [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/wiggle-sort-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/wiggle-sort-ii.py) | _O(n)_  on average | _O(1)_        | Medium         | variant of [Sort Colors](https://leetcode.com/problems/sort-colors/) | Tri Partition |
0347| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/top-k-frequent-elements.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/top-k-frequent-elements.py) | _O(n)_ | _O(n)_        | Medium         | | Quick Select, Heap, Bucket Sort |
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
0015 | [3 Sum](https://leetcode.com/problems/3sum/)         | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/3sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/3sum.py)       | _O(n^2)_        | _O(1)_          | Medium         || Two Pointers
0016 | [3 Sum Closest](https://leetcode.com/problems/3sum-closest/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/3sum-closest.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/3sum-closest.py) | _O(n^2)_       | _O(1)_          | Medium         || Two Pointers
0018| [4 Sum](https://leetcode.com/problems/4sum/)         | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/4sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/4sum.py)        | _O(n^3)_    | _O(1)_    | Medium         || Two Pointers
0019| [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-nth-node-from-end-of-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-nth-node-from-end-of-list.py) | _O(n)_       | _O(1)_         | Medium         || 
0141| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/linked-list-cycle.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/linked-list-cycle.py) | _O(n)_ | _O(1)_         | Easy         || 
0143| [Reorder List](https://leetcode.com/problems/reorder-list/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reorder-list.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reorder-list.py) | _O(n)_          |  _O(1)_         | Medium         ||  
0167| [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/two-sum-ii-input-array-is-sorted.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/two-sum-ii-input-array-is-sorted.py) | _O(n)_   | _O(1)_         | Medium         | |
0209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-size-subarray-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-size-subarray-sum.py) | _O(n)_ | _O(1)_ |  Medium | | Binary Search, Sliding Window
0283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/move-zeroes.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/move-zeroes.py) | _O(n)_ | _O(1)_          | Easy         | |
0287| [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-the-duplicate-number.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-the-duplicate-number.py)   | _O(n)_          | _O(1)_          | Hard       | | Binary Search, Two Pointers |
0344| [Reverse String](https://leetcode.com/problems/reverse-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-string.py) | _O(n)_ | _O(1)_ | Easy         | |
0345| [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reverse-vowels-of-a-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reverse-vowels-of-a-string.py) | _O(n)_ | _O(1)_ | Easy         | |
0349| [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/intersection-of-two-arrays.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/intersection-of-two-arrays.py) | _O(m + n)_ | _O(min(m, n))_ | Easy         | EPI | Hash, Binary Search
0350| [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/intersection-of-two-arrays-ii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/intersection-of-two-arrays-ii.py) | _O(m + n)_ | _O(1)_ | Easy         | EPI | Hash, Binary Search
0360| [Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/sort-transformed-array.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sort-transformed-array.py) | _O(n)_ | _O(1)_ | Medium         |🔒|
0567| [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/permutation-in-string.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/permutation-in-string.py) | _O(n)_ | _O(1)_ | Medium         ||
0844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/backspace-string-compare.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/backspace-string-compare.py) | _O(m + n)_ | _O(1)_ | Easy ||
0862| [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/shortest-subarray-with-sum-at-least-k.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/shortest-subarray-with-sum-at-least-k.py) | _O(n)_        | _O(n)_          | Hard           || Mono Deque, Sliding Window |
0977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/squares-of-a-sorted-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/squares-of-a-sorted-array.py) | _O(n)_ | _O(1)_ | Easy ||
1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-consecutive-ones-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-consecutive-ones-iii.py) | _O(n)_ | _O(1)_ | Medium || Sliding Window

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Recursion
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0098| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|[C++](./001_Coding_Interview/LeetCode-Solutions/C++/validate-binary-search-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/validate-binary-search-tree.py)| _O(n)_ | _O(1)_ | Medium ||
0100| [Same Tree](https://leetcode.com/problems/same-tree/)      |[C+](./001_Coding_Interview/LeetCode-Solutions/C++/same-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/same-tree.py)  | _O(n)_          | _O(h)_        | Easy          ||
0104| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-depth-of-binary-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-depth-of-binary-tree.py)| _O(n)_ | _O(h)_ | Easy ||
0105| [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/construct-binary-tree-from-preorder-and-inorder-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/construct-binary-tree-from-preorder-and-inorder-traversal.py) | _O(n)_        | _O(n)_          | Medium   ||
0109| [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/convert-sorted-list-to-binary-search-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/convert-sorted-list-to-binary-search-tree.py) | _O(n)_        | _O(logn)_          | Medium         ||
0110| [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/balanced-binary-tree.py) | _O(n)_| _O(h)_   | Easy           ||
0111| [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-depth-of-binary-tree.py)| _O(n)_ | _O(h)_ | Easy ||
0114| [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/flatten-binary-tree-to-linked-list.py)| _O(n)_        | _O(h)_          | Medium         ||
0116| [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/populating-next-right-pointers-in-each-node.py)| _O(n)_ | _O(1)_ | Medium ||
0124| [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-maximum-path-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-maximum-path-sum.py) | _O(n)_| _O(h)_| Hard  ||  
0129| [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/sum-root-to-leaf-numbers.py) | _O(n)_ | _O(h)_ | Medium ||
0298 | [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-longest-consecutive-sequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-longest-consecutive-sequence.py) | _O(n)_ | _O(h)_ | Medium    |🔒|
0337| [House Robber III](https://leetcode.com/problems/house-robber-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/house-robber-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/house-robber-iii.py) | _O(n)_          | _O(h)_          | Medium           ||
0395| [Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-substring-with-at-least-k-repeating-characters.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-substring-with-at-least-k-repeating-characters.py) | _O(n)_          | _O(1)_          | Medium           ||
0437| [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/path-sum-iii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/path-sum-iii.py) | _O(n)_          | _O(h)_          | Easy           ||

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
0034| [Search for a Range](https://leetcode.com/problems/search-for-a-range/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/search-for-a-range.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/search-for-a-range.py) | _O(logn)_ | _O(1)_   | Medium         ||
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
0658 | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/find-k-closest-elements.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/find-k-closest-elements.py) | _O(logn + k)_ | _O(1)_ | Medium | |
0852 | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/peak-index-in-a-mountain-array.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/peak-index-in-a-mountain-array.py) | _O(logn)_ | _O(1)_ | Easy | |
0981| [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/time-based-key-value-store.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/time-based-key-value-store.py) | set: _O(1)_<br> get : _O(logn)_ | _O(n)_ | Medium    || 

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

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Breadth-First Search
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0102| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-level-order-traversal.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-level-order-traversal.py)| _O(n)_| _O(n)_| Easy  || 
0107| [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-level-order-traversal-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-level-order-traversal-ii.py) | _O(n)_| _O(n)_| Easy  ||
0103| [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-zigzag-level-order-traversal.py) | _O(n)_| _O(n)_| Medium  ||  
0117| [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/populating-next-right-pointers-in-each-node-ii.py)| _O(n)_ | _O(1)_ | Hard ||
0127| [Word Ladder](https://leetcode.com/problems/word-ladder/)|[C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-ladder.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-ladder.py) | _O(b^(d/2))_      | _O(w * l)_          | Medium         | CTCI | Bi-BFS
0133| [Clone Graph](https://leetcode.com/problems/clone-graph/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/clone-graph.py)   | _O(n)_          | _O(n)_          | Medium         ||
0207| [Course Schedule](https://leetcode.com/problems/course-schedule/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/course-schedule.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/course-schedule.py)   | _O(\|V\| + \|E\|)_          | _O(\|E\|)_          | Medium         || Topological Sort |
0210| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/course-schedule-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/course-schedule-ii.py)   | _O(\|V\| + \|E\|)_          | _O(\|E\|)_          | Medium         || Topological Sort |
0261| [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/graph-valid-tree.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/graph-valid-tree.py)   | _O(\|V\| + \|E\|)_          | _O(\|V\| + \|E\|)_          | Medium         | 🔒 |
0269| [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/alien-dictionary.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/alien-dictionary.py)  | _O(n)_ | _O(1)_ | Hard         |🔒| Topological Sort, BFS, DFS |
0286| [Walls and Gates](https://leetcode.com/problems/walls-and-gates/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/walls-and-gates.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/walls-and-gates.py)   | _O(m * n)_          | _O(g)_          | Medium         | 🔒 |
0317| [Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/shortest-distance-from-all-buildings.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/shortest-distance-from-all-buildings.py)   | _O(k * m * n)_          | _O(m * n)_          | Hard         | 🔒 |
0490| [The Maze](https://leetcode.com/problems/the-maze/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/the-maze.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/the-maze.py) | _O(max(r, c) * w)_ | _O(w)_ | Medium | | |
0743|[Network Delay Time](https://leetcode.com/problems/network-delay-time/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/network-delay-time.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/network-delay-time.py)| _O(\|E\| * log\|V\|)_ | _O(\|E\|)_ | Medium | | `Dijkstra's Algorithm` |
0752|[Open the Lock](https://leetcode.com/problems/open-the-lock/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/open-the-lock.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/open-the-lock.py)| _O(k * n^k + d)_ | _O(k * n^k + d)_ | Medium | | |
0815|[Bus Routes](https://leetcode.com/problems/bus-routes/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/bus-routes.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/bus-routes.py)| _O(\|E\| + \|V\|)_ | _O(\|E\| + \|V\|)_ | Hard | | |
0865|[Shortest Path to Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/shortest-path-to-get-all-keys.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/shortest-path-to-get-all-keys.py)| _O(k * r * c + k^3*2^k)_ | _O(k*2^k)_ | Hard | | `Dijkstra's Algorithm` |
0886|[Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/possible-bipartition.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/possible-bipartition.py)| _O(\|V\| + \|E\|)_ | _O(\|V\| + \|E\|)_ | Medium | | |

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
0257| [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/binary-tree-paths.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/binary-tree-paths.py)  | _O(n * h)_ | _O(h)_ | Easy         |||
0282| [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/expression-add-operators.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/expression-add-operators.py)  | _O(4^n)_ | _O(n)_ | Hard         |||
0301| [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-invalid-parentheses.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-invalid-parentheses.py)  | _O(C(n, c))_ | _O(c)_ | Hard         |||
0329| [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-increasing-path-in-a-matrix.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-increasing-path-in-a-matrix.py)  | _O(m * n)_ | _O(m * n)_ | Hard         || DFS, Topological Sort |
0332| [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reconstruct-itinerary.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reconstruct-itinerary.py)  | _O(t! / (n1! * n2! * ... nk!))_ | _O(t)_ | Medium         |||
0339| [Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/nested-list-weight-sum.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/nested-list-weight-sum.py)  | _O(n)_ | _O(h)_ | Easy         |🔒||
0547| [Friend Circles](https://leetcode.com/problems/friend-circles/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/friend-circles.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/friend-circles.py) | _O(n^2)_          | _O(n)_          | Medium           || Union Find |
0694| [Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-distinct-islands.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-distinct-islands.py) | _O(m * n)_          | _O(m * n)_          | Medium           |🔒||
0695| [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-area-of-island.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-area-of-island.py) | _O(m * n)_          | _O(m * n)_          | Easy           ||
0785| [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/is-graph-bipartite.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/is-graph-bipartite.py) | _O(\|V\| + \|E\|)_          | _O(\|V\|)_          | Medium           |||

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
0040| [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/combination-sum-ii.py)| _O(k * C(n, k))_| _O(k)_         | Medium         ||
0046| [Permutations](https://leetcode.com/problems/permutations/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/permutations.py) | _O(n * n!)_         | _O(n)_          | Medium         ||
0047| [Permutations II](https://leetcode.com/problems/permutations-ii/)| [Python](./001_Coding_Interview/LeetCode-Solutions/Python/permutations-ii.py) | _O(n * n!)_   | _O(n)_          | Medium           ||
0051| [N-Queens](https://leetcode.com/problems/n-queens/)      | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/n-queens.py)   | _O(n!)_         | _O(n)_          | Hard           ||
0077| [Combinations](https://leetcode.com/problems/combinations/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/combinations.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/combinations.py) | _O(O(k * C(n, k)))_ | _O(k)_           | Medium         ||
0079| [Word Search](https://leetcode.com/problems/word-search/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-search.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-search.py) | _O(m * n * 3^l)_ | _O(l)_ | Medium         ||
0093| [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/restore-ip-addresses.py) | _O(1)_ | _O(1)_ | Medium         ||
0078| [Subsets](https://leetcode.com/problems/subsets/)       | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/subsets.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/subsets.py)    | _O(n * 2^n)_    | _O(1)_          | Medium         ||
0126| [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)   |[C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-ladder-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-ladder-ii.py) | _O(b^(d/2))_ | _O(w * l)_         | Hard         | CTCI | Bi-BFS
0140| [Word Break II](https://leetcode.com/problems/word-break-ii/)  | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-break-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-break-ii.py) |  _O(n * l^2 + n * r)_      | _O(n^2)_       | Hard           ||
0212| [Word Search II](https://leetcode.com/problems/word-search-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-search-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-search-ii.py) | _O(m * n * 3^h)_ | _O(t)_  | Hard         | LintCode | Trie, DFS
0291| [Word Pattern II](https://leetcode.com/problems/word-pattern-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-pattern-ii.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-pattern-ii.py)  | _O(n * C(n - 1, c - 1))_ | _O(n + c)_ | Hard         |🔒||

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
0070| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/climbing-stairs.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/climbing-stairs.py) | _O(logn)_    | _O(1)_          | Easy           || Matrix Exponentiation
0072| [Edit Distance](https://leetcode.com/problems/edit-distance/)|[Python](./001_Coding_Interview/LeetCode-Solutions/Python/edit-distance.py)| _O(m * n)_      | _O(m + n)_      | Hard           ||
0091| [Decode Ways](https://leetcode.com/problems/decode-ways/)   | [C++](./001_Coding_Interview/LeetCode-Solutions/Python/decode-ways.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/decode-ways.py)| _O(n)_          | _O(1)_          | Medium         ||
0123| [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-time-to-buy-and-sell-stock-iii.py) | _O(n)_ | _O(1)_ | Hard ||
0139| [Word Break](https://leetcode.com/problems/word-break/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/word-break.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/word-break.py) |  _O(n * l^2)_         | _O(n)_       | Medium         ||
0198| [House Robber](https://leetcode.com/problems/house-robber/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/house-robber.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/house-robber.py) | _O(n)_          | _O(1)_          | Easy           ||
0279| [Perfect Squares](https://leetcode.com/problems/perfect-squares/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/perfect-squares.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/perfect-squares.py) | _O(n * sqrt(n))_         | _O(n)_          | Medium           ||  Hash |
0304| [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/range-sum-query-2d-immutable.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/range-sum-query-2d-immutable.py) | ctor: _O(m * n)_, lookup: _O(1)_          | _O(m * n)_          | Medium           ||
0322| [Coin Change](https://leetcode.com/problems/coin-change/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/coin-change.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/coin-change.py) | _O(n * k)_ | _O(k)_ | Medium ||
0377| [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/combination-sum-iv.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/combination-sum-iv.py)   | _O(nlogn + n * t)_          | _O(t)_          | Medium         | |
0403 | [Frog Jump](https://leetcode.com/problems/frog-jump/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/frog-jump.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/frog-jump.py) | _O(n^2)_ | _O(n^2)_ | Hard ||
0416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/partition-equal-subset-sum.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/partition-equal-subset-sum.py) | _O(n * s)_ | _O(s)_ | Medium ||
0446 | [Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/arithmetic-slices-ii-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/arithmetic-slices-ii-subsequence.py) | _O(n^2)_ | _O(n * d)_ | Hard ||
0516 | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/longest-palindromic-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/longest-palindromic-subsequence.py) | _O(n^2)_ | _O(n)_ | Medium |||
0568 | [Maximum Vacation Days](https://leetcode.com/problems/maximum-vacation-days/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-vacation-days.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-vacation-days.py) | _O(n^2 * k)_ | _O(k)_ | Hard |🔒||
0639 | [Decode Ways II](https://leetcode.com/problems/decode-ways-ii/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/decode-ways-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/decode-ways-ii.py) | _O(n)_ | _O(1)_ | Hard |||
0673 | [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/number-of-longest-increasing-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/number-of-longest-increasing-subsequence.py) | _O(n^2)_ | _O(n)_ | Medium ||
0688 | [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/knight-probability-in-chessboard.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/knight-probability-in-chessboard.py) | _O(k * n^2)_ | _O(n^2)_ | Medium ||
0689 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/maximum-sum-of-3-non-overlapping-subarrays.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/maximum-sum-of-3-non-overlapping-subarrays.py) | _O(n)_ | _O(n)_ | Hard ||
0714 | [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/best-time-to-buy-and-sell-stock-with-transaction-fee.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-time-to-buy-and-sell-stock-with-transaction-fee.py) | _O(n)_ | _O(1)_ | Medium ||
0935| [Knight Dialer](https://leetcode.com/problems/knight-dialer/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/knight-dialer.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/knight-dialer.py) | _O(logn)_ | _O(1)_ | Medium || Matrix Exponentiation |

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
0055| [Jump Game](https://leetcode.com/problems/jump-game/)     | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/jump-game.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/jump-game.py)  | _O(n)_          | _O(1)_          | Medium         ||
0122| [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/best-time-to-buy-and-sell-stock-ii.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/best-time-to-buy-and-sell-stock-ii.py) | _O(n)_ | _O(1)_ | Easy ||
0392| [Is Subsequence](https://leetcode.com/problems/is-subsequence/)| [C++](./001_Coding_Interview/LeetCode-Solutions/C++/is-subsequence.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/is-subsequence.py)   | _O(n)_          | _O(1)_          | Medium         ||
0402 | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/remove-k-digits.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/remove-k-digits.py) | _O(n)_ | _O(n)_ | Medium | LintCode |
0452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/minimum-number-of-arrows-to-burst-balloons.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/minimum-number-of-arrows-to-burst-balloons.py) | _O(nlogn)_ | _O(1)_ | Medium | |
0621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/task-scheduler.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/task-scheduler.py) | _O(n)_ | _O(1)_ | Medium | |
0767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/reorganize-string.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/reorganize-string.py) | _O(n)_ | _O(1)_ | Medium | |
0843 | [Guess the Word](https://leetcode.com/problems/guess-the-word/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/guess-the-word.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/guess-the-word.py) | _O(n)_ | _O(n)_ | Hard || MinMax, Math |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Graph
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0399| [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/evaluate-division.cpp)  [Python](./001_Coding_Interview/LeetCode-Solutions/Python/evaluate-division.py)  | _O(e + q)_ | _O(e)_ | Medium         || `Floyd-Warshall Algorithm`, BFS, Union Find|

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
0348| [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/design-tic-tac-toe.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/design-tic-tac-toe.py) | _O(1)_ | _O(n^2)_ | Medium |🔒||
0359| [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/logger-rate-limiter.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/logger-rate-limiter.py) | _O(1), amortized_ | _O(k)_ | Easy |🔒| Deque |
0380| [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/insert-delete-getrandom-o1.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/insert-delete-getrandom-o1.py) | _O(1)_ | _O(n)_| Hard || |
0381| [Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/insert-delete-getrandom-o1-duplicates-allowed.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/insert-delete-getrandom-o1-duplicates-allowed.py) | _O(1)_ | _O(n)_ | Hard || |
0432| [All O\`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/all-oone-data-structure.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/all-oone-data-structure.py) | _O(1)_ | _O(n)_| Hard || |
0489| [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/robot-room-cleaner.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/robot-room-cleaner.py) | _O(n)_ | _O(n)_ | Hard |🔒| |
0642| [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/design-search-autocomplete-system.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/design-search-autocomplete-system.py) | _O(p^2)_ | _O(p * t + s)_ | Hard |🔒| |
0716| [Max Stack](https://leetcode.com/problems/max-stack/) | [C++](./001_Coding_Interview/LeetCode-Solutions/C++/max-stack.cpp) [Python](./001_Coding_Interview/LeetCode-Solutions/Python/max-stack.py) | push: _O(logn)_<br> pop: _O(logn)_<br> popMax: _O(logn)_<br> top: _O(1)_<br> peekMax: _O(1)_ | _O(n)_ | Easy || |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

## Concurrency
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|

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
