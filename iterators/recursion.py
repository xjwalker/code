def iterate_list(elements):
    if len(elements) <= 1:
        return elements[0]
    print(elements.pop())
    return iterate_list(elements)


def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    print(iterate_list([1, 2, 3, 4, 5, 6, 7]))
    print('-')
    # print(fib(40))
