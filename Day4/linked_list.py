class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

class LinkedList:
	def __init__(self):
		self.start = None
		self.end = None

	def append(self, value):
		new_node = LinkedLIstNode(value)

		if self.start is None:
			self.start = new_node
			self.end = new_node
		else:
			self.end.right = new_node
			new_node.left = self.end
			self.end = new_node

	def search(self, value):
		current_node = self.start

		while current_node is not None:
			print(current_node.value)
			current_node = current_node.right
			if current_node.value == value:
				return current_node

linked_list = LinkedList()

for i in range(100):
	linked_list.append(i)
if result is not None:
result = linked_list.search(50)
else:
	print "Value not found."


a = LinkedLIstNode(10)
b = LinkedLIstNode(15)

a.right = b
b.left = a