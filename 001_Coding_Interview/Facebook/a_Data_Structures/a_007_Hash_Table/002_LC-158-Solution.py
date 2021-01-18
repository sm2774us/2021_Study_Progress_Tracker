from typing import List

import unittest

"""
The read4 API is already defined for you.
    @param buf, a list of characters
    @return an integer
    def read4(buf):
# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
def read4(buf):
    return 4 if len(buf) >= 4 else len(buf)

class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.count = 0
        self.curr = 0
        self.offset = 0
        self.bufsize = 0

    # Solution 1: Two Pointers
    #
    def read_solution_1(self, buf: List[str], n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        while idx < n:
            if self.curr >= self.count:
                self.count = read4(self.buf4)
                self.curr = 0
                if self.count == 0:
                    break
            buf[idx] = self.buf4[self.curr]
            self.curr += 1
            idx += 1
        return idx

    # Solution 2: Store the pos and offset that is read by last read4
    #
    def read_solution_2(self, buf: List[str], n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        pos, eof = 0, False
        while not eof and pos < n:
            if self.bufsize == 0:
                self.bufsize = read4(self.buf4)
                eof = self.bufsize < 4
            byte = min(n - pos, self.bufsize)
            for i in range(byte):
                buf[pos + i] = self.buf4[self.offset + i]
            self.offset = (self.offset + byte) % 4
            self.bufsize -= byte
            pos += byte
        return pos

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_read(self) -> None:
        sol = Solution()
        buf = list('abcdefghijk')
        self.assertEqual(4,sol.read_solution_1(buf,4))
        self.assertEqual(4,sol.read_solution_2(buf,4))
        buf = list('efghijk')
        self.assertEqual(4,sol.read_solution_1(buf,4))
        self.assertEqual(4,sol.read_solution_2(buf,4))
        buf = list('ijk')
        self.assertEqual(3,sol.read_solution_1(buf,3))
        self.assertEqual(3,sol.read_solution_2(buf,3))


if __name__ == "__main__":
    unittest.main()
