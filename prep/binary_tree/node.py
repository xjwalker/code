class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def create_example_tree(self):
        root_node = Node(1)
        root_node.right = Node(2)
        root_node.right.right = Node(5)
        root_node.right.right.left = Node(3)
        root_node.right.right.right = Node(6)
        root_node.right.right.left.right = Node(4)
        return root_node
