"""
This question is designed to help you get a better understanding of basic heap operations.

There are 3 types of query:

"1 v" - Add an element v to the heap.
"2 v" - Delete the element v from the heap.
"3" - Print the minimum of all the elements in the heap.
NOTE: It is guaranteed that the element to be deleted will be there in the heap.
Also, at any instant, only distinct elements will be in the heap.

Input Format

The first line contains the number of queries, Q.
Each of the next Q lines contains one of the 3 types of query.


Output Format

For each query of type 3, print the minimum value on a single line.

Sample Input

STDIN       Function
-----       --------
5           Q = 5
1 4         insert 4
1 9         insert 9
3           print minimum
2 4         delete 4
3           print minimum
Sample Output

4
9
Explanation

After the first 2 queries, the heap contains {4, 9}. Printing the minimum gives 4 as the output.
Then, the 4th query deletes 4 from the heap, and the 5th query gives 9 as the output.
"""


def add(arr: list, val: int) -> list:
    arr.append(val)
    current = len(arr) - 1
    while True:
        parent = (current - 1) // 2
        if current == 0:
            break
        elif arr[parent] > arr[current]:
            arr[current], arr[parent] = arr[parent], arr[current]
            current = parent
        else:
            break

    return arr


def delete(arr: list, val: int):
    '''
    Assuming that any value given to search is present in the heap
    '''

    if val not in arr:
        return

    parent = arr.index(val)
    arr[parent] = arr[-1]
    arr.pop()

    while parent < len(arr):

        left = parent * 2 + 1
        right = parent * 2 + 2

        if left > len(arr) - 1:
            break

        if right > len(arr) - 1:
            if arr[parent] > arr[left]:
                arr[parent], arr[left] = arr[left], arr[parent]
            break

        l_val = arr[left]
        r_val = arr[right]

        minimum = left if l_val < r_val else right

        if arr[parent] > arr[minimum]:
            arr[parent], arr[minimum] = arr[minimum], arr[parent]
            parent = minimum
        else:
            break

    return arr


def q_heap_1():
    heap = []
    add(heap, 4)
    add(heap, 9)
    print(heap[0])
    delete(heap, 4)
    print(heap[0])


def main():
    q_heap_1()


if __name__ == '__main__':
    main()
