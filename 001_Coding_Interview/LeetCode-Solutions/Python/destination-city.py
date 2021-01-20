# Time:  O(n)
# Space: O(n)

import itertools


class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        A, B = map(set, itertools.zip(*paths))
        return (B-A).pop()
