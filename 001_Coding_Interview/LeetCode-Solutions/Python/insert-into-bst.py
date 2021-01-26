# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Time:  O(log(n))  [average case]
        Space: O(1)
        """
        new_node = TreeNode(val)

        if not root:
            return new_node

        curr = root
        while (curr != new_node):
            if curr.val > val:
                if not curr.left:
                    curr.left = new_node
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                curr = curr.right
        return root
