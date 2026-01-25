Question 2
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, StandardScaler, Normalizer
df = pd.read_csv("encoded_churn_data.csv")
num_cols = ["Age", "Tenure", "MonthlyCharges", "TotalCharges"]
# Min-Max Scaling
minmax = MinMaxScaler()
df_minmax = minmax.fit_transform(df[num_cols])

# Max Absolute Scaling
maxabs = MaxAbsScaler()
df_maxabs = maxabs.fit_transform(df[num_cols])

# Z-Score Standardization
standard = StandardScaler()
df_standard = standard.fit_transform(df[num_cols])

# Vector Normalization

normalizer = Normalizer()
df_normalized = normalizer.fit_transform(df[num_cols])
print("Feature Scaling Completed")
