"""In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same approach repeatedly, can you sort an entire array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to.

In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.

Example.

n = 7
arr = [3, 4, 7, 5, 6, 2, 1]

Working from left to right, we get the following output:

3 4 7 5 6 2 1
3 4 7 5 6 2 1
3 4 5 7 6 2 1
3 4 5 6 7 2 1
2 3 4 5 6 7 1
1 2 3 4 5 6 7

Function Description

Complete the insertionSort2 function in the editor below.

insertionSort2 has the following parameter(s):

int n: the length of arr
int arr[n]: an array of integers
Prints

At each iteration, print the array as space-separated integers on its own line.

Input Format

The first line contains an integer, n, the size of arr.
The next line contains n space-separated integers arr[i].

6               n = 6
1 4 3 5 6 2     arr = [1, 4, 3, 5, 6, 2]

1 4 3 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 2 3 4 5 6
"""


def insert_sort_p2(arr):
    for i in range(len(arr) - 1, -1, -1):
        aux_index = i
        aux_index_2 = aux_index - 1
        while arr[aux_index] < arr[aux_index_2] and i >= 1:
            arr[aux_index_2], arr[aux_index] = arr[aux_index], arr[aux_index_2]
            aux_index -= 1
            aux_index_2 -= 1
        print(*arr, sep=' ')
    return arr


def insert_sort_2(arr):  # <- this prints the arr as wanted.
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
            print(*arr, sep=' ')
    return arr


def main():
    arr = [1, 4, 3, 5, 6, 2]
    # result = insert_sort_p2(arr)
    result = insert_sort_2(arr)
    assert result == [1, 2, 3, 4, 5, 6]


if __name__ == '__main__':
    main()
    """
    1 4 3 5 6 2 
    1 3 4 5 6 2 
    1 3 4 5 6 2 
    1 3 4 5 6 2 
    1 2 3 4 5 6 
"""
