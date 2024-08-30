import numpy as np
lst1 = [1,2,3,4,5]
arr1 = np.array(lst1)
print(arr1)

tup1 = (10,20,30,40,50)
arr12 = np.array(tup1)
print(arr12)

arr2 = np.zeros(5)
print(arr2)
arr2_2d = np.zeros((3,3))
print(arr2_2d)
arr2_3d = np.zeros((2,3,3))
print(arr2_3d)
# zeros method create an array of zero, ones method create array of one
arr3 = np.ones(5)
print(arr3)

arr4 = np.arange(11) #mentioning only stoping index
print(arr4)

arr4_1 = np.arange(10,21)  # mentioning both starting and stoping index
print(arr4_1)

arr4_2 = np.arange(10,101,5) # mentioning starting index,stoping index and step value
print(arr4_2)

# we can use floting values in arange () method
