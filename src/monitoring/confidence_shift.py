import numpy as np

def confidence_shift(old_probs, new_probs):
    old_conf = np.mean(np.max(old_probs, axis=1))
    new_conf = np.mean(np.max(new_probs, axis=1))
    return float(new_conf - old_conf)
