from typing import List
import collections

import unittest

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        allWords = list(set().union(beginWord, endWord, wordList))

        wordDict = self.construct(allWords)

        return self.bfs(beginWord, endWord, wordDict)

    def construct(self, wordList):
        wordDict = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                new = word[:i] + '_' + word[i + 1:]
                wordDict[new].append(word)

        return wordDict

    def bfs(self, beginWord, endWord, wordDict):
        queue = collections.deque()
        queue.append([beginWord, 1])

        visited = set()
        visited.add(beginWord)

        while queue:
            word, steps = queue.popleft()

            for i in range(len(word)):
                new = word[:i] + '_' + word[i + 1:]
                neighbors = wordDict[new]
                for neigh in neighbors:
                    if neigh not in visited:
                        if neigh == endWord:
                            return steps + 1
                        else:
                            visited.add(neigh)
                            queue.append([neigh, steps + 1])

        return 0


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_ladderLength(self) -> None:
        s = Solution()
        for beginWord, endWord, wordList, solution in (
            [
                "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5
            ],
            [
                "hit", "cog", ["hot","dot","dog","lot","log"], 0
            ]
        ):
            self.assertEqual(s.ladderLength(beginWord, endWord, wordList), solution)


if __name__ == "__main__":
    unittest.main()
