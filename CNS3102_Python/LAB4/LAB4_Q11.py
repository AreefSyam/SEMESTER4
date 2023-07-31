import numpy as np

#[18]
my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array)

#[19]
my_slice = my_array[:, 1:3].copy()
print(my_slice)

my_array[:, :] = my_array * 2
print("\n",my_array)
print(my_slice)

#[20]: true
my_array = np.array([1, 2, 3])
my_slice = my_array[1:3]
print("\n",my_slice.base is my_array)

#[21]: false
my_array = np.array([1, 2, 3])
my_array = my_array[1:4]
my_slice = my_array[1:3]
print(my_slice.base is my_array)

#[22]:
print(my_slice)

#[23]:
print(my_array)

#[24]:
# But a change to `my_slice` still impacts `my_array`.
my_slice[0] = -1
print("But a change to `my_slice` still impacts `my_array`:",my_array)

#[25]:
my_slice.base is my_array.base