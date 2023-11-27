from .node import Node, create_example_tree


def preorder(root_node: Node):
    print(root_node.value, end=" ")
    if root_node.left:
        preorder(root_node.left)
    if root_node.right:
        preorder(root_node.right)


def test_preorder(root_node: Node):
    assert preorder(root_node) == '1 2 5 3 4 6'


if __name__ == '__main__':
    root = create_example_tree()
    preorder(root)
    # test_preorder(root)
    # 1 2 5 3 4 6

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
