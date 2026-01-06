import numpy as np

def logic_instability(probabilities):
    probabilities = np.asarray(probabilities)

    if probabilities.ndim == 1:
        raise ValueError("logic_instability expects prediction probabilities, not class labels")

    confidence = probabilities.max(axis=1)
    return float(np.var(confidence))
