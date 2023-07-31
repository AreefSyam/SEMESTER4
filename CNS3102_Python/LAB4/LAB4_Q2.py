import numpy as np

np.random.seed(21)
# This guarantees the code will generate the same

#set of random numbers whenever executed
random_integers = np.random.randint(1,high=500000, size=(20, 5))

print(random_integers)

avg = np.mean(random_integers[:, 1], axis=0) #second coloumn, all row

print(f"\nThe average value for coloumn 2 : {avg:.2f}") #two decimal places