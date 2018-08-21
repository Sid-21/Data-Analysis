import numpy as np


# FOR CREATING ARRAYS, WE NEED TO MAKE LISTS. -- One way
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print(my_array1)

# CREATING MULTI-DIMENSIONAL ARRAYS
my_list2 = [11,22,33,44]
my_lists = [my_list1, my_list2]
my_array2= np.array(my_lists)
print(my_array2)

# CHECKING SHAPE OF ARRAY
my_array2.shape

# CHECKING THE TYPE
my_array2.dtype

# SPECIAL CASE ARRAYS
np.zeros()
np.empty()
np.ones()

# ARRANGING ARRAYS IN SPECIFIC ORDER LIKE FROM 0 TO 11
np.arange(5,50,4)

# ARITHIMATIC OPERATIONS
arr1 = np.array([[1,2,3,4],[11,22,33,44]])
print(arr1 - arr1)
print(arr1 * arr1)
print(1 / arr1)

