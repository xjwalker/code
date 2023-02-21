"""
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below.

rotLeft has the following parameter(s):

int a[n]: the array to rotate
int d: the number of rotations
Returns

int a'[n]: the rotated array
Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations.
The second line contains  space-separated integers, each an .

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4

"""


def left_rotation(arr, n_rotations):
    return arr[n_rotations:] + arr[:n_rotations]


def main():
    res = left_rotation([1, 2, 3, 4, 5], 4)
    assert res == [5, 1, 2, 3, 4]
    res = left_rotation([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10)
    assert res == [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]


if __name__ == '__main__':
    main()
