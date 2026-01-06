def predict(model, X):
    preds = model.predict(X)
    probs = model.predict_proba(X)
    return preds, probs
