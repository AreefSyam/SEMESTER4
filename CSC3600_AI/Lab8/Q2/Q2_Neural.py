import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from tensorflow import keras

# Step 1: Load the datasets
train_data = pd.read_csv(r'D:\VISUAL STUDIO CODE\PYTHON\CSC3600_AI\Lab8\Q2\train.csv')
test_data = pd.read_csv(r'D:\VISUAL STUDIO CODE\PYTHON\CSC3600_AI\Lab8\Q2\test.csv')

# Step 2: Preprocess the data
# Separate the features and target variable in the training dataset
X_train = train_data.iloc[:, :-1].values
y_train = train_data.iloc[:, -1].values

# Separate the features in the testing dataset
X_test = test_data.iloc[:, :-1].values

# Scale the features using standardization (optional)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 3: Build and train the neural network model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(4, activation='softmax')
])

# Compile the model with an appropriate optimizer, loss function, and metrics
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model using the training data
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Step 4: Evaluate the model
# Make predictions on the test set
y_pred = np.argmax(model.predict(X_test), axis=-1)

# Print the predicted price range for mobile phones in the test set
print("\nPredicted Price Range:")
print(y_pred)

# Step 5: Performance Evaluation
# Obtain the true labels of the test set
y_true = test_data.iloc[:, -1].values

# Calculate accuracy
accuracy = np.mean(y_pred == y_true)
print("\nAccuracy:", accuracy)

# Calculate other evaluation metrics
report = classification_report(y_true, y_pred)
print("\nClassification Report:")
print(report)

# Calculate confusion matrix
confusion_mat = confusion_matrix(y_true, y_pred)
print("\nConfusion Matrix:")
print(confusion_mat)


# For example, to analyze misclassified samples:
misclassified_samples = X_test[y_pred != y_true]
print("\nMisclassified Samples:")
print(misclassified_samples)
