import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])

#  convert 2d t0 1d
arr_1d = arr1.reshape(6)
print(arr_1d)

# convert 2d to 2d inter chainging row and colum
arr_2d = arr1.reshape(3,2)
print(arr_2d)

#  convert 2d to 3d
arr_3d = arr1.reshape(2,1,3)
print(arr_3d)
new_3d = arr1.reshape(3,1,2)
print(new_3d)