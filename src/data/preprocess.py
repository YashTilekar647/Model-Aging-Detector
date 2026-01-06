import pandas as pd

def preprocess(df, target_col, reference_columns=None):
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Handle missing values
    for col in X.columns:
        if X[col].dtype == "object":
            X[col] = X[col].fillna(X[col].mode()[0])
        else:
            X[col] = X[col].fillna(X[col].median())

    # Encode categoricals
    X = pd.get_dummies(X, drop_first=True)

    # Align columns if reference provided
    if reference_columns is not None:
        X = X.reindex(columns=reference_columns, fill_value=0)

    return X, y
