# Program to print all combination
# of size r in an array of size n

# The main function that prints
# all combinations of size r in
# arr[] of size n. This function
# mainly uses combinationUtil()
def printCombination(arr, n, r): # combinacion | permutacion. 1234 n = 4  possibles= 10 10pn = 4 * 10 * 4.
                                 # permutacione s una combinacion ordernada | 4444. 3333 | n!(n-p)/ (n *p) =
    # A temporary array to
    # store all combination
    # one by one
    data = [0] * r;

    # Print all combination
    # using temporary array 'data[]'

    combinationUtil(arr, data, 0,
                    n - 1, 0, r)

# arr[] ---> Input Array
# data[] ---> Temporary array to
#		 store current combination
# start & end ---> Starting and Ending
#			 indexes in arr[]
# index ---> Current index in data[]
# r ---> Size of a combination
# to be printed
def combinationUtil(arr, data, start, end, index, r):
    # Current combination is ready
    # to be printed, print it
    if (index == r):
        for j in range(r):
            print(data[j], end=" ")
        print()
        return

    # replace index with all
    # possible elements. The
    # condition "end-i+1 >=
    # r-index" makes sure that
    # including one element at
    # index will make a combination
    # with remaining elements at
    # remaining positions
    i = start
    while (i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1, end, index + 1, r)
        i += 1


# Driver Code
arr = [1, 2, 3, 4, 5] # permutaciones sin repeteciones. ||
r = 2
n = len(arr)
printCombination(arr, n, r)
