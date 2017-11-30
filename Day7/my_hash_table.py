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
        new_node = LinkedListNode(value)

        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.right = new_node
            new_node.left = self.end
            self.end = new_node