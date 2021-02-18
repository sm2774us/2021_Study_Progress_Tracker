import collections

import unittest

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None

    @classmethod
    def treeToList(cls, root):
        if not root:
            return []

        q = collections.deque([root])

        result = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                temp.append(node.val)
            result.append(temp)
        return result

class Solution(object):
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        return self.MorrisTraversal(root)

    def MorrisTraversal(self, root):
        if root is None:
            return
        broken = [None, None]
        pre, cur = None, root

        while cur:
            if cur.left is None:
                self.detectBroken(broken, pre, cur)
                pre = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    self.detectBroken(broken, pre, cur)
                    node.right = None
                    pre = cur
                    cur = cur.right

        broken[0].val, broken[1].val = broken[1].val, broken[0].val

        return root

    def detectBroken(self, broken, pre, cur):
        if pre and pre.val > cur.val:
            if broken[0] is None:
                broken[0] = pre
            broken[1] = cur

class Test(unittest.TestCase):
	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_recoverTree(self) -> None:
		root = TreeNode(1)
		root.left = TreeNode(3)
		root.left.right = TreeNode(2)
		sol = Solution()
		sol.recoverTree(root)
		#print(root)
		self.assertEqual([[3],[1],[2]], TreeNode.treeToList(root))

		root = TreeNode(3)
		root.left = TreeNode(1)
		root.right = TreeNode(4)
		root.right.left = TreeNode(2)
		sol = Solution()
		sol.recoverTree(root)
		#print(root)
		self.assertEqual([[2],[1, 4],[3]], TreeNode.treeToList(root))

if __name__ == "__main__":
	unittest.main()
