# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


class Node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None


def in_order(node:Node):
    if node is None:
        return
    in_order(node.left_child)
    print(node.data, end=" ")
    in_order(node.right_child)


def in_order_while(node:Node):
    current: Node = node
    stack = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.left_child
            continue
        elif len(stack) > 0:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right_child
            continue
        else:
            break


def pre_order(node:Node):
    if node is None:
        return
    print(node.data, end=" ")
    pre_order(node.left_child)
    pre_order(node.right_child)


def post_order(node:Node):
    if node is None:
        return
    post_order(node.left_child)
    post_order(node.right_child)
    print(node.data, end=" ")



def main():
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)
    print(in_order(root),"In Order")
    print(in_order_while(root),"In Order while")
    print(pre_order(root),"pre_order Order")
    print(post_order(root),"post_order Order")

if __name__ == "__main__":
    main()