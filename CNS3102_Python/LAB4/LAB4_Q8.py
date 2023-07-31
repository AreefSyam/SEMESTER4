import numpy as np
my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array)
my_array[:, :] = my_array * 2
print("\n",my_array)