from typing import List

import unittest

class Solution:
    def next_step(self, cells: List[int]) -> List[int]:
        res = [0] * 8
        for i in range(1, 7):
            res[i] = int(cells[i - 1] == cells[i + 1])
        return res

    # Solution:
    # 
    # Let us solve this problem by definition: we do iteration by iteration. 
    # However if N is very big, then we spend O(N) time and it can take too much time. 
    # Note, that there can be only 2^8 possible options for cells (in fact only 2^6 even, 
    # because after first step the first and the last symbols will always be zeros). 
    # It means, that after some number of iterations, cells start to repeat, and we found a loop.
    # 
    # How can we find a loop? We need to keep our positions in hash-table, 
    # so we can find loop_len. We do iteration by iteration and if we found a loop, 
    # we need to do (N - i) % loop_len more steps.
    #
    # Complexity:
    # TC: O(64)
    # SC: O(64)
    # because the loop size will not be more than 64 ( i.e., 2^6 )
    #
    # Here's a generalizable way to approach this problem w/o having to have a ton of insight:
    #
    #   * there are 8 cells so there are 2 ^ 8 = 256 possible cell configurations
    #   * therefore, after 256 transformations you are guaranteed to observe a cycle
    #     by the pigeonhole principle: https://en.wikipedia.org/wiki/Pigeonhole_principle
    #
    # In the future when you see questions where you have to make a large amount of state transitions
    # over a state space that seems small, just compare the size of the state space
    # to the # of transitions to determine if there's a cycle so you can bound complexity
    # to the size of the state space.
    #
    # There are two key observations to make here:
    # ---------------------------------------------
    # 1> The transformations form a cycle.
    # 2>The original array that is passed in, is not a part of that cycle.
    #
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        found_dic = {}
        for i in range(N):
            cells_str = str(cells)
            if cells_str in found_dic:
                loop_len = i - found_dic[cells_str]
                aux_key_list = list(map(lambda a: a, found_dic.keys()))[found_dic[cells_str]:]
                return eval(aux_key_list[(N - i) % loop_len])
                # return self.prisonAfterNDays(cells, (N - i) % loop_len)
            else:
                found_dic[cells_str] = i
                cells = self.next_step(cells)

        return cells


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_mergeTwoLists(self) -> None:
        s = Solution()
        for cells, N, solution in (
            [
                [0,1,0,1,1,0,0,1],
                7,
                [0,0,1,1,0,0,0,0]
            ],
            [
                [1,0,0,1,0,0,1,0],
                1000000000,
                [0,0,1,1,1,1,1,0]
            ]
        ):
            self.assertEqual(
                solution,
                s.prisonAfterNDays(cells, N)
            )


if __name__ == "__main__":
    unittest.main()
