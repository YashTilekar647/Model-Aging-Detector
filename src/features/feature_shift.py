import numpy as np

def feature_shift(old_importance, new_importance):
    return float(np.mean(np.abs(old_importance - new_importance)))
