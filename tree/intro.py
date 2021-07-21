# https://www.geeksforgeeks.org/binary-tree-set-1-introduction/

# What is height of Binary Tree? Relation between Nodes and height?
# https://www.geeksforgeeks.org/relationship-number-nodes-height-binary-tree/

# Important Theory: https://www.geeksforgeeks.org/binary-tree-set-2-properties/

# Types of Binary Tree: https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def main():
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)


if __name__ == "__main__":
    main()