import numpy as np

np.random.seed(21)
# This guarantees the code will generate the same

#set of random numbers whenever executed
random_integers = np.random.randint(1,high=500000, size=(20, 5))

print(random_integers)

avg = np.mean(random_integers[:5, 2:4], axis=0) #second coloumn, all row

print(f"\nAverage of the first 5 rows of the third and fourth columns: {avg}")