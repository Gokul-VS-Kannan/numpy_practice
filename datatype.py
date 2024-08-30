import numpy as np 

arr1 = np.array(["a","b","c","d"])
print(arr1)
print(arr1.dtype)

arr2 = np.array([1,2,3,4,5])
print(arr2)
print(arr2.dtype)  # op:int64

# chainging data type by assigning the data type while creating the array

arr3 = np.array([1,2,3,4,5],dtype=np.int16)
print(arr3)
print(arr3.dtype)  # op : int16

# converting data types of array
arr4 = arr3.astype(np.float16)
print(arr4,arr4.dtype)