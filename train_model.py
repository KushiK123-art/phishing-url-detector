import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from feature_extraction import extract_features

# Load dataset

df = pd.read_csv('dataset/phishing.csv')

# Extract features
X = df['URL'].apply(extract_features).tolist()
y = df['Label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Save model
with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print('Model trained and saved successfully!')