def compress_values(values):
    values_dict = {}
    for val in values:
        if val not in values_dict:
            values_dict[val] = 1
        else:
            values_dict[val] += 1

    res = ''
    arr = []
    for index, val in values_dict.items():
        res += f"{index}{val}"
        arr.append(res)

    return len(res), res


if __name__ == '__main__':
    values = ["a", "a", "b", "b", "c", "c", "c"]
    print(compress_values(values))
