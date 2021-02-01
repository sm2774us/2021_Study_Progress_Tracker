# Time:  O(n)
# Space: O(1)

# Example:
# BINARY TREE
#           4
#         /  \
#        /    \
#       2      5
#     /   \   /
#    /     \ /
#   1       3
#
#  PRE-ORDER TRAVERSAL
#  4->2->1->3->5->3

# Example:
# BINARY TREE
#             a
#           /  \
#          /    \
#         b      c
#        /
#       /
#      d
#     / \
#    /   \
#   e     f
#
#
#  PRE-ORDER TRAVERSAL
#  a->b->d->e->f->c

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Set current to root of binary tree
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                # Find the previous (prev) of curr
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                # Make curr as right child of its prev
                if node.right is None:
                    result.append(curr.val)
                    node.right = curr
                    curr = curr.left

                # fix the right child of prev
                else:
                    node.right = None
                    curr = curr.right

        return result


# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:  # preorder: root -> left -> right
                stack.append((root.right, False))
                stack.append((root.left, False))
                stack.append((root, True))
        return result

