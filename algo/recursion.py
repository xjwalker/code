def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


def agg_nums(numbers: list):
    if len(numbers) == 1:
        return numbers[0]

    current_num = numbers.pop()

    return current_num + agg_nums(numbers)


def find_max_num(numbers: list, max_n=-1):
    if len(numbers) == 1:
        return max_n if max_n > numbers[0] else numbers[0]

    current_num = numbers.pop()

    if current_num > max_n:
        return find_max_num(numbers, current_num)

    return find_max_num(numbers, max_n)


def find_max_num_chatgpt(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        max_value = find_max_num_chatgpt(nums[1:])
        return max_value if max_value > nums[0] else nums[0]


def reverse_string(word: str):
    if len(word) == 1:
        return word[0]
    letter = word[-1]

    return letter + reverse_string(word[:len(word) - 1])


def find_minimum_common_divisor(n, m, mcd=2):
    """
    Find the greatest common divisor of two numbers: Write a function that takes two positive integers as input and
    returns their greatest common divisor using recursion.
    """
    if n >= m and n % m != 0:
        return -1

    if n >= m and mcd == m:
        return m
    if m >= n and mcd == n:
        return n
    #
    # if n % mcd == 0 and m % mcd == 0:
    #     return mcd

    return find_minimum_common_divisor(n, m, mcd + 1)


def gcd_chatpgt(a, b):
    if b == 0:
        return a
    else:
        return gcd_chatpgt(b, a % b)


def count_occurrences(word, char, count=0):
    if len(word) == 1 and word[0] == char:
        count += 1
        return count
    elif len(word) == 1:
        return count

    letter = word[0]
    if letter == char:
        count += 1

    return count_occurrences(word[1:], char, count)


def is_palindrome(word: str):
    if len(word) == 0:
        return True
    if len(word) == 1:
        return True

    if word[0] != word[-1]:
        return False

    return is_palindrome(word[1:len(word) - 1])


# def make_combinations(numbers: list): #[1, 2, 3, 4]
#

def binary_search(numbers, search_value, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if numbers[mid] == search_value:
        return mid

    if numbers[mid] > search_value:
        return binary_search(numbers, search_value, left, mid - 1)
    else:
        return binary_search(numbers, search_value, mid + 1, right)


def binary_search_recursive_chatgpt(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_recursive_chatgpt(arr, low, mid - 1, key)
        else:
            return binary_search_recursive_chatgpt(arr, mid + 1, high, key)
    else:
        return -1


def recursive_multiplication(n, m):
    if m == 1:
        return n

    return n + recursive_multiplication(n, m - 1)


def main():
    print('factorial num:')
    print(factorial(5))

    print('sum numbers')
    print(agg_nums([1, 2, 3, 4, 5]))

    print('find maximum value')
    print(find_max_num([1, 2900, 300, 4, 5, 234100]))

    print('reverse string')
    print(reverse_string("?satse omoc aloh"))

    print('minimum common divisor')
    print(find_minimum_common_divisor(18, 24))

    print("count occurrences")
    print(count_occurrences("abecedarioaa", "a"))

    print('is palindrome')
    print(is_palindrome("racecar"))

    print('binary search')
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(binary_search(arr, 5, 0, len(arr)))

    print(binary_search_recursive_chatgpt(arr, 0, len(arr), 5))

    print('recursive multiplication')
    print(recursive_multiplication(8, 4))


if __name__ == '__main__':
    main()
