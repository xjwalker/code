def insert_sort(some_array):

    for j in range(len(some_array) - 1):
        i = j + 1
        while some_array[j] > some_array[i]:
            aux = some_array[j]
            some_array[j] = some_array[i]
            some_array[i] = aux
        i += 1
    return some_array


if __name__ == '__main__':
    arr = [1, 50, 3, 23, 2, 32]
    print(arr)
    print(insert_sort(arr))
