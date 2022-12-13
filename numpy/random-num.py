from numpy import random

x = random.randint(100)
print(x)

x = random.rand()

print(x)

x=random.randint(100, size=(5))

print(x)

x = random.randint(100, size=(3, 5))

print(x)

x = random.rand(5)

print(x)

x = random.rand(3, 5)

print(x)

x = random.choice([3, 5, 7, 9])

print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

print('distribution')

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)
print('permutation')
arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
print(random.permutation(arr))
print(random.permutation(arr))