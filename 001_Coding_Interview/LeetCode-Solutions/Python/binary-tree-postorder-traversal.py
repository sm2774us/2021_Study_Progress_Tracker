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
#  POST-ORDER TRAVERSAL
#  1->3->2->3->5->4

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
#  POST-ORDER TRAVERSAL
#  e->f->d->b->c->a

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dummy = TreeNode(0)
        dummy.left = root
        result, cur = [], dummy
        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    result += self.traceBack(cur.left, node)
                    node.right = None
                    cur = cur.right

        return result

    def traceBack(self, frm, to):
        result, cur = [], frm
        while cur is not to:
            result.append(cur.val)
            cur = cur.right
        result.append(to.val)
        result.reverse()
        return result


class Solution2(object):
    def postorderTraversal(self, root):
       if not root:
           return []
       current = root
       post_order_list = []
       while current:
           if current.right is None:
               post_order_list.insert(0, current.val)
               current = current.left
           else:
               # find left most of the right sub-tree
               predecessor = current.right
               while (predecessor.left) and (predecessor.left != current):
                   predecessor = predecessor.left
               # and create a link from this to current
               if predecessor.left is None:
                   post_order_list.insert(0, current.val)
                   predecessor.left = current
                   current = current.right
               else:
                   predecessor.left = None
                   current = current.left
       return post_order_list


# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution3(object):
    def postorderTraversal(self, root):
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
            else:  # postorder: left -> right -> root
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))
        return result

