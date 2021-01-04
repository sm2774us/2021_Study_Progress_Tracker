from typing import List

import collections
import random

import unittest

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word: str) -> int:
#        """
#        :type word: str
#        :rtype int
#        """
# the Master class is included for debugging purpose only
class Master(object):
    def guess(self, word: str) -> int:
        """
        :type word: str
        :rtype int
        """
        return 1

class Solution:

    # Solution: Minimax
    #
    # Idea: This will use the MinMax Algorithmic idea to prune the search space
    # MiniMax:
    #   - https://www.youtube.com/watch?v=KU9Ch59-4vw
    #   - https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/Minimax.html
    #
    # Ideas from where I understood it:
    #   - https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison
    #
    # , Frequency Guess, Zero Match Guess]
    #
    # Idea 1 - Random Guess:
    # We can randomly pickup the words, guess it and find the number of correct characters
    # Then we prune the search space (wordlist) by keeping only those words which is having
    # same number of matching characters with the current word which the master.guess() returned
    # Example: For string1, guess returned 2, meaning 2 characters are correct, so we keep only
    # those words in word list which is have exactly 2 character matches with current word.
    #
    # Idea 2 - Zero Match Guess:
    # Probability of getting 0 matched is (25/26)^6 (because the correct one is only having 1 character
    # out of 26 alphabates and this is for all 6 position, so probability of getting a non match is (1-(1/26)))
    # This is around 80%. So we have 80% chance of getting a 0 match and with that we can greatly prune the
    # word list just by removing any words which is having any match with the 0 match guess. So we use this
    # to eliminate as many candidate as possible. So we need to find a word which is having higher number of
    # matching neighbours, so we can destroy that complete cluster if it is a 0 match. That is also can be viewed
    # as fewest 0 match with other words.
    #
    # Idea 3 - Frequency Guess:
    # We select words by scoring them. We go through the wordlist and for each 6 positions we count the frequency
    # of each alphabate. Say at first position 'p' is dominating with count of 7, for second position 'n' is dominating
    # with 9 counts. If we are allowed to guess outside the wordlist we would've guessed these top frequency characters
    # of each position concatenated into a string. This will have very high chance of getting a huge family of matching
    # strings. In current situation we can't do that. Thus we score each word by checking its characters against these
    # frequencies. The words having more character on the higher end of the frequency list, we guess those ones
    # this will auto select the word with biggest family. (We implement this idea here)
    #
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def similarity(w1, w2):
            c = 0
            for i, j in zip(w1, w2):
                c += i == j
            return c

        def purge(wordlist, guess, d):
            newWordlist = []
            for i in wordlist:
                if similarity(i, guess) == d:
                    newWordlist.append(i)
            return newWordlist

        def randomGuess(wordlist):
            return wordlist[random.randint(0, len(wordlist) - 1)]

        def frequencyGuess(wordlist):
            freq = collections.defaultdict(lambda: collections.defaultdict(int))
            for w in wordlist:
                for i in range(6):
                    freq[i][w[i]] += 1

            bestGuess = ""
            bestFreqScore = 0
            for w in wordlist:
                currFreqScore = 0
                for i in range(6):
                    currFreqScore += freq[i][w[i]]
                if currFreqScore > bestFreqScore:
                    bestFreqScore = currFreqScore
                    bestGuess = w

            return bestGuess

        def zeroMatchGuess(wordlist):
            zeroMatch = collections.defaultdict(int)
            for w1 in wordlist:
                for w2 in wordlist:
                    zeroMatch[w1] += similarity(w1, w2) == 0

            bestGuess = ""
            minZeroMatch = len(wordlist)
            for w in zeroMatch:
                if zeroMatch[w] < minZeroMatch:
                    minZeroMatch = zeroMatch[w]
                    bestGuess = w

            return bestGuess

        def guess(wordlist, guessMethod, master):
            for i in range(10):
                guess = guessMethod(wordlist)
                d = master.guess(guess)
                if d == 6:
                    return
                wordlist = purge(wordlist, guess, d)

        guess(wordlist, frequencyGuess, master)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findSecretWord(self) -> None:
        master = Master()
        sol = Solution()
        wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
        sol.findSecretWord(wordlist, master)

if __name__ == "__main__":
    unittest.main()
