"""
You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree. You just have to complete the function.

Input Format

You are given a function,

Node * insert (Node * root ,int data) {

}
Constraints

No. of nodes in the tree  500
Output Format

Return the root of the binary search tree after inserting the value into the tree.

Sample Input

        4
       / \
      2   7
     / \
    1   3
The value to be inserted is 6.

Sample Output

         4
       /   \
      2     7
     / \   /
    1   3 6
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def pre_order(root):
    if root == None:
        return

    print(root.info, end=" ")
    pre_order(root.left)
    pre_order(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, info):
        if not self.root:
            self.root = Node(info)
            return self.root

        self.traverse(self.root, info)

    def traverse(self, head, info):
        if head is None:
            return None

        if info > head.info:
            res = self.traverse(head.right, info)
            if not res:
                head.right = Node(info)
        else:
            res = self.traverse(head.left, info)
            if not res:
                head.left = Node(info)

        return head


def main():
    t = 6
    arr = [4, 2, 7, 1, 3, 6]
    tree = BinarySearchTree()
    for i in range(t):
        tree.insert(arr[i])
    pre_order(tree.root)
    # should print: 4 2 1 3 7 6


if __name__ == '__main__':
    main()
