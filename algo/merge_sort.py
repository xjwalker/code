# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                print(f'setting value: {L[i]} to position: {k}')
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                print(f'setting value: {R[j]} to position: {k}')
                j += 1
            k += 1
        print('--')
        # Checking if any element was left
        while i < len(L):
            print(f"putting {L[i]} in position {k}")
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            print(f"putting {R[j]} in position {k}")
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 90, 89, 13, 87, -9]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

# This code is contributed by Mayank Khanna
