#Question 2

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from category_encoders import OrdinalEncoder, TargetEncoder
df = pd.read_csv("cleaned_churn_data.csv")

# Label Encoding (Binary)
le = LabelEncoder()
df["Gender_LE"] = le.fit_transform(df["Gender"])
df["Churn_LE"] = le.fit_transform(df["Churn"])

# Ordinal Encoding
ordinal_map = {
    "Contract": {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    }
}
ord_enc = OrdinalEncoder(mapping=[ordinal_map])
df["Contract_OE"] = ord_enc.fit_transform(df[["Contract"]])

# One-Hot Encoding
df = pd.get_dummies(df, columns=["PaymentMethod"], drop_first=True)
# Frequency Encoding
freq_map = df["Contract"].value_counts(normalize=True)
df["Contract_FE"] = df["Contract"].map(freq_map)
# Target Encoding
te = TargetEncoder(cols=["Contract"])
df["Contract_TE"] = te.fit_transform(df["Contract"], df["Churn_LE"])
df.to_csv("encoded_churn_data.csv", index=False)
