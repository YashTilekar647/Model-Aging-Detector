import os, sys, joblib
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.data.preprocess import preprocess


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from src.monitoring.logic_stability import logic_instability
from src.monitoring.aging_detector import detect_aging

MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "base_model.pkl")

st.set_page_config(page_title="Model Aging Detector", layout="wide")
st.title("🧠 Model Aging Detector")

model = joblib.load(MODEL_PATH)
# Load training feature schema
feature_columns = joblib.load(
    os.path.join(PROJECT_ROOT, "models", "feature_columns.pkl")
)


df = pd.read_csv("data/raw/dataset.csv")
# SAME target column as training
TARGET_COLUMN = df.columns[-1]   # or hardcode if you want

# Preprocess using SAME logic & SAME feature space
X_dash, _ = preprocess(
    df,
    TARGET_COLUMN,
    reference_columns=feature_columns
)

# Safe predictions
preds = model.predict(X_dash)
probs = model.predict_proba(X_dash)

confidence_scores = probs.max(axis=1)

# Compute instability using CONFIDENCE (locked contract)
instability = logic_instability(probs)







st.subheader("Dataset Preview")
st.dataframe(df.head())


status = detect_aging(0.0, 0.0, instability)

st.metric("Prediction Instability", round(instability, 4))

#ploting confidence distribution
st.subheader("Prediction Confidence Distribution")

fig, ax = plt.subplots()
ax.hist(confidence_scores, bins=20)
ax.set_xlabel("Prediction Confidence")
ax.set_ylabel("Number of Samples")
ax.set_title("Model Confidence Spread")

st.pyplot(fig)

#p
st.subheader("Feature Importance")

importances = model.feature_importances_
top_idx = importances.argsort()[-10:]

fig2, ax2 = plt.subplots()
ax2.barh(
    range(len(top_idx)),
    importances[top_idx]
)
ax2.set_yticks(range(len(top_idx)))
ax2.set_yticklabels([X_dash.columns[i] for i in top_idx])
ax2.set_title("Top Influential Features")

st.pyplot(fig2)



if "HEALTHY" in status:
    st.success(status)
elif "WARNING" in status:
    st.warning(status)
else:
    st.error(status)
