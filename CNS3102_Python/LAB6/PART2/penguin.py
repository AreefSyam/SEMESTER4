import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Set the display width
pd.set_option("display.width", 1000)

# Step 2: Load the dataset
salary_data = pd.read_csv('D:\VISUAL STUDIO CODE\PYTHON\CNS3102_Python\LAB6\penguins_size.csv')

# Step 3: Explore the dataset
# Check for null values in each column
print(salary_data.isnull().sum())

'''
You can see the number of null values in each column of the salary_data DataFrame.
This can be useful for identifying columns with missing data that may need to
be handled or cleaned before further analysis or modeling.
'''

# Drop the rows with missing values
salary_data.dropna(inplace=True)

# Split the data into features and target
X = salary_data.iloc[:, :-1]  # Selects all the rows and all columns except the last column from the salary_data
y = salary_data.iloc[:, -1]  # Selects all the rows and the last column from the salary_data DataFrame
'''
Features (X): This includes all the columns of the dataset except the last column.
These columns represent the input variables or characteristics that we will use to make predictions.
Target variable (y): This corresponds to the last column of the dataset.
It represents the variable we want to predict or estimate using the input features.
'''

# Encode categorical variables using one-hot encoding
X_encoded = pd.get_dummies(X)
'''
One-hot encoding is a process of converting categorical variables into a
numerical representation that can be used for machine learning algorithms.
It takes the feature data (X) as input and returns a new DataFrame (X_encoded)
where categorical variables are replaced with their corresponding binary columns.
'''

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
'''
1) By splitting the data into training and testing sets, we can train our machine learning models on
   the training data and evaluate their performance on the testing data.
2) The test_size parameter is set to 0.2, indicating that 20% of the data will be allocated for testing,
   while the remaining 80% will be used for training.
3) The random_state parameter is used to control the randomization process,
   allowing you to obtain consistent results when you set it to the same value.
'''

# Create a list to store accuracy and time measurements
classifiers = ['K-NN']
accuracy_scores = []
training_times = []
testing_times = []

# Define a function to measure time taken for training and testing
def measure_time(classifier, X_train, y_train, X_test):
    # Training
    start_train = time.time()
    classifier.fit(X_train, y_train)
    end_train = time.time()
    train_time = end_train - start_train
    
    # Testing
    start_test = time.time()
    classifier.predict(X_test)
    end_test = time.time()
    test_time = end_test - start_test
    
    return train_time, test_time

# Create and train the classifiers

# K-Nearest Neighbors Classifier
knn_classifier = KNeighborsClassifier()
knn_train_time, knn_test_time = measure_time(knn_classifier, X_train, y_train, X_test)
knn_predictions = knn_classifier.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_predictions)
accuracy_scores.append(knn_accuracy)
training_times.append(knn_train_time)
testing_times.append(knn_test_time)

# Create a comparison table
data = {'Classifier': classifiers, 'Accuracy': accuracy_scores, 'Training Time': training_times, 'Testing Time': testing_times}
comparison_df = pd.DataFrame(data)
print(comparison_df)

# Create comparison graphs
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Bar chart for accuracy comparison
colors = ['green']  # Specify the colors for the bars
axs[0].bar(classifiers, accuracy_scores, color=colors)  # Set the color parameter
axs[0].set_xlabel('Classifier')
axs[0].set_ylabel('Accuracy')
axs[0].set_title('Accuracy Comparison')

# Bar chart for training and testing time comparison
bar_width = 0.3
index = np.arange(len(classifiers))

axs[1].bar(index, training_times, bar_width, label='Training Time')
axs[1].bar(index + bar_width, testing_times, bar_width, label='Testing Time')
axs[1].set_xlabel('Classifier')
axs[1].set_ylabel('Time (seconds)')
axs[1].set_title('Training and Testing Time Comparison')
axs[1].set_xticks(index + bar_width / 2)
axs[1].set_xticklabels(classifiers)
axs[1].legend()

plt.tight_layout()
plt.show()
