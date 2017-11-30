class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def search(self, value):
        if self.value == value:
            return self

        if self.right is None:
            return None

        return self.right.search(value)

    def delete(self):
        previous_node = self.left
        next_node = self.right

        self.right = None
        self.left = None

        if previous_node is not None:
            previous_node.right = next_node

        if next_node is not None:
            next_node.left = previous_node


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

    def is_empty(self):
        if self.start is None:
            return True
        else:
            return False

    def has_only_one_node(self):
        if not self.is_empty() and self.start == self.end:
            return True
        else:
            return False

    def remove_last_node(self):
        if self.is_empty():
            return
        elif self.has_only_one_node():
            self.start = None
            self.end = None
        else:
            second_to_last = self.end.left

            second_to_last.right = None
            self.end.left = None

            self.end = second_to_last

    def search(self, value):
        if self.start is None:
            return None

        self.start.search(value)

    def delete_at_index(self, target_index):
        i = 0
        current_node = self.start

        while current_node is not None:
            if i == target_index:
                node_i_want_to_delete = current_node
                break;

            current_node = current_node.right
            i += 1

        if node_i_want_to_delete == self.start:
            self.start = node_i_want_to_delete.right

        if node_i_want_to_delete == self.end:
            self.end = node_i_want_to_delete.left

        node_i_want_to_delete.delete()



    def print_all_node_values(self):
        current_node = self.start
        while current_node is not None:
            print current_node.value
            current_node = current_node.right

ll = LinkedList()
ll.append(10)
ll.append(15)
ll.append(20)
ll.append(25)

print "First Run"
ll.print_all_node_values()

ll.delete_at_index(0)

print "Second Run"
ll.print_all_node_values()