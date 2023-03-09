"""
since
a=1, b=2, c=3, d=4 .... w=23 x=24 y=25 z=26
given a string containing only numbers
return all the combinations inside the string that are valid letters'
ex: input "1123"
generates: [1,1,2,3], [11, 2, 3], [1, 12, 3], [1, 1, 23], [11, 23]
return value: [aabc, kbc, ajc, aaw, kw]
"""


def find_valid_combinations(digits):
    """
    We start by calling find_combinations with an empty list for the current argument and an
    empty list for the results argument. At each step, we check if there are any digits left in the digits string.
    If not, we have found a valid combination and append it to the results list. Otherwise,
    we try appending the next 1 or 2 digits to the current list, depending on whether they form a number less than 26.
    We then recursively call find_combinations with the remaining digits and the updated current list.
    When the recursion returns, we backtrack to the previous step and try the next possible combination.

    For the input string "1123", the find_valid_combinations function would return the
    list [[1, 1, 2, 3], [1, 12, 3], [11, 2, 3], [11, 23], [1, 1, 23]], which includes
    all valid combinations of digits less than 26.
    :param digits:
    :return: []
    """
    results = []
    find_combinations(digits, [], results)
    return results


def find_combinations(digits, current, results):
    if len(digits) == 0:
        results.append(current)
    else:
        # Try a single-digit number
        digit = int(digits[0])
        if digit > 0:
            find_combinations(digits[1:], current + [digit], results)

        # Try a two-digit number if possible
        if len(digits) >= 2:
            number = int(digits[:2])
            if number < 26:
                find_combinations(digits[2:], current + [number], results)


def main():
    print(find_valid_combinations("1123"))


if __name__ == '__main__':
    main()
