#create 1d array from 0 to 9 and reshape it into 2x5 matrix

import numpy as np

x = [0,1,2,3,4,5,6,7,8,9]
arr = np.array(x)
print(arr)

# reshaping
re_arr = arr.reshape(2,5)
print("reshaped array is :")
print(re_arr)
