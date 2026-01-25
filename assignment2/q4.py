#Question 4
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
df = pd.read_csv("encoded_churn_data.csv")
# Skewness Transformation
df["TotalCharges_Log"] = np.log1p(df["TotalCharges"])

# Train-Test Split
X = df.drop(columns=["Churn", "Churn_LE"])
y = df["Churn_LE"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("Training set:", X_train.shape)
print("Testing set:", X_test.shape)
