def time_split(df, split_ratio=0.7):
    split = int(len(df) * split_ratio)
    return df.iloc[:split], df.iloc[split:]
