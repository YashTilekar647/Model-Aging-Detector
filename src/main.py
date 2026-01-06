# Fix path
import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import joblib

from src.data.load_data import load_dataset
from src.data.preprocess import preprocess
from src.data.time_split import time_split

from src.model.train import train_model
from src.model.predict import predict
from src.model.evaluate import evaluate

from src.features.feature_shift import feature_shift
from src.monitoring.confidence_shift import confidence_shift
from src.monitoring.logic_stability import logic_instability
from src.monitoring.aging_detector import detect_aging

from src.utils.logger import log
from src.utils.report_generator import generate_report

# ================= CONFIG =================
DATA_PATH = "data/raw/dataset.csv"
TARGET_COLUMN = "Survived"   # USER DEFINES THIS
# ==========================================

df = load_dataset(DATA_PATH, TARGET_COLUMN)

baseline_df, current_df = time_split(df)

# Preprocess baseline
X_base, y_base = preprocess(baseline_df, TARGET_COLUMN)

# Preprocess current using baseline columns as reference
X_curr, y_curr = preprocess(
    current_df,
    TARGET_COLUMN,
    reference_columns=X_base.columns
)


model = train_model(X_base, y_base)



# SAVE FEATURE SCHEMA USED FOR TRAINING (VERY IMPORTANT)
joblib.dump(
    X_base.columns.tolist(),
    "models/feature_columns.pkl"
)


base_preds, base_probs = predict(model, X_base)
curr_preds, curr_probs = predict(model, X_curr)

base_acc = evaluate(y_base, base_preds)
curr_acc = evaluate(y_curr, curr_preds)

instability = logic_instability(curr_probs)

conf_shift = confidence_shift(base_probs, curr_probs)
feat_shift = 0.0  # structural comparison optional

status = detect_aging(feat_shift, conf_shift, instability)

metrics = {
    "Baseline Accuracy": base_acc,
    "Current Accuracy": curr_acc,
    "Instability": instability,
    "Confidence Shift": conf_shift,
    "Feature Shift": feat_shift
}

log(metrics)
log(status)
generate_report(metrics, status)

print("MODEL STATUS:", status)
