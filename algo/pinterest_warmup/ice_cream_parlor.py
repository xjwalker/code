"""
Two friends like to pool their money and go to the ice cream parlor.
They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example. m = 6 arr = [1, 2, 3, 4, 5]

The two flavors that cost 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.

Function Description

Complete the icecreamParlor function in the editor below.

icecreamParlor has the following parameter(s):

int m: the amount of money they have to spend
int cost[n]: the cost of each flavor of ice cream
Returns

int[2]: the indices of the prices of the two flavors they buy, sorted ascending
Input Format

The first line contains an integer, , the number of trips to the ice cream parlor.
The next  sets of lines each describe a visit.

Each trip is described as follows:

1. The integer m, the amount of money they have pooled.
2. The integer n, the number of flavors offered at the time.
3. n space-separated integers denoting the cost of each flavor: cost[cost[1], cost[2], ..., cost[n]].
Note: The index within the cost array represents the flavor of the ice cream purchased.

Sample Input

STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]
Sample Output

1 4
1 2
Explanation

Sunny and Johnny make the following two trips to the parlor:

The first time, they pool together  dollars. Of the five flavors available that day, flavors  and  have a total cost of .
The second time, they pool together  dollars. Of the four flavors available that day, flavors  and  have a total cost of .

"""


def ice_cream_parlor(m, arr):
    costs = {}
    for index, cost in enumerate(arr):
        if m - cost in costs:
            return [costs[m - cost], index + 1]
        costs[cost] = index + 1


def ice_cream_parlor_cheat(m, arr):
    d = dict()
    for idx, price in enumerate(arr):
        if m - price in d:
            return [d[m - price], idx + 1]
        d[price] = idx + 1


def main():
    arr = [1, 4, 5, 3, 2]
    res = ice_cream_parlor(4, arr)
    assert res == [1, 4]

    arr = [2, 2, 4, 3]
    res = ice_cream_parlor(4, arr)

    assert res == [1, 2]

    arr = [1, 3, 4, 6, 7, 9]
    res = ice_cream_parlor(9, arr)
    assert res == [2, 4]

    arr = [1, 3, 4, 6, 7, 9]
    res = ice_cream_parlor(9, arr)
    assert res == [2, 4]


if __name__ == '__main__':
    main()
