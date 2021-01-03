from typing import List

import unittest

class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_numUniqueEmails(self) -> None:
        sol = Solution()
        for emails, solution in (
            [
                ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"],
                2
            ],
            [
                ["alice.z@leetcode.com","alicez@leetcode.com"],
                1
            ]
        ):
            self.assertEqual(
                solution,
                sol.numUniqueEmails(emails)
            )

        if __name__ == "__main__":
            unittest.main()
