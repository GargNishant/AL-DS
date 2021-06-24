
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

    def delete_node(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        current = self.head
        while current is not None:
            if current.next is None:
                break
            if current.next.data == key:
                current.next = current.next.next
                break
            current = current.next

    def get_count_iter(self,node):
        current = node
        result = 0
        while current.next is not None:
            result += 1
            current = current.next
        return result + 1

    def get_count_rec(self,node:Node):
        if node.next is None:
            return 1
        return 1 + self.get_count_rec(node.next)

    def get_count(self, func):
        if func == 'iter':
            return self.get_count_iter(self.head)
        elif func == 'recursive':
            return self.get_count_rec(self.head)


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
    Llist.delete_node(0)
    Llist.new_head(Node(0.3))
    Llist.print_list()
    print(f"Recursive count is:{Llist.get_count('recursive')}")
    print(f"Iterative count is:{Llist.get_count('iter')}")
