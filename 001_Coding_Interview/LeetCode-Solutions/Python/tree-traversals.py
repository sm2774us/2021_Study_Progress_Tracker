from typing import List

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
#  IN-ORDER TRAVERSAL
#  1->2->3->4->5
#
#  PRE-ORDER TRAVERSAL
#  4->2->1->3->5->3
#
#  POST-ORDER TRAVERSAL
#  1->3->2->3->5->4


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# TC: O(n)
# SC: O(1)
class MorrisTraversals:
	def inorderTraversal(self, root: 'TreeNode') -> List[int]:
		if not root:
			return []
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
					node.right = curr
					curr = curr.left

				# fix the right child of prev
				else:
					result.append(curr.val)
					node.right = None
					curr = curr.right
		return result

	def preorderTraversal(self, root: 'TreeNode') -> List[int]:
		if not root:
			return []
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

	def postorderTraversal(self, root: 'TreeNode') -> List[int]:
		if not root:
			return []
		# Set current to root of binary tree
		result, curr = [], root
		while curr:
			if curr.right is None:
				result.insert(0, curr.val)
				curr = curr.left
			else:
				# Find the left most of the right sub-tree 
				node = curr.right
				while node.left and node.left != curr:
					node = node.left

				# and create a link from this to the curr
				if node.left is None:
					result.insert(0, curr.val)
					node.left = curr
					curr = curr.right
				else:
					node.left = None
					curr = curr.left
		return result


# TC: O(n)
# SC: O(h)
# where, h : height of the tree
class StackBasedTraversals:
	def inorderTraversal(self, root: 'TreeNode') -> List[int]:
		if not root:
			return []
		# Set current to root of binary tree
		result, stack = [], [(root, False)]
		while stack:
			root, is_visited = stack.pop()
			if root is None:
				continue
			if is_visited:
				result.append(root.val)
			else:	# in-order: left -> root -> right
				stack.append((root.right, False))
				stack.append((root, True))
				stack.append((root.left, False))
		return result

	def preorderTraversal(self, root: 'TreeNode') -> List[int]:
		if not root:
			return []
		# Set current to root of binary tree
		result, stack = [], [(root, False)]
		while stack:
			root, is_visited = stack.pop()
			if root is None:
				continue
			if is_visited:
				result.append(root.val)
			else:	# pre-order: root -> left -> right
				stack.append((root.right, False))
				stack.append((root.left, False))
				stack.append((root, True))
		return result

	def postorderTraversal(self, root: 'TreeNode') -> List[int]:
		if not root:
			return []
		# Set current to root of binary tree
		result, stack = [], [(root, False)]
		while stack:
			root, is_visited = stack.pop()
			if root is None:
				continue
			if is_visited:
				result.append(root.val)
			else:	# post-order: left -> right -> root
				stack.append((root, True))
				stack.append((root.right, False))
				stack.append((root.left, False))
		return result

if __name__ == "__main__":
	node = TreeNode(4)
	node.left = TreeNode(2)
	node.right = TreeNode(5)
	node.left.left = TreeNode(1)
	node.left.right = TreeNode(3)
	node.right.left = TreeNode(3)

	# Morris Traversal is a way of traversing BST with O(1) space and O(n) time.
	# It's a little hard to understand but the basic idea is to link predecessor back to current node
	# so that we can trace back to top of BST.	
	morrisTraversals = MorrisTraversals()
	print(f'In-Order-Traversal (Morris): {morrisTraversals.inorderTraversal(node)}')
	print(f'Pre-Order-Traversal (Morris): {morrisTraversals.preorderTraversal(node)}')
	print(f'Post-Order-Traversal (Morris): {morrisTraversals.postorderTraversal(node)}')

	stackBasedTraversals = StackBasedTraversals()
	print(f'In-Order-Traversal (Stack): {stackBasedTraversals.inorderTraversal(node)}')
	print(f'Pre-Order-Traversal (Stack): {stackBasedTraversals.preorderTraversal(node)}')
	print(f'Post-Order-Traversal (Stack): {stackBasedTraversals.postorderTraversal(node)}')