from typing import List

import random

import unittest

#
# In python, creating a simple api for a set() would be a perfect solution if not for the third operation, getRandom().
# We know that we can retrieve an item from a set, and not know what that item will be, but that would not be
# actually random. (This is due to the way python implements sets. In python3, when using integers, elements are
# popped from the set in the order they appear in the underlying hashtable. Hence, not actually random.)
#
# A set is implemented essentially the same as a dict in python, so the time complexity of add / delete
# is on average O(1). When it comes to the random function, however, we run into the problem of needing to
# convert the data into a python list in order to return a random element. That conversion will add a
# significant overhead to getRandom, thus slowing the whole thing down.
#
# Instead of having to do that type conversion (set to list) we can take an approach that involves
# maintaining both a list and a dictionary side by side. That might look something like:
#
# data_map == {4: 0, 6: 1, 2: 2, 5: 3}
# data == [4, 6, 2, 5]
#
# Notice that the key in the data_map is the element in the list, and the value in the data_map is the
# index the element is at in the list.
# --------------------------------------------------------------------------------------------------------------------
# Notes:
#
# This can be made more efficient by removing the variables last_elem_in_list and index_of_elem_to_remove.
# I have used this to aid in readability.
# The remove operation might appear complicated so here's a before and after of what the data looks like:
# ---------------------------------------
# element_to_remove = 7
#
# before:     [4, 7, 9, 3, 5]
# after:      [4, 5, 9, 3]
#
# before:     {4:0, 7:1, 9:2, 3:3, 5:4}
# after:      {4:0, 9:2, 3:3, 5:1}
# ---------------------------------------
# All we're doing is replacing the element in the list that needs to be removed with the last element in the list.
# And then we update the values in the dictionary to reflect that.
#
# --------------------------------------------------------------------------------------------------------------------
# Let's look at the implementation:
#
class RandomizedSet:

    def __init__(self):
        self.data_map = {}  # dictionary, aka map, aka hashtable, aka hashmap
        self.data = []  # list aka array

    def view(self) -> List[int]:
        return self.data

    def insert(self, val: int) -> bool:

        # the problem indicates we need to return False if the item
        # is already in the RandomizedSet---checking if it's in the
        # dictionary is on average O(1) where as
        # checking the array is on average O(n)
        if val in self.data_map:
            return False

        # add the element to the dictionary. Setting the value as the
        # length of the list will accurately point to the index of the
        # new element. (len(some_list) is equal to the index of the last item +1)
        self.data_map[val] = len(self.data)

        # add to the list
        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:

        # again, if the item is not in the data_map, return False.
        # we check the dictionary instead of the list due to lookup complexity
        if not val in self.data_map:
            return False

        # essentially, we're going to move the last element in the list
        # into the location of the element we want to remove.
        # this is a significantly more efficient operation than the obvious
        # solution of removing the item and shifting the values of every item
        # in the dicitionary to match their new position in the list
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        # change the last element in the list to now be the value of the element
        # we want to remove
        self.data[-1] = val

        # remove the last element in the list
        self.data.pop()

        # remove the element to be removed from the dictionary
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        # if running outside of leetcode, you need to `import random`.
        # random.choice will randomly select an element from the list of data.
        return random.choice(self.data)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_RandomizedSet(self) -> None:
        randomizedSet = RandomizedSet()
        self.assertEqual(True, randomizedSet.insert(1))
        self.assertEqual([1], randomizedSet.view())
        self.assertEqual(False, randomizedSet.remove(2))
        self.assertEqual([1], randomizedSet.view())
        self.assertEqual(True, randomizedSet.insert(2))
        self.assertEqual([1,2], randomizedSet.view())
        ret = randomizedSet.getRandom()
        self.assertEqual(True, ret >= 1 and ret <= 2)
        self.assertEqual(True, randomizedSet.remove(1))
        self.assertEqual([2], randomizedSet.view())
        self.assertEqual(False, randomizedSet.insert(2))
        self.assertEqual([2], randomizedSet.view())
        self.assertEqual(2, randomizedSet.getRandom())


if __name__ == "__main__":
    unittest.main()
