import numpy as np

print('array shape')
arr = np.array([[1, 2, 3, 4], [5, 6, 7,8]])
print(arr.shape)


print('array reshape')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

print('array reshape with two dimensions')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

print("array base")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)


print("Convert 1D array with 8 elements to 3D array with 2x2 elements:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

print("Convert the array into a 1D array:")
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)