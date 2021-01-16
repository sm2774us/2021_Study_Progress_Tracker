from typing import List
from functools import lru_cache

import unittest


class TrieNode:
    def __init__(self, key=None):
        self.key = key
        self.children = {}
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.word_end = True

class Solution:

    # Solution 1: Dynamic Programming
    #
    # The idea is the following:
    #
    #   * d is an array that contains booleans
    #   * d[i] is True if there is a word in the dictionary that ends at ith index of s AND d
    #     is also True at the beginning of the word
    #
    # Example:
    #
    #   * s = "leetcode"
    #   * words = ["leet", "code"]
    #   * d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"
    #   * d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True
    #
    # The result is the last index of d.
    #
    # Complexity:
    #
    # TC = O(s^2 * k)
    # where, s = len(s) and k = len(words)
    #
    def wordBreak_dynamic_programming_solution_1(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] |= dp[i - len(word)]
                    break
        return dp[-1]

    # Solution 2: DFS using lru_cache
    #
    # Let dfs(k) be a possibility to split string s[k:] into words from wordSet.
    # Then to check if word s[k:] can be splitted, we need to check if for some i word s[k:i]
    # in our wordSet and if s[i:] can be splitted, which is dfs(i).
    #
    # Complexity:
    # let T be the maximum length of word in our wordSet.
    # Then we need O(T) time to check if word in our set, so we have overall O(n^2T) complexity.
    # Space complexity is O(n +Tn) : to keep our cache and to keep our set of wordSet
    #
    # TC: O(n^2T) ; SC: O(n + Tn)
    #
    def wordBreak_dfs_using_lru_cache_solution_2(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)

        @lru_cache(None)
        def dfs(k):
            if k == n: return True
            for i in range(k + 1, n + 1):
                if s[k:i] in wordSet and dfs(i):
                    return True
            return False

        return dfs(0)

    # Solution 3: Trie + DFS + Memoization
    #
    def wordBreak_trie_dfs_memoization_solution_3(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add_word(word)

        @lru_cache(maxsize=None)
        def dfs(i, node):
            if i == len(s):
                # Make sure that the last character was the end of a word
                return node.word_end

            ch = s[i]
            # If word_end there are two options. We could try to continue down the current subtree or start
            # a new search from the root
            if node.word_end:
                return dfs(i, root) or (dfs(i + 1, node.children[ch]) if ch in node.children else False)
            elif ch in node.children:
                return dfs(i + 1, node.children[ch])
            return False

        root = trie.root
        return dfs(0, root)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_mergeTwoLists(self) -> None:
        sol = Solution()
        for s, wordDict, solution in (
            [
                "leetcode",
                ["leet", "code"],
                True
            ],
            [
                "applepenapple",
                ["apple", "pen"],
                True
            ],
            [
                "catsandog",
                ["cats", "dog", "sand", "and", "cat"],
                False
            ]
        ):
            self.assertEqual(
                solution,
                sol.wordBreak_dynamic_programming_solution_1(s, wordDict)
            )
            self.assertEqual(
                solution,
                sol.wordBreak_dfs_using_lru_cache_solution_2(s, wordDict)
            )
            self.assertEqual(
                solution,
                sol.wordBreak_trie_dfs_memoization_solution_3(s, wordDict)
            )

if __name__ == "__main__":
    unittest.main()
