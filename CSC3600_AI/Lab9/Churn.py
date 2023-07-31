import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
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

# Create an instance of the Decision Tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier to the data
clf.fit(X_encoded, y)

# Get the index of the last tree in the decision path
last_tree_index = clf.tree_.node_count - 1

# Plot the decision tree for the last output only with larger font size
plt.figure(figsize=(15, 8))
plot_tree(clf, feature_names=X_encoded.columns, class_names=['No Churn', 'Churn'], filled=True, node_ids=True, max_depth=3,
          impurity=False, rounded=True, precision=2, fontsize=5)
plt.show()
