def binary_search(some_array, searching):
    left = 0
    right = len(some_array) - 1

    while left <= right:
        median = int((left + right) / 2)
        print("index: ", median)
        print(some_array[median])

        if searching > some_array[median]:
            left = median + 1
        elif searching < some_array[median]:
            right = median - 1
        else:
            return True

    return False


if __name__ == '__main__':
    some_array = [1, 2, 3, 22, 45, 67, 89, 100, 200, 201, 1023]
    result = binary_search(some_array, searching=22)

    print(result)
