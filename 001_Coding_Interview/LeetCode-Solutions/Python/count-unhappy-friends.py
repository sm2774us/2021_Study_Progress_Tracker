# Time:  O(n^2)
# Space: O(n^2)

class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        friends = [[0]*n for _ in range(n)]
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                friends[i][preferences[i][j]] = j
        pairing = [0]*n
        for i, j in pairs:
            pairing[i], pairing[j] = j, i
        return sum(any(friends[i][j] < friends[i][pairing[i]] and friends[j][i] < friends[j][pairing[j]]
                       for j in range(len(friends[i])) if j != i and j != pairing[i])
                   for i in range(len(friends)))
