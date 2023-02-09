# Enter your code here. Read input from STDIN. Print output to STDOUT
def quick_sort(n, ar):
    if n < 2:
        return ar
    else:
        pivot = ar[0]
        left, right = [], []
        for element in ar:
            if element < pivot:
                left.append(element)
            if element > pivot:
                right.append(element)
        arr1 = quick_sort(len(left), left) + [pivot] + quick_sort(len(right), right)
        print(*arr1)
    return arr1


def quicksort(n, arr):
    if n < 2:
        return arr
    else:
        pivot = int(arr.pop())

    left, right = [], []
    for element in arr:
        if element > pivot:
            right.append(element)
        else:
            left.append(element)
    arr1 = quicksort(len(left), left) + [pivot] + quicksort(len(right), right)
    print(*arr1, sep=" ")
    return arr1


def main():
    arr = [5, 8, 1, 3, 7, 9, 2]
    quick_sort(len(arr), arr)
    print('=============')
    arr2 = [5, 8, 1, 3, 7, 9, 2]
    quicksort(len(arr2), arr2)  # yt


if __name__ == '__main__':
    main()
