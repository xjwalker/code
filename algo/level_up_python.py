def find_prime_factors(number: int) -> list:
    """
    630 -> [2, 3, 3, 5, 7]
    630/2: 315
    315/3: 105
    105/3: 35
    35/5: 7
    7/7: 0

    :param number: integer number
    :return: list of prime numbers that multiplied return the given number
    """
    if number % 2 != 0:
        return [number]
    result = []
    aux_prime_index = 2
    while number > 0 and aux_prime_index < number + 1:
        if number % aux_prime_index != 0:
            aux_prime_index += 1
        else:
            number = number / aux_prime_index
            result.append(aux_prime_index)
    return result


def is_palindrome(word: str):
    abc = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', ' u',
           'v', 'w', 'x', 'y', 'z'}
    backwards = ''
    for i in range(len(word), 0, -1):
        if word[i].lower() not in abc:
            continue
        backwards += word[i].lower()

    forward = ''
    for i in range(len(word)):
        if word[i].lower() not in abc:
            continue
        forward += word[i].lower()

    print('f', forward)
    print('b', backwards)
    return forward == backwards


def is_palindrome_2(word: str) -> bool:
    import re
    forward = ''.join(re.findall(r'[a-z]+', word.lower()))
    backwards = forward[::-1]
    return forward == backwards


def sort_words(words: str) -> str:
    """ """
    return ' '.join(sorted(words.split(), key=str.casefold))


def find_all_results(items: list, search_value) -> list:
    list_of_indices = []
    for index, value in enumerate(items):
        if value == search_value:
            list_of_indices.append([index])
        elif isinstance(items[index], list):
            for i in find_all_results(items[index], search_value):
                list_of_indices.append([index] + i)

    return list_of_indices


from itertools import product


def solve_sudoku(sudoku_grid: list):
    for (row, column) in product(range(0, 9), repeat=2):
        if sudoku_grid[row][column] == 0:  # find unassigned cell
            for num in range(1, 10):
                allowed = True  # check if num is allowed in row/column/box
                for i in range(0, 9):
                    if num in (sudoku_grid[i][column], sudoku_grid[row][i]):
                        allowed = False
                        break  # not allowed in row or column
                for (i, j) in product(range(0, 3), repeat=2):
                    if sudoku_grid[row - row % 3 + i][column - column % 3 + j] == num:
                        allowed = False
                        break  # not allowed in box
                if allowed:
                    sudoku_grid[row][column] = num
                    if trial := solve_sudoku(sudoku_grid):
                        return trial
                    sudoku_grid[row][column] = 0
            return False  # could not place number in this cell
    return sudoku_grid


def print_sudoku(sudoku_grid):
    sudoku_grid = [['*' if num == 0 else num for num in row] for row in sudoku_grid]
    print()
    for row in range(0, 9):
        if (row % 3 == 0) and (row != 0):
            print('-' * 33)  # draw horizontal line
        for col in range(0, 9):
            if (col % 3 == 0) and col != 0:
                print(' | ', end='')  # draw vertical line
            print(f' {sudoku_grid[row][col]} ', end='')
        print()
    print()


def main():
    print('prime factors')
    print(find_prime_factors(630))
    print(find_prime_factors(13))

    print('palindrome')
    print(is_palindrome('hello world'))
    print(is_palindrome("go hang a salami - I'm a lasagna hog"))

    print('palindrome 2')
    print(is_palindrome_2('hello world'))
    print(is_palindrome_2("go hang a salami - I'm a lasagna hog"))

    print('sort words')
    print(sort_words('string of words'))

    print('find all elements in nested lists')
    print(find_all_results([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))
    print(find_all_results([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], [1, 2, 3]))

    print('sudoku')
    sudoku_grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                   [0, 0, 0, 0, 8, 0, 0, 7, 9],
                   ]
    print_sudoku(sudoku_grid)
    solution = solve_sudoku(sudoku_grid)
    print_sudoku(solution)


if __name__ == '__main__':
    main()
