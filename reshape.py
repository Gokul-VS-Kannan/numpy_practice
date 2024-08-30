import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9])
#  1 D to 2 D
arr_2d = arr1.reshape(3,3)
print(arr_2d)
# 1 dD to 3 d
arr_3d = arr1.reshape(1,1,9)
print(arr_3d)
new_3d = arr1.reshape(1,3,3)
print(new_3d)