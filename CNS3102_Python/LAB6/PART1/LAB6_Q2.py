# Python program to explain os.mkdir() method

# importing os module
import os

# Directory
directory = "GeeksforGeeks2"

# Parent Directory path (Make sure is a parent folder)
parent_dir = "/workspaces/Python-Sem4/PYTHON/CNS3102/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks2' folder in CNS3102 folder
os.mkdir(path) # make a new folder
print("Directory '% s' created" % directory)
