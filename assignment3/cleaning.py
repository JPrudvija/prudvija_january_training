#Creanling Data set
# cleaning.py

import pandas as pd
import os


def load_data(filepath="data/insurance.csv"):
    """
    Load dataset
    """
    df = pd.read_csv(filepath)
    return df


def clean_data(df):
    """
    Perform data cleaning
    """

    print("Initial Shape:", df.shape)

    # Check missing values
    print("\nMissing Values:\n")
    print(df.isnull().sum())

    # Remove duplicates
    df = df.drop_duplicates()
    print("\nShape after removing duplicates:", df.shape)

    # Convert categorical variables using One-Hot Encoding
    df = pd.get_dummies(df, drop_first=True)

    print("\nFinal Columns:\n", df.columns)

    return df


if __name__ == "__main__":
    df = load_data()
    df_cleaned = clean_data(df)

    # Save cleaned file
    os.makedirs("data", exist_ok=True)
    df_cleaned.to_csv("data/insurance_cleaned.csv", index=False)

    print("\nCleaned dataset saved as data/insurance_cleaned.csv")
