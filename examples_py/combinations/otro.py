def subset_sum(numbers, target, partial=[], min_possibles=set()):
    agg = check_permutation(partial)
    print('partial solution', partial, ' agg: ', agg, ' partial ', partial)
    # agg = sum(partial)
    if agg > target:
        return

    if agg == target:
        min_possibles.add(len(partial))

    #todo;  plantear esta madre en notacion matematica
    print(len(numbers), '<--- registro de numeros')
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]

        subset_sum(remaining, target, partial + [n], min_possibles)

    return min(min_possibles)


def check_permutation(numbers):
    agg = 0
    for num in numbers:
        agg += num

    return agg


if __name__ == "__main__":
    result = subset_sum([3, 3, 9, 8, 4, 5, 7, 10], 15) # combination excluyente
    print('result:', result)

# bfs  dfs
