#
# Time : O(1) for get and put operations
# Space: O(1)
#
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 146: LRU Cache
#
# Description:
#
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# Follow up:
# Could you do get and put in O(1) time complexity?
#
#
#
# Example 1:
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
# Constraints:
#
#   * 1 <= capacity <= 3000
#   * 0 <= key <= 3000
#   * 0 <= value <= 104
#   * At most 3 * 104 calls will be made to get and put.
#
# **************************************************************************
# Source: https://leetcode.com/problems/lru-cache/ (Leetcode - Problem 146 - LRU Cache)
#         https://practice.geeksforgeeks.org/problems/lru-cache/1 (GeeksForGeeks - LRU Cache)
#
import unittest


class Node(object):
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next

    def __repr__(self):
        return "%s:%s -> %r" % (self.key, self.value, self.next)


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity: int):
        # self.head.next points at the oldest (least used) node,
        # self.tail points at the latest used node
        self.head = self.tail = Node(0, 0)
        self.capacity = capacity
        self.size = 0
        self.mapping = {}

    def append_to_tail(self, node: Node):
        self.tail.next = node
        node.pre = self.tail
        node.next = None

        self.tail = node

    def remove_node(self, node: Node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def move_to_tail(self, node: Node):
        if node != self.tail:
            self.remove_node(node)
            self.append_to_tail(node)

    # @return an integer
    def get(self, key: int) -> int:
        if key in self.mapping:
            node = self.mapping[key]
            self.move_to_tail(node)
            return node.value

        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def put(self, key: int, value: int) -> None:
        node = self.mapping.get(key)

        if node is None:
            # the key is not found; create a new node
            # note: do this before removing the first node
            #   in case there is only one node
            new_node = Node(key, value, self.tail)
            self.append_to_tail(new_node)
            self.mapping[key] = new_node
            self.size += 1

            if self.size > self.capacity:
                # note: self.head.next will be modified by
                #   self.remove_node, so make node a variable
                node = self.head.next
                self.remove_node(node)
                del self.mapping[node.key]
                self.size -= 1

        else:
            # the key exists; update the value and move the node
            # to the tail if necessary
            node.value = value
            self.move_to_tail(node)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_lruCache(self) -> None:
        lruCache = LRUCache(2)

        lruCache.put(1, 1)
        # cache is {1 = 1}
        # self.assertEqual(1, lruCache.get(1))

        lruCache.put(2, 2)
        # cache is {1 = 1, 2 = 2}
        # self.assertEqual(1, lruCache.get(1))
        # self.assertEqual(2, lruCache.get(2))

        self.assertEqual(1, lruCache.get(1))
        lruCache.put(3, 3)
        # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(-1, lruCache.get(2))

        lruCache.put(4, 4)
        # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(-1, lruCache.get(1))

        self.assertEqual(3, lruCache.get(3))
        self.assertEqual(4, lruCache.get(4))


if __name__ == "__main__":
    unittest.main()
