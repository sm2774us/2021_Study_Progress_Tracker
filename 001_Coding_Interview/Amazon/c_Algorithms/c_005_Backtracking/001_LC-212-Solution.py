#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 212: Word Search II
#
# Description:
#
# Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/word-search-ii/ (LeetCode - Problem 212 - Word Search II)
# **************************************************************************
#
from typing import List
from collections import defaultdict

import unittest


class TrieNode:
    def __init__(self):
        # self.children = {}
        self.children = defaultdict(TrieNode)
        self.end_node = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        # for symbol in word:
        #     root = root.children.setdefault(symbol, TrieNode())
        for symbol in word:
            root = root.children[symbol]
        root.end_node = 1


class Solution(object):
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.num_words = len(words)
        res, trie = [], Trie()
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, "", res)
        res.sort()
        return res

    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0:
            return

        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        if tmp not in node.children:
            return

        board[i][j] = "#"
        for x, y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            self.dfs(board, node.children[tmp], i + x, j + y, path + tmp, res)
        board[i][j] = tmp


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findWords(self) -> None:
        sol = Solution()
        for board, words, solution in (
            [
                [
                    ["o", "a", "a", "n"],
                    ["e", "t", "a", "e"],
                    ["i", "h", "k", "r"],
                    ["i", "f", "l", "v"],
                ],
                ["oath", "pea", "eat", "rain"],
                ["eat", "oath"],
            ],
            [[["a", "b"], ["c", "d"]], ["abcb"], []],
            # [
            #     [["G","I","Z"], ["U","E","K"], ["Q","S","E"]],
            #     ["GEEKS", "FOR", "QUIZ", "GO"],
            #     ["GEEKS", "QUIZ"]
            # ]
        ):
            self.assertEqual(solution, sol.findWords(board, words))


# main
if __name__ == "__main__":
    unittest.main()
