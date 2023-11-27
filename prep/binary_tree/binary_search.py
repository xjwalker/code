def binary_search(elements, value):

    size = len(elements)

    low = 0
    
    while True:
        mid = elements[size//2]

        if value > elements[mid]:
            print()
        elif value < elements[mid]:
            print()
        elif value == elements[mid]:
            return mid

    return -1

