"""
Given the pointer to the head node of a linked list and an integer to insert at a certain position,
create a new node with the given integer as its  attribute, insert this node at the desired position
and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on.
The head pointer given may be null meaning that the initial list is empty.

Example
 refers to the first node in the list


Insert a node at position 2 with data=4 . The new list is 1 -> 2 -> 3 -> 4

Function Description Complete the function insertNodeAtPosition in the editor below. It must return a reference to the
head node of your finished list.

insertNodeAtPosition has the following parameters:

head: a SinglyLinkedListNode pointer to the head of the list
data: an integer value to insert as data in your new node
position: an integer position to insert the new node, zero based indexing
Returns

SinglyLinkedListNode pointer: a reference to the head of the revised list
Input Format

The first line contains an integer n, the number of elements in the linked list.
Each of the next  lines contains an integer SinglyLinkedListNode[i].data.
The next line contains an integer data, the data of the node that is to be inserted.
The last line contains an integer position.
"""


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node):
    chain = ''
    while node:
        chain += str(node.data)
        if node.next is not None:
            chain += '->'
        node = node.next

    return chain


def insert_node_at_position(llist, data, position):
    # Write your code here
    head = llist
    if head is None:
        return SinglyLinkedListNode(data)
    aux_node = head
    while position > 0:
        if position == 1:
            next_node = aux_node.next
            aux_node.next = SinglyLinkedListNode(data)
            aux_node.next.next = next_node
        position -= 1
        aux_node = aux_node.next
    return head


def main():
    llist = SinglyLinkedListNode(16)
    llist.next = SinglyLinkedListNode(13)
    llist.next.next = SinglyLinkedListNode(7)

    res = insert_node_at_position(llist, 1, 2)
    res = print_singly_linked_list(res)

    llist = SinglyLinkedListNode(16)
    llist.next = SinglyLinkedListNode(13)
    llist.next.next = SinglyLinkedListNode(1)
    llist.next.next.next = SinglyLinkedListNode(7)
    llist = print_singly_linked_list(llist)

    assert llist == res


if __name__ == '__main__':
    main()
