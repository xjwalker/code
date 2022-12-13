import numpy as np

p1 = [1,2,3,4,5]
p2 = [6,7,8,9,10]

array = [p1, p2]

arr = np.array(array)

print('5th element on 2nd row: ', arr[1, 4])



arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:6])



arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:3, 1:4])