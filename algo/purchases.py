def print_matrix(matrix):
    res = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            res += f'[{matrix[i][j]}] '
        res += '\n'
    print(res)


def best_purchase(items, budget):
    aux_max_area = -1
    temp_t =[]
    for i in range(len(items)):
        for j in range(len(items)):
            temp_line = []
            for width in range(1, len(items) - i):
                for height in range(1, len(items) - j):
                    # items, x, y, width height.
                    items_cost = 0
                    for aux_i in range(i, width):
                        for aux_j in range(j, height):
                            items_cost += items[aux_i][aux_j]
                            temp_line.append(items[aux_i][aux_j])
                    if budget >= items_cost:
                        aux_max_area = width * height
            temp_t.append(temp_line)

    print(temp_t)
    return aux_max_area


def max_rectangular_area(matrix, budget):
    n = len(matrix)
    m = len(matrix[0])
    # Compute the cumulative sum of the matrix
    cum_sum = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            cum_sum[i][j] = cum_sum[i-1][j] + cum_sum[i][j-1] - cum_sum[i-1][j-1] + matrix[i-1][j-1]
    max_area = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(i, n+1):
                for l in range(j, m+1):
                    # Compute the sum of the submatrix using cumulative sum
                    current_sum = cum_sum[k][l] - cum_sum[k][j-1] - cum_sum[i-1][l] + cum_sum[i-1][j-1]
                    if current_sum <= budget:
                        area = (k-i+1) * (l-j+1)
                        max_area = max(max_area, area)
    return max_area

def max_items(matrix, budget):
    n = len(matrix)
    max_items = 0
    cumulative_sums = [[0] * n for _ in range(n)]  # this creates a nxn empty matrix

    # Calculate cumulative sums for sub matrices
    for i in range(n):
        for j in range(n):
            cumulative_sums[i][j] = matrix[i][j]
            if i > 0:
                cumulative_sums[i][j] += cumulative_sums[i - 1][j]
            if j > 0:
                cumulative_sums[i][j] += cumulative_sums[i][j - 1]
            if i > 0 and j > 0:
                cumulative_sums[i][j] -= cumulative_sums[i - 1][j - 1]
    print(cumulative_sums)
    # Iterate over all possible pairs of top and bottom rows
    for i in range(n):
        for j in range(n):
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
    res = best_purchase(list_items, budget)
    print('new copy ', res)

    res = max_items(list_items, budget)
    print(res)

    list_items = [
        [90, 90, 100],
        [90, 120, 42],
        [10, 10, 42],
    ]
    list_items = [
        [401, 401, 401],
        [401, 200, 200],
        [401, 401, 401],
    ]
    budget = 400
    res = max_items_2(list_items, budget)  # <- wrong function
    print(res)

    res = max_rectangular_area(list_items, budget)
    print('-------', res)

    list_items = [
        [90, 90, 100],  # -> 280 - 3
        [90, 120, 42],  # 220 - 3
        [10, 10, 42],  # 184 - 3
    ]  # 330 - 6 | 190 - 3
    list_items = [
        [401, 401, 401],
        [401, 200, 200],
        [401, 401, 401],
    ]
    budget = 400
    res = max_items_3(list_items, budget)
    print(res)


if __name__ == '__main__':
    main()
