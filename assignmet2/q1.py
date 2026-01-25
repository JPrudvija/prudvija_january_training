#  Question1
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("synthetic_customer_churn_100k.csv")

print("Initial Shape:", df.shape)

# Display basic info
print("Shape of dataset:", df.shape)
print("\nColumn names:\n", df.columns)
print("\nDataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Handling Missing Values

# Numerical columns
num_cols = ["Age", "Tenure", "MonthlyCharges", "TotalCharges"]
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Categorical columns
cat_cols = ["Gender", "Contract", "PaymentMethod", "Churn"]
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)
# Fixing Data Types

df["Churn"] = df["Churn"].astype("category")

# Removing Duplicates

df.drop_duplicates(inplace=True)

# Outlier Treatment (IQR Method)
for col in ["MonthlyCharges", "TotalCharges"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.clip(df[col], lower, upper)

# Dropping Irrelevant Columns

df.drop(columns=["CustomerID"], inplace=True)

print("Final Shape:", df.shape)

# Save cleaned dataset
df.to_csv("cleaned_churn_data.csv", index=False)
