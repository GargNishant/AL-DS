
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, node:Node):
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(str(temp.data))
            temp = temp.next

    def new_head(self,node: Node):
        node.next, self.head = self.head, node

    def insert(self, new_data, prev_node: Node):
        current = self.head
        if current is None:
            raise ValueError("LinkedList cannot be empty")
        while not current == prev_node:
            if current is None:
                raise ValueError("Given Node not found")
            current = current.next
        temp = current.next
        current.next = Node(new_data)
        current.next.next = temp


if __name__ == "__main__":
    Llist = LinkedList()
    node = Node(6.5)
    Llist.append(Node(0))
    Llist.append(Node(1))
    Llist.append(Node(2))
    Llist.append(Node(3))
    Llist.append(Node(4))
    Llist.append(node)
    Llist.append(Node(5))
    Llist.append(Node(6))
    Llist.insert(4.3,node)
    Llist.new_head(Node(0.3))
    Llist.print_list()




