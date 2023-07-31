import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# Set the display width
pd.set_option("display.width", 1000)

# Step 2: Load the dataset
# from google.colab import files
# uploaded = files.upload()

# Step 3: Explore the dataset
salary_data = pd.read_csv('D:\VISUAL STUDIO CODE\PYTHON\CNS3102_Python\Project\Real_Project\RICE.csv')
print(salary_data.shape)
print(salary_data)
print(salary_data.isnull().sum())

# Drop the rows with missing values
salary_data.dropna(inplace=True)

# Split the data into features and target
X = salary_data.iloc[:, :-1]
y = salary_data.iloc[:, -1]
print(y)

# Encode categorical variables using one-hot encoding
X_encoded = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Create a list to store accuracy and time measurements
classifiers = ['RF', 'K-NN', 'Logistic Regression']
accuracy_scores = []
training_times = []
testing_times = []

# Define a function to measure time taken for training and testing
def measure_time(classifier, X_train, y_train, X_test):
    start_train = time.time()
    classifier.fit(X_train, y_train)
    end_train = time.time()
    train_time = end_train - start_train
    
    start_test = time.time()
    classifier.predict(X_test)
    end_test = time.time()
    test_time = end_test - start_test
    
    return train_time, test_time

# Create and train the classifiers

# Random Forest Classifier
rf_classifier = RandomForestClassifier()
rf_train_time, rf_test_time = measure_time(rf_classifier, X_train, y_train, X_test)
rf_predictions = rf_classifier.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
accuracy_scores.append(rf_accuracy)
training_times.append(rf_train_time)
testing_times.append(rf_test_time)

# K-Nearest Neighbors Classifier
knn_classifier = KNeighborsClassifier()
knn_train_time, knn_test_time = measure_time(knn_classifier, X_train, y_train, X_test)
knn_predictions = knn_classifier.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_predictions)
accuracy_scores.append(knn_accuracy)
training_times.append(knn_train_time)
testing_times.append(knn_test_time)

# Logistic Regression Classifier
lr_classifier = LogisticRegression(max_iter=1000)  # Increase max_iter
lr_train_time, lr_test_time = measure_time(lr_classifier, X_train, y_train, X_test)
lr_predictions = lr_classifier.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_predictions)
accuracy_scores.append(lr_accuracy)
training_times.append(lr_train_time)
testing_times.append(lr_test_time)

# Create a comparison table
data = {'Classifier': classifiers, 'Accuracy': accuracy_scores, 'Training Time': training_times, 'Testing Time': testing_times}
comparison_df = pd.DataFrame(data)
print(comparison_df)

# Create comparison graphs
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Bar chart for accuracy comparison
colors = ['blue', 'green', 'red']  # Specify the colors for the bars
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