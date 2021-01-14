from typing import List
from typing import Tuple

import unittest

class AutocompleteSystem(object):
    class Trie(object):
        def __init__(self):
            self.sentences = {}
            self.next = {}

    def __init__(self, sentences: List[str], times: List[int]):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = self.Trie()
        for i in range(len(sentences)):
            self.addSentence(sentences[i], times[i])
        self.prefix = ""
        self.cur = self.root

    def addSentence(self, sentence: str, time: int):
        node = self.root
        for c in sentence:
            if c not in node.next:
                node.next[c] = self.Trie()
            node = node.next[c]
            if sentence not in node.sentences:
                node.sentences[sentence] = 0
            node.sentences[sentence] += time


    def input(self, c: str) -> List[str]:
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.addSentence(self.prefix, 1)
            self.cur = self.root
            self.prefix = ""
            return []
        else:
            self.prefix += c
            if c not in self.cur.next:
                self.cur.next[c] = self.Trie()
            self.cur = self.cur.next[c]
            return self.pickTop3()

    def pickTop3(self) -> List[str]:
        if len(self.cur.sentences) == 0:
            return []
        cnt = 0
        res = []
        for sentence, time in sorted(self.cur.sentences.items(), key = self.findNum):
            res.append(sentence)
            cnt += 1
            if cnt >= 3:
                break
        return res


    def findNum(self, item: Tuple[str, int]) -> Tuple[str, int]:
        return (-item[1], item[0])


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_autocomplete_system_input(self) -> None:
        autoCompleteSystem = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
        for c, solution in (
            ['i', ["i love you", "island","i love leetcode"]],
            [' ', ["i love you","i love leetcode"]],
            ['a', []],
            ['#', []]
        ):
            self.assertEqual(
                solution,
                autoCompleteSystem.input(c)
            )


if __name__ == "__main__":
    unittest.main()
