from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target variable (species)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create KNN classifier
k = 3  # Define the number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)

# Train the model
knn.fit(X_train, y_train)

# Predict the species for a new iris flower
# You can input your own values for sepal length, sepal width, petal length, and petal width
new_flower_data = [[5.1, 3.5, 1.4, 0.2]]  # Example values, replace with your data
predicted_species = knn.predict(new_flower_data)

# Map the predicted label to the corresponding species name
species_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
predicted_species_name = species_mapping[predicted_species[0]]

print(f"The predicted species for the new flower is: {predicted_species_name}")

# Evaluate the model's accuracy on the test set
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the KNN classifier: {accuracy:.2f}")




