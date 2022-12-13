input_logs_simple = [
    {
        'start': 0,
        'end': 5,
        'batch_size': 5
    }, {
        'start': 4,
        'end': 7,
        'batch_size': 3
    }, {
        'start': 6,
        'end': 13,
        'batch_size': 11
    }, {
        'start': 8,
        'end': 13,
        'batch_size': 10
    }
]

#
# |--- 5 ---|
#	     |----- 3 -----|
#	     			|------ 11 -------|
#					     |---- 10 ----|

input_logs = [
    {
        'start': 0,
        'end': 5,
        'batch_size': 5
    }, {
        'start': 4,
        'end': 7,
        'batch_size': 3
    }, {
        'start': 6,
        'end': 13,
        'batch_size': 11
    }, {
        'start': 0,
        'end': 3,
        'batch_size': 10
    }, {
        'start': 6,
        'end': 10,
        'batch_size': 10
    }
]


# |--- 5 ---|
#	     |----- 3 -----|
#	     			|------ 11 -------|
# |- 10 -|
#					|----- 10 ----|

def find_peak_looping(logs):
    peak = -1
    for i in range(len(logs)):
        for j in range(i + 1, len(logs)):
            if logs[i]['start'] <= logs[j]['start'] <= logs[i]['end']:
                agg = logs[j]['batch_size'] + logs[i]['batch_size']
                peak = agg if agg > peak else peak

    return peak


def find_peak_final(logs):
    peak = -1
    for i in range(len(logs)):
        agg = logs[i]['batch_size']
        for j in range(len(logs)):
            if i == j:
                continue
            if logs[i]['start'] <= logs[j]['start'] <= logs[i]['end']:
                agg += logs[j]['batch_size']
                peak = agg if agg > peak else peak

    return peak


if __name__ == '__main__':
    result = find_peak_final(input_logs)

    print(result)
