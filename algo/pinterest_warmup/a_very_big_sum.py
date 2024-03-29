"""In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .
Return

long: the sum of all array elements
Input Format

The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.

Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005
Output

5000000015

"""


def a_very_big_sum(ar):
    # agg = 0
    # for num in ar:
    #   agg += num
    # return agg
    return sum(ar)


def recursive_sum(nums):
    if len(nums) == 1:
        return nums[0]

    # current = nums[nums.length()]
    # int[] nums = Arrays.copyOfRange(nums, 1, nums.length());
    # return current + recursive_sum(nums)
    return nums.pop() + recursive_sum(nums)


def main():
    nums = [90, 90, 1]
    print(a_very_big_sum(nums))
    print(recursive_sum(nums))

    res = a_very_big_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
    print(res)
    # assert res == 5000000015


if __name__ == '__main__':
    main()
