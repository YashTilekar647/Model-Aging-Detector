import numpy as np
import pandas as pd

def generate_data(n_samples, shift=False):
    np.random.seed(42)

    age = np.random.randint(18, 70, n_samples)
    income = np.random.randint(20000, 120000, n_samples)
    activity = np.random.rand(n_samples)

    # Original logic
    if not shift:
        risk = (age > 50).astype(int)
    else:
        # New hidden logic (aging cause)
        risk = ((income < 40000) & (activity < 0.4)).astype(int)

    df = pd.DataFrame({
        "age": age,
        "income": income,
        "activity_score": activity,
        "risk": risk
    })

    return df
