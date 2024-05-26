from binary_tree import Node, draw_trees


def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.right.left.left = Node(10)
    root.right.left.right = Node(11)
    root.left.right.left = Node(12)
    root.left.right.right = Node(13)
    root.left.left.left.left = Node(14)
    root.left.left.left.right = Node(15)
    root.right.right.left = Node(16)
    root.right.right.right = Node(17)

    draw_trees(root)


if __name__ == '__main__':
    main()
