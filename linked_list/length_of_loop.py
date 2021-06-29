# https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/
from intro import LinkedList, Node


class LinkedList_Loop(LinkedList):

    def create_loop(self, start_pos):
        current = self.head
        start = self.head
        pos = 0
        while current.next is not None:
            current = current.next
            if not pos == start_pos:
                start = start.next
                pos += 1
        current.next = start

    def loop_length(self):
        start = self.loop_start_point()
        end = start.next
        counter = 1
        while not end == start:
            end = end.next
            counter += 1
        return counter

    def loop_start_point(self):
        slow = self.head.next
        fast = slow.next
        if self.head.next is None or self.head.next.next is None:
            return -1
        while fast.next is not None or fast is not None:
            if fast == slow:
                return fast
            fast = fast.next.next
            slow = slow.next


if __name__ == "__main__":
    Llist = LinkedList_Loop()
    Llist.append(Node(0))
    Llist.append(Node(1))
    Llist.append(Node(2))
    Llist.append(Node(3))
    Llist.append(Node(4))
    Llist.append(Node(5))
    Llist.append(Node(6))
    Llist.append(Node(7))
    Llist.append(Node(8))
    Llist.append(Node(9))
    Llist.append(Node(10))
    Llist.create_loop(5)
    # Llist.print_list()
    print(Llist.loop_length())