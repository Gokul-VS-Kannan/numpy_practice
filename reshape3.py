import numpy as np

arr1 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

# convert 3d array to 2d array
arr_2d = arr1.reshape(4,2)
print(arr_2d)

new_2d = arr1.reshape(2,4)
print(new_2d)

#  convert 3d to 1d
arr_1d = arr1.reshape(8)
print(arr_1d)