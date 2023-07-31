import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load the dataset
penguin_data = pd.read_csv('D:\VISUAL STUDIO CODE\PYTHON\CNS3102_Python\LAB6\penguins_size.csv')

# Remove rows with missing values
penguin_data = penguin_data.dropna()

# Convert categorical columns to numeric representations using one-hot encoding
penguin_data = pd.get_dummies(penguin_data, columns=['species', 'island', 'sex'])

# Split the penguin_data DataFrame into input features (X) and target variable (y)
# X contains all the columns except 'species_Adelie', while y contains only the 'species_Adelie' column
X = penguin_data.drop('species_Adelie', axis=1)  # Input features
y = penguin_data['species_Adelie']  # Target variable

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define range of number of neighbors
no_neighbors = np.arange(1, 9)

# Empty arrays to store accuracy values
train_accuracy = np.empty(len(no_neighbors))
test_accuracy = np.empty(len(no_neighbors))

# Loop over number of neighbors
for i, k in enumerate(no_neighbors):
    # Create a KNN classifier with current number of neighbors
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)

    # Store accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    # Store accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Plot the results
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(no_neighbors, test_accuracy, label='Testing Accuracy')
plt.plot(no_neighbors, train_accuracy, label='Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.show()
