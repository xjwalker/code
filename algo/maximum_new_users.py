def frequency_max_new_users(numbers: list, queries: list) -> list:
    final_res = []

    for query in queries:
        current_max = -1
        frequency = 0
        for i in range(query - 1, len(numbers)):
            if current_max < numbers[i]:
                current_max = numbers[i]
                frequency = 1
            elif numbers[i] == current_max:
                frequency += 1
        final_res.append(frequency)
    return final_res


def main():
    numbers = [2, 1, 2]
    queries = [1, 2, 3]
    expected_value = [2, 1, 1]
    result = frequency_max_new_users(numbers, queries)
    assert expected_value == result
    

if __name__ == '__main__':
    main()
    import cProfile

    cProfile.run('main()')
