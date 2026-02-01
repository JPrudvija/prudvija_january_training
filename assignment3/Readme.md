Contains:
Dataset Used
For this assignment, I used the Medical Cost Personal Dataset from Kaggle.
File name: insurance.csv
Total records: 1338
Target variable: charges
The problem is a regression problem because the output (charges) is a continuous numerical value.

1. Data Cleaning
In the data cleaning step, I performed the following:
Loaded the dataset using pandas.
Checked for missing values using isnull().sum().
Removed duplicate rows if present.
Converted categorical columns (sex, smoker, region) into numerical format using One-Hot Encoding.
Saved the cleaned dataset as insurance_cleaned.csv.
There were no missing values in the dataset. After encoding, the dataset became fully numerical and ready for modeling.

2. Exploratory Data Analysis (EDA)
In EDA, I analyzed the dataset to understand patterns and relationships.
Steps performed:
Displayed dataset information using df.info().
Displayed statistical summary using df.describe().
Plotted histogram of charges to understand distribution.
Plotted correlation heatmap to check relationships between variables.

Observations:
The charges variable is positively skewed.
Smoking status has a strong effect on insurance charges.
Age and BMI also affect the charges.
No strong multicollinearity was observed among independent variables.

3. Data Splitting
The dataset was divided into:
80% Training data
20% Testing data
I used:
##train_test_split(test_size=0.2, random_state=42)
Training data is used to train the model and testing data is used to evaluate the model performance.

4. Linear Regression Model
I used the Linear Regression model from Scikit-learn.
Steps followed:
Separated input features (X) and target variable (y).
Trained the model using training data.
Predicted the charges for test data.
Linear Regression tries to find the best line that fits the data.

5. Model Evaluation
To evaluate the model, I used:
Mean Squared Error (MSE)
Measures the average squared difference between actual and predicted values.
Lower MSE means better model performance.
R² Score
Shows how well the model explains the variance.
R² value closer to 1 means better fit.
The model gave a good R² score, which means it explains a good portion of the variation in insurance charges.

Conclusion:
In this assignment, I successfully built a Linear Regression model to predict medical insurance charges.
The dataset was cleaned and prepared properly.
EDA helped in understanding the relationship between variables.
The model performed well based on MSE and R² score.
Smoking and age are the most important factors affecting insurance charges.
Therefore, Linear Regression is suitable for this dataset.



