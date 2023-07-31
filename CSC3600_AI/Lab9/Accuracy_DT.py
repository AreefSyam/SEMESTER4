import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('D:\VISUAL STUDIO CODE\PYTHON\CSC3600_AI\Lab9\WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Drop the rows with missing values
data.dropna(inplace=True)

# Split the data into features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Encode categorical variables using one-hot encoding
X_encoded = pd.get_dummies(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Create an instance of the Decision Tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

# Plot the accuracy
plt.bar(['Accuracy'], [accuracy])
plt.ylim(0, 1)
plt.ylabel('Accuracy')
plt.title('Decision Tree Accuracy')
plt.show()

print("Accuracy:", accuracy)
