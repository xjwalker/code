def print_matrix(matrix):
    res = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            res += f'[{matrix[i][j]}] '
        res += '\n'
    print(res)


def best_purchase(items, budget):
    # list of combinations:
    # (0, 0), (0, 1), (0,2) # 280
    # (0, 0), (0, 1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2) #
    size = len(items)
    columns = []
    vertical_list = []
    horizontal_list = []
    smaller_lists = []
    full_list_price = 0

    for i in range(size):
        vertical_list = []
        horizontal_list = []
        vertical_index = 0
        horizontal_index = i
        for j in range(size):
            full_list_price += items[i][j]

            horizontal_list.append(items[i][j])
            vertical_list.append(items[vertical_index][horizontal_index])
            vertical_index += 1

        columns.append(vertical_list)
        columns.append(horizontal_list)

    if budget == full_list_price:
        return size * size

    print(columns)


def max_items(matrix, budget):
    n = len(matrix)
    max_items = 0
    cumulative_sums = [[0] * n for _ in range(n)]

    # Calculate cumulative sums for submatrices
    for i in range(n):
        for j in range(n):
            cumulative_sums[i][j] = matrix[i][j]
            if i > 0:
                cumulative_sums[i][j] += cumulative_sums[i - 1][j]
            if j > 0:
                cumulative_sums[i][j] += cumulative_sums[i][j - 1]
            if i > 0 and j > 0:
                cumulative_sums[i][j] -= cumulative_sums[i - 1][j - 1]

    # Iterate over all possible pairs of top and bottom rows
    for i in range(n):
        for j in range(i, n):
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                current_sum = cumulative_sums[j][mid]
                if i > 0:
                    current_sum -= cumulative_sums[i - 1][mid]
                if current_sum <= budget:
                    max_items = max(max_items, (j - i + 1) * (mid + 1))
                    left = mid + 1
                else:
                    right = mid - 1

    return max_items


def max_items_2(matrix, budget):
    n = len(matrix)
    max_items = 0

    # Calculate the prefix sums for each row of the matrix
    prefix_sums = [[0] * (n + 1) for _ in range(n)]
    for i in range(n):
        for j in range(1, n + 1):
            prefix_sums[i][j] = prefix_sums[i][j - 1] + matrix[i][j - 1]

    # Iterate over all possible combinations of rows and columns
    for i in range(n):
        for j in range(i, n):
            for k in range(n):
                l = k
                current_sum = 0
                # Calculate the sum of the submatrix
                while l < n and current_sum + prefix_sums[j][l + 1] - prefix_sums[i][l + 1] + prefix_sums[i][k] - \
                        prefix_sums[j][k] <= budget:
                    current_sum += prefix_sums[j][l + 1] - prefix_sums[i][l + 1] + prefix_sums[i][k] - prefix_sums[j][k]
                    l += 1
                # Update the maximum number of items
                max_items = max(max_items, (j - i + 1) * (l - k))

    return max_items


def max_items_3(matrix, budget):
    n = len(matrix)
    max_items = 0
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(n):
                if i == j:
                    current_sum = matrix[i][k]
                else:
                    current_sum += sum(matrix[x][k] for x in range(i, j + 1))
                if current_sum > budget:
                    break
                max_items = max(max_items, (j - i + 1) * (k + 1))
    return max_items


def generate_rectangles(items_list):
    size = len(items_list) - 1
    aux_list = []
    j = 0
    for i in range(size):
        aux_list.append(items_list[i][i])


def main():
    list_items = [
        [90, 90, 100],  # -> 280 - 3
        [90, 120, 42],  # 220 - 3
        [10, 10, 42],  # 184 - 3
    ]  # 330 - 6 | 190 - 3
    budget = 400
    print_matrix(list_items)
    best_purchase(list_items, budget)

    res = max_items(list_items, budget)
    print(res)

    list_items = [
        [90, 90, 100],  # -> 280 - 3
        [90, 120, 42],  # 220 - 3
        [10, 10, 42],  # 184 - 3
    ]  # 330 - 6 | 190 - 3
    budget = 400
    res = max_items_2(list_items, budget)
    print(res)
    list_items = [
        [90, 90, 100],  # -> 280 - 3
        [90, 120, 42],  # 220 - 3
        [10, 10, 42],  # 184 - 3
    ]  # 330 - 6 | 190 - 3
    budget = 400
    res = max_items_3(list_items, budget)
    print(res)


if __name__ == '__main__':
    main()
