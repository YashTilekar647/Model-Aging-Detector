def detect_aging(feature_shift_score, confidence_shift_score, instability_score):
    if feature_shift_score > 0.15:
        return "CRITICAL: LOGIC AGING DETECTED"

    if confidence_shift_score > 0.20:
        return "WARNING: OVERCONFIDENT MODEL"

    if instability_score > 0.25:
        return "WARNING: UNSTABLE PREDICTIONS"

    return "MODEL HEALTHY"
