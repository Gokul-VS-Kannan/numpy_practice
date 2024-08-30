import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1.shape)

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2.shape)

arr3 = np.array([
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
])

print(arr3)
print(arr3.shape)

arr4 = np.array([
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
])

print(arr4.shape)