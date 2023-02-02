def insertion_sort2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(*arr, sep=" ")


def third_is(arr):
    for i in range(1, len(arr)):
        while arr[i] < arr[i - 1] and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
        print(*arr, sep=" ")
    return arr


if __name__ == '__main__':
    arr = [1, 50, 3, 23, 2, 32, 30]
    insertion_sort2(arr)
    print('===')
    arr = [1, 50, 3, 23, 2, 32, 30]
    third_is(arr)
