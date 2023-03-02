"""
The height of a binary tree is the number of edges between the tree's root and its furthest leaf.
For example, the following binary tree is of height :

image
Function Description

Complete the getHeight or height function in the editor. It must return the height of a binary tree as an integer.

getHeight or height has the following parameter(s):

root: a reference to the root of a binary tree.
Note -The Height of binary tree with single node is taken as zero.

Input Format

The first line contains an integer , the number of nodes in the tree.
Next line contains  space separated integer where th integer denotes node[i].data.

Note: Node values are inserted into a binary search tree before a reference to the tree's root node
is passed to your function.
In a binary search tree, all nodes on the left branch of a node are less than the node value.
All values on the right branch are greater than the node value.
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    agg = 0
    left = traverse(root.left, agg)
    right = traverse(root.right, agg)

    total = max(left, right)
    return total


def traverse(root, agg=0):
    if root is None:
        return agg

    left = traverse(root.left, agg + 1)
    right = traverse(root.right, agg + 1)

    total = max(left, right)

    return total


def main():
    tree = BinarySearchTree()
    t = 7
    arr = [3, 5, 2, 1, 4, 6, 7]
    for i in range(t):
        tree.create(arr[i])

    res = height(tree.root)
    assert res == 3

    tree = BinarySearchTree()
    t = 1
    arr = [15]
    for i in range(t):
        tree.create(arr[i])
    res = height(tree.root)
    assert res == 0

    tree = BinarySearchTree()
    t = 5
    arr = [3, 1, 7, 5, 4]
    for i in range(t):
        tree.create(arr[i])
    res = height(tree.root)
    assert res == 3


if __name__ == '__main__':
    main()
