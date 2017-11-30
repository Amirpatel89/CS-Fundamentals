from binarytree import Node, show
import numpy.random as nprnd


class MyBinaryTreeNode(Node):
	def __init__(self, value):
		self.value = value
		self.parent = None
		# self.children = []
		self.left = None
		self.right = None

	# def add_child(self, child_node):
	# 	self.children.append(child_node)
	# 	child_node.parent = self

	# def remove_child(self, child_node):
	# 	del self.children[self.children.indexof(child_node)]

	def add(self, new_node):
		if new_node.value >= self.value:
			if self.right is None:
				self.right = new_node
				new_node.parent = self
			else:
				self.right.add(new_node)

		else: 
			if self.left is None:
				self.left = new_node
				new_node.parent = self
			else:
				self.left.add(new_node)

	def exists(self, value):
		if self.value == value:
			return True


class BST:
		def __init__(self):
			self.root = None
		def add(self, value):
			new_node = MyBinaryTreeNode(value)

			if self.root is None:
				self.root = new_node
			else:
				self.root.add(new_node)

		def exists(self, value):

			if self.root is None:
				return False
			else:
				self.root.exists(value)

def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]


tree = BST()
for i in random_numbers(25):
	tree.add(i)



# tree.add(10)
# tree.add(20)
# tree.add(-1)
# tree.add(22)
# tree.add(5)

show(tree.root)
# root = MyTreeNode(5)
# root.add_child(MyTreeNode(10))
# root.add_child(MyTreeNode(20))

# for child in root.children:
# 	print child.value