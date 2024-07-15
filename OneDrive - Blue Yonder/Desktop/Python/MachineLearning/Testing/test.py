import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data, target=None):
    if target is not None and target in data.columns:
        X = data.drop(columns=[target])
        y = data[target]
    else:
        X = data
        y = None
    
    # Convert categorical variables to numerical format using one-hot encoding
    X = pd.get_dummies(X)
    
    return X, y

def build_model(data, target):
    X, y = preprocess_data(data, target)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    
    return model

# Main script
data = load_data(r"MachineLearning\Data\people.csv")
model = build_model(data, target="Marital status")

new_data = load_data(r"MachineLearning\Data\new_people.csv")
new_data_processed, _ = preprocess_data(new_data)  # No target column in new data
predictions = model.predict(new_data_processed)

print("Predictions for new data:", predictions)
