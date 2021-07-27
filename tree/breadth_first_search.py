# https://www.geeksforgeeks.org/level-order-tree-traversal/

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def bfs(node:Node):
    queue = []
    queue.append(node)
    while len(queue) > 0:
        temp = queue.pop(0)
        print(temp.data)
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)

def main():
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    bfs(root)

if __name__ == "__main__":
    main()