import numpy as np
np.random.seed(21)
# This guarantees the code will generate the same
#set of random numbers whenever executed
random_integers = np.random.randint(1,high=500000, size=(20, 5))
random_integers
