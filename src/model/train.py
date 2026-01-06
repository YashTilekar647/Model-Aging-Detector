import os
import joblib
from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=6,
        min_samples_leaf=10,
        random_state=42
    )

    model.fit(X, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/base_model.pkl")

    return model
