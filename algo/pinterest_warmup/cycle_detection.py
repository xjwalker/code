"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise, return 0.

Example

 refers to the list of nodes 1 -> 2 -> 3 -> null

The numbers shown are the node numbers, not their data values. There is no cycle in this list so return 0.

 refers to the list of nodes 1 -> 2 -> 3 -> null

There is a cycle where node 3 points back to node 1, so return 1.

Function Description

Complete the has_cycle function in the editor below.

It has the following parameter:

SinglyLinkedListNode pointer head: a reference to the head of the list
Returns

int: 1  if there is a cycle or 0 if there is not
Note: If the list is empty, head will be null.

Input Format

The code stub reads from stdin and passes the appropriate argument to your function.
The custom test cases format will not be described for this question due to its complexity. Expand the section for the main function and review the code if you would like to figure out how to create a custom case.
"""


class Node:
    data = None

    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    viewed_nodes = set()
    if head is None or head.next is None:
        return 1
    aux_node = head
    while aux_node is not None:
        if aux_node not in viewed_nodes:
            viewed_nodes.add(aux_node)
        else:
            return 1
        aux_node = aux_node.next
    return 0


def main():
    llist = Node(1)
    llist.next = Node(2)
    llist.next.next = Node(3)
    res = has_cycle(llist)
    assert res == 0

    llist = Node(1)
    llist.next = Node(2)
    llist.next.next = llist
    res = has_cycle(llist)  # <- circular reference.
    assert res == 1


if __name__ == '__main__':
    main()
