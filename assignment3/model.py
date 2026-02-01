# model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def train_model(df):

    # Separate features and target
    X = df.drop("charges", axis=1)
    y = df["charges"]

    # Split data (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model Evaluation")
    print("----------------")
    print("Mean Squared Error (MSE):", mse)
    print("R² Score:", r2)

    # Display coefficients
    coefficients = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": model.coef_
    })

    print("\nFeature Importance (Coefficients):")
    print(coefficients.sort_values(by="Coefficient", ascending=False))

    return model


if __name__ == "__main__":
    df = pd.read_csv("data/insurance_cleaned.csv")
    train_model(df)

