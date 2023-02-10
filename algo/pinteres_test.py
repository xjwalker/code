# height, number of columns returns a grid layout
# next pin in shortest column so far
# if there's a tie place it in the leftmost column
# list per column


from heapq import heappush as push, heappop as pop


def get_columns(pins, k):
    columns = [[] for _ in range(k)]
    columns_heap = [[0, i] for i in range(0, k)]
    columns_grid = [[] for _ in range(k)]
    for pin in pins:
        height, col = pop(columns_heap)
        columns[col].append(pin["id"])
        # push(columns_heap, [height + 1, col])
        push(columns_heap, [height + pin["height"], col])
        columns_grid[col].append(pin)
    return columns_grid, columns_heap


def model_pins(pins, n_columns):
    agg_pins = {}
    grid_layout = []
    for i in range(n_columns):
        grid_layout.append([])
        agg_pins[i] = 0

    for i in range(n_columns):  # fill first row for all columns
        agg_pins[i] += pins[i]['height']
        grid_layout[i] = [pins[i]]

    for i in range(n_columns, len(pins)):
        lowest_height_val = float('Inf')
        aux_index = -1
        for index in range(len(agg_pins)):  # find the column index with lowest height
            if agg_pins[index] < lowest_height_val:  # this covers the most left index in case of a tie
                lowest_height_val = agg_pins[index]
                aux_index = index

        agg_pins[aux_index] += pins[i]['height']
        grid_layout[aux_index].append(pins[i])

    return grid_layout, agg_pins


def main():
    pins = [
        {"id": 1, "height": 300},
        {"id": 2, "height": 200},
        {"id": 3, "height": 250},
        {"id": 4, "height": 350},
        {"id": 5, "height": 100},
    ]
    n_columns = 2

    expected_result = [
        [
            {"id": 1, "height": 300},
            {"id": 4, "height": 350},
        ],
        [
            {"id": 2, "height": 200},
            {"id": 3, "height": 250},
            {"id": 5, "height": 100},
        ]
    ]

    result = model_pins(pins, n_columns)
    # assert result == expected_result
    print('1: ', result)
    print('2: ', get_columns(pins, 2))

    pins = [
        {"id": 0, "height": 10},
        {"id": 1, "height": 5},
        {"id": 2, "height": 12},
        {"id": 3, "height": 31},
        {"id": 4, "height": 23},
        {"id": 5, "height": 8},
        {"id": 6, "height": 21},
        {"id": 7, "height": 99},
        {"id": 8, "height": 1}
    ]
    result = model_pins(pins, 4)
    print('1: ', result)
    print('2: ', get_columns(pins, 4))


if __name__ == '__main__':
    main()
