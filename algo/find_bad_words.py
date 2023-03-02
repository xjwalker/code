class Node:
    def __init__(self, value):
        self.value = None
        self.left = None
        self.right = None
        self.is_leaf = False


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return self.root

        aux_node = self.root
        while aux_node:
            aux_node = aux_node.left




def find_bad_words(bad_words, phrase):
    for bad_word in bad_words:
        if bad_word in phrase:
            return True

    return False


def main():
    bad_words = ['hate u', 'hatred']
    phrase = 'i hate u, but i love you'
    print(find_bad_words(bad_words, phrase))

    phrase = 'Oh man, i hate u'
    print(find_bad_words(bad_words, phrase))

    phrase = 'I love you'
    print(find_bad_words(bad_words, phrase))

    phrase = 'hatred-not'
    print(find_bad_words(bad_words, phrase))


if __name__ == '__main__':
    main()
