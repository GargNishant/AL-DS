# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
from intro import LinkedList, Node

class LinkedList_2(LinkedList):

    def get_from_last(self,pos):
        main_ = self.head
        ref_ = self.head
        steps = 0
        while main_ is not None:
            main_ = main_.next

            if steps == pos:
                ref_ = ref_.next
            else:
                steps += 1
        if not steps == pos:
            return None
        return ref_.data

if __name__ == "__main__":
    llist = LinkedList_2()
    head = Node(20)
    llist.append(head)
    llist.append(Node(4))
    llist.append(Node(15))
    llist.append(Node(35))
    result = llist.get_from_last(4)
    print(result)