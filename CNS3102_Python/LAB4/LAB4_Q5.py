import numpy as np

my_vector = np.array([1, 2, 3, 4, 5, 6])
selection = my_vector % 2 == 0
my_vector[selection]