# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    result.append(curr.val)
                    node.right = None
                    curr = curr.right

        return result

#
# In inorder, the order should be
# left -> root -> right
#
# But when we use stack, the order should be reversed:
#
# right -> root -> left
#
#
# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()  # the last element
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:  # inorder: left -> root -> right
                stack.append((root.right, False))
                stack.append((root, True))
                stack.append((root.left, False))
        return result

#
# Morris Traversal:
#
# Morris Traversal is a way of traversing BST with O(1) space and O(n) time.
# It's a little hard to understand but the basic idea is to link predecessor back to current node
# so that we can trace back to top of BST. It's also a little tricky to see how it is O(n)
# since finding predecessor is often O(logn). The answer is , we don't have to find predecessor
# for every node, only the nodes with valid left child. It will be obvious if you draw a tree to
# see that every edge is only visited constant time.
#
# TC: O(n)
# SC: O(1)
#
# def inorderTraversal(self, root):
#         result=[]
#         node=root
#         while node!=None:
#             if node.left==None:
#                 result.append(node.val)
#                 node=node.right
#             else:
#                 pre=node.left
#                 while pre.right!=None and pre.right!=node:
#                     pre=pre.right
#                 if pre.right==None:
#                     pre.right=node
#                     node=node.left
#                 else:
#                     pre.right=None
#                     result.append(node.val)
#                     node=node.right
#         return result
#
# Preorder, basically the same, just one line of change
#
#
# def preorderTraversal(self, root):
#         result=[]
#         node=root
#         while node!=None:
#             #print(node.val)
#             if node.left==None:
#                 result.append(node.val)
#                 node=node.right
#             else:
#                 pre=node.left
#                 while pre.right!=node and pre.right!=None:
#                     pre=pre.right
#                 if pre.right==None:
#                     result.append(node.val)
#                     pre.right=node
#                     node=node.left
#                 else:
#                     pre.right=None
#                     node=node.right
#         return result
#
# Postorder can be simple as well. Just do everything reversely comparing to the preorder one. 
# By this I mean we go right child node and use deque to append left to result. Here is the code:
#
# def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res = deque()
#
#         while root:
#             if root.right:
#                 temp = root.right
#                 while temp.left and temp.left != root:
#                     temp = temp.left
#                 if not temp.left:
#                     res.appendleft(root.val)
#                     temp.left = root
#                     root = root.right
#                 else:
#                     temp.left = None
#                     root = root.left
#             else:
#                 res.appendleft(root.val)
#                 root = root.left
#
#         return res
# 
# or w/o using deque ... For post-order, begin with current and if current.right is empty - 
# start looking towards left. If not, find left most predecessor and link the left of this 
# predecessor back to current. (In short, flip the lefts in in-order to rights and keep inserting 
# nodes to the beginning of the visited list )
#
# def postorderTraversal(root):
#    if not root:
#        return []
#    current = root
#    post_order_list = []
#    while current:
#        if not current.right:
#            post_order_list.insert(0, current.val)
#            current = current.left
#        else:
#            # find left most of the right sub-tree
#            predecessor = current.right
#            while (predecessor.left) and (predecessor.left != current):
#                predecessor = predecessor.left
#            # and create a link from this to current
#            if not predecessor.left:
#                post_order_list.insert(0, current.val)
#                predecessor.left = current
#                current = current.right
#            else:
#                predecessor.left = None
#                current = current.left
#    return post_order_list
#
# ---------------------------------------------------------------------------
# Using stack
#
# TC: O(n)
# SC: O(h)
#
# In pre-order, the order should be
#
# root -> left -> right
#
# But when we use stack, the order should be reversed:
#
# right -> left -> root
#
# Preorder Traversal
#
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res, stack = [], [(root, False)]
#         while stack:
#             node, visited = stack.pop()  # the last element
#             if not node:
#                 continue
#             if visited:
#                 res.append(node.val)
#             else:  # preorder: root -> left -> right
#                 stack.append((node.right, False))
#                 stack.append((node.left, False))
#                 stack.append((node, True))
#         return res
#
#
# In inorder, the order should be
# left -> root -> right
#
# But when we use stack, the order should be reversed:
#
# right -> root -> left
#
# Inorder Traversal
#
# class Solution2(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result, stack = [], [(root, False)]
#         while stack:
#             root, is_visited = stack.pop()  # the last element
#             if root is None:
#                 continue
#             if is_visited:
#                 result.append(root.val)
#             else:  # inorder: left -> root -> right
#                 stack.append((root.right, False))
#                 stack.append((root, True))
#                 stack.append((root.left, False))
#         return result
#
# In postorder, the order should be
# left -> right -> root
#
# But when we use stack, the order should be reversed:
#
# root -> right -> left
#
# Postorder Traversal
#
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res, stack = [], [(root, False)]
#         while stack:
#             node, visited = stack.pop()  # the last element
#             if not node:
#                 continue
#             if visited:
#                 res.append(node.val)
#             else:  # postorder: left -> right -> root
#                 stack.append((node, True))
#                 stack.append((node.right, False))
#                 stack.append((node.left, False))
#         return res
#