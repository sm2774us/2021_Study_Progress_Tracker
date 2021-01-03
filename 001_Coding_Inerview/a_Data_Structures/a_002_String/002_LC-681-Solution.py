import unittest

class Solution:
    # Solution Explanation:
    # --------------------------------------------------------------------------------
    # Simulate the clock going forward by one minute.
    # Each time it moves forward, if all the digits are allowed, then return the time.
    #
    # TC: O(N) - Linear - where N is a number of characters in the input string
    # SC: O(1) - Constant Space
    def nextClosestTime(self, time: str) -> str:
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(":")
        #current = 60 * int(time[:2]) + int(time[3:])
        current = int(hour) * 60 + int(minute)

        for i in range(current + 1, current + 1441):
            minutes = i % 1440
            h, m = minutes // 60, minutes % 60

            result = "{:02d}:{:02d}".format(h, m)

            if set(result) <= set(time):
                break

        return result

    def nextClosestTime_oneliner(self, time):
        """
        :type time: str
        :rtype: str
        """
        return min((t <= time, t)
                   for i in range(24 * 60)
                   for t in ['%02d:%02d' % divmod(i, 60)]
                   if set(t) <= set(time))[1]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_nextClosestTime(self) -> None:
        sol = Solution()
        for time, solution in (["19:34", "19:39"], ["23:59","22:22"]):
            self.assertEqual(
                solution,
                sol.nextClosestTime(time)
            )
            self.assertEqual(
                solution,
                sol.nextClosestTime_oneliner(time)
            )

if __name__ == "__main__":
    unittest.main()
