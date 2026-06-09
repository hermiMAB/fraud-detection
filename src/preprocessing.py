import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    """Loads dataset with error handling."""
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return None

def clean_data(df):
    """Handles missing values and duplicates."""
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def engineer_time_features(df, signup_col='signup_time', purchase_col='purchase_time'):
    """Extracts temporal features safely."""
    try:
        df[signup_col] = pd.to_datetime(df[signup_col])
        df[purchase_col] = pd.to_datetime(df[purchase_col])
        df['hour_of_day'] = df[purchase_col].dt.hour
        df['day_of_week'] = df[purchase_col].dt.dayofweek
        df['time_since_signup'] = (df[purchase_col] - df[signup_col]).dt.total_seconds()
        return df
    except Exception as e:
        print(f"Error in time feature engineering: {e}")
        return df