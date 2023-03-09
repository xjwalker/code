class Node:

    def __init__(self, value=None):
        self.val = value
        self.children = []


def is_mirror_tree(root):
    if not root:
        return True

    return is_mirror_tree_helper(root.children)


def is_mirror_tree_helper(children):
    n = len(children)
    if n == 0:
        return True
    elif n % 2 != 0:
        return False

    for i in range(n // 2):
        left = children[i]
        right = children[n - i - 1]
        if left.val != right.val:
            return False
        if not is_mirror_tree_helper(left.children) or not is_mirror_tree_helper(right.children):
            return False

    return True


def main():
    root = Node(10)
    root.children = [Node(5), Node(5)]
    root.children[0].children = [Node(3), Node(6)]
    root.children[1].children = [Node(6), Node(3)]
    res = is_mirror_tree(root)

    print(res)


if __name__ == '__main__':
    main()
