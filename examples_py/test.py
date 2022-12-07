#!/bin/python3

def run():
    matrix = [
        ['T', 's', 'i'],
        ['h', '%', 'x'],
        ['i', ' ', '#'],
        ['s', 'M', ' '],
        ['$', 'a', ' '],
        ['#', 't', '%'],
        ['i', 'r', '!'],
    ]

    message = ''
    columns = len(matrix)
    rows = len(matrix[0])

    for col in range(rows):
        print(col)
        for row in range(columns):
            message += matrix[col][row]
            # flag = True
            # while row.isalnum() and flag:
            #     message += row
            #     flag = False

    print(message)

run()
