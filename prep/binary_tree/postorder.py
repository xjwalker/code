from .node import Node


def postorder(root: Node):
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)

    print(root.value, end=" ")


if __name__ == '__main__':
    node = Node(None).create_example_tree()
    postorder(node)

"""
     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4
"""
