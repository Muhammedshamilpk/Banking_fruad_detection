import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    """
    Load dataset from CSV.
    """
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """
    Remove duplicate rows.
    """
    df = df.drop_duplicates()
    return df


def preprocess_data(df):
    """
    Split features and target, then scale Amount and Time.
    """

    X = df.drop("Class", axis=1)
    y = df["Class"]

    amount_scaler = StandardScaler()
    time_scaler = StandardScaler()
    
    
    X["Amount"] = amount_scaler.fit_transform(X[["Amount"]])
    X["Time"] = time_scaler.fit_transform(X[["Time"]])

    return X, y, amount_scaler,time_scaler