def not_sliding_windows():
    friends = [32, 9, 32, 19, 30, 23, 22, 27, 29, 31, 31, 31]

    highest_group = float('-Inf')
    for i in range(len(friends) - 2):
        avg = (friends[i] + friends[i + 1] + friends[i + 2]) / 3
        highest_group = max(highest_group, avg)
    print(highest_group)


def max_sum_subarray(arr, k):
    n = len(arr)
    max_sum = 0

    # Calculate the sum of the first window
    for i in range(k):
        max_sum += arr[i]

    current_sum = max_sum

    # Slide the window through the array
    for i in range(k, n):
        current_sum = current_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum


def min_sum_array(arr, k):
    start = 0
    curr_count = 0
    min_val = float('Inf')
    for i, num in enumerate(arr):
        curr_count += num
        if i - start + 1 >= k:
            min_val = min(curr_count, min_val)
            curr_count -= arr[start]
            start += 1
    return min_val


if __name__ == '__main__':
    print("not sliding window")
    not_sliding_windows()

    # Example usage:
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 3
    result = max_sum_subarray(arr, k)
    print("max")
    print(result)

    arr = [10, 4, 2, 5, 6, 3, 8, 1]
    k = 3

    print("min:")
    print(min_sum_array(arr, k))
