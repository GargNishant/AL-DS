
# https://www.geeksforgeeks.org/level-order-tree-traversal/

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def dfs(node:Node):
    if node is None:
        return
    dfs(node.left)
    print(node.data, end=" ")
    dfs(node.right)


def main():
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    dfs(root)

if __name__ == "__main__":
    main()