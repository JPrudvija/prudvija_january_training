# eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def perform_eda(df):

    print("Dataset Info:\n")
    print(df.info())

    print("\nStatistical Summary:\n")
    print(df.describe())

    # Distribution of target variable
    plt.figure()
    sns.histplot(df["charges"], kde=True)
    plt.title("Distribution of Insurance Charges")
    plt.xlabel("Charges")
    plt.ylabel("Frequency")
    plt.show()

    # Correlation Heatmap
    plt.figure()
    correlation = df.corr()
    sns.heatmap(correlation, annot=True)
    plt.title("Correlation Matrix")
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("data/insurance_cleaned.csv")
    perform_eda(df)
