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
    print(node.data)
    in_order(node.right_child)


def pre_order(node:Node):
    if node is None:
        return
    print(node.data)
    pre_order(node.left_child)
    pre_order(node.right_child)

def post_order(node:Node):
    if node is None:
        return
    post_order(node.left_child)
    post_order(node.right_child)
    print(node.data)

def main():
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)
    print("In Order",in_order(root))
    print("pre_order Order", pre_order(root))
    print("post_order Order", post_order(root))

if __name__ == "__main__":
    main()