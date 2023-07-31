#[4]
import numpy as np
my_array = np.array([1, 2, 3, 4])
print(my_array)

#[5]
my_slice = my_array[1:3]
print(my_slice)

#[6]
my_slice[0] = -1
print(my_slice)

#[7]
print(my_array)

#[8]
print(my_array[1])

#[9]
x = [1, 2, 3]
y = x[0:2]
print(y)
y[0] = "a change"
print(y)

#[10]
print(x)

#[11]
my_array = np.array([1, 2, 3])
my_slice = my_array[1:3]
print(my_slice)
my_slice[0] = -1
print(my_array)

#[12]
my_array = np.array([1, 2, 3])
my_slice = my_array[[1,2]]
my_slice[0] = -1
print("Yg ke 12:",my_array)

#[13]
my_array = np.array([1, 2, 3])
my_slice = my_array[1:3]
print(my_slice)
my_slice = my_slice * 2
print("Yg ke 13:", my_slice)

#[14]
print("Yg ke 14:",my_array)

#[15]
my_array = np.array([1, 2, 3])
my_slice = my_array[1:3]
#the view remains a view if you edit it by modifying it using basic indexing
#(i.e. you use ``[]`` on the left side of the assignment operator
my_slice[:] = my_slice * 2
print("Yg ke 15:",my_slice)

#[16]
print("Yg ke 16:",my_array)