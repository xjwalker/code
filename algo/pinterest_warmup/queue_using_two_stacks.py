"""
A queue is an abstract data type that maintains the order in which elements were added to it,
allowing the oldest elements to be removed from the front and new elements to be added to the rear.
 This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue
 (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks.
Then process q queries, where each query is one of the following 3 types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
Input Format

The first line contains a single integer, q, denoting the number of queries.
Each line i of the q subsequent lines contains a single query in the form described in the problem statement above.
All three queries start with an integer denoting the query type,
but only query 1 is followed by an additional space-separated value, z, denoting the value to be enqueued.

Output Format

For each query of type , print the value of the element at the front of the queue on a new line.

Sample Input

STDIN   Function
-----   --------
10      q = 10 (number of queries)
1 42    1st query, enqueue 42
2       dequeue front element
1 14    enqueue 42
3       print the front element
1 28    enqueue 28
3       print the front element
1 60    enqueue 60
1 78    enqueue 78
2       dequeue front element
2       dequeue front element
Sample Output

14
14


Explanation

Perform the following sequence of actions:

Enqueue 42; {42}.
Dequeue the value at the head of the queue, 42; {}.
Enqueue 14; {14}.
Print the value at the head of the queue, 14; {14}.
Enqueue 28; {14,28}.
Print the value at the head of the queue, 14;{14, 28} .
Enqueue 60; {14, 28, 60}.
Enqueue 78; {14,28, 60, 78}.
Dequeue the value at the head of the queue, 14; {28, 60, 78}.
Dequeue the value at the head of the queue, 28; {60, 78}.
"""


class QueueC:
    def __init__(self):
        self.q = []
        self.aux_queue = []

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):  # 14, 28, 60, 78
        aux = self.q[0]
        del self.q[0]
        self.aux_queue = self.q[::-1]
        self.q = self.aux_queue[::-1]
        return aux

    def printFront(self):
        print(self.q[0])


def main():
    q = QueueC()
    q.enqueue(42)
    q.dequeue()
    q.enqueue(14)
    q.printFront()
    q.enqueue(28)
    q.printFront()
    q.enqueue(60)
    q.enqueue(78)
    q.dequeue()
    q.dequeue()


if __name__ == '__main__':
    main()
