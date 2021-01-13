from typing import List
import unittest


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda log: log.split()[0])   # when suffix is tie, sort by identifier
        letters.sort(key=lambda log: log.split()[1:])  # sorted by suffix
        result = letters + digits  # put digit logs after letter logs
        return result

    def reorderLogFiles_concise(self, a: List[str]) -> List[str]:
        def f(x):
            y = x.split(' ', 1)
            return (0, y[1], y[0]) if y[1][0].isalpha() else (1, None, None)

        return sorted(a, key=f)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reorderLogFiles(self) -> None:
        s = Solution()
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        solution = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        self.assertEqual(solution, s.reorderLogFiles(logs))
        self.assertEqual(solution, s.reorderLogFiles_concise(logs))


if __name__ == "__main__":
    unittest.main()
