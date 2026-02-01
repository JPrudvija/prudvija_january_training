# Customer Churn Prediction - Supervised Machine Learning

## Project Objective

The objective of this project is to predict whether a customer will churn (leave the company) or not using supervised machine learning algorithms.  
Since the target variable (Churn) has two categories (Yes/No), this is a classification problem.

## Dataset Description

Dataset Name: Telco Customer Churn (Kaggle)

- Total Records: 7043
- Target Variable: Churn (Yes / No)
- Features include:
  - Tenure
  - MonthlyCharges
  - TotalCharges
  - Contract Type
  - Internet Service
  - Payment Method
  - SeniorCitizen
  - Partner
  - Dependents
  - and other service-related features

The dataset contains both numerical and categorical variables.

## Data Preprocessing Steps

Before applying machine learning algorithms, proper data cleaning and preprocessing was performed:

• Removed duplicate records  
• Removed irrelevant column (customerID)  
• Converted TotalCharges to numeric datatype  
• Handled missing values using median imputation  
• Encoded categorical variables using Label Encoding and One-Hot Encoding  
• Applied StandardScaler for feature scaling  
• Split the dataset into training and testing sets (80:20 ratio)  

These preprocessing steps improved model performance and ensured better prediction accuracy.

## Algorithms Used

The following five supervised learning algorithms were implemented:

1. Logistic Regression  
2. Decision Tree Classifier  
3. Random Forest Classifier  
4. K-Nearest Neighbors (KNN)  
5. Support Vector Machine (SVM)  

Each model was trained using the training dataset and tested using the testing dataset.

## Evaluation Metrics Used

The following classification metrics were used to evaluate model performance:

- Accuracy  
- Precision  
- Recall  
- F1-Score  

## Model Performance Results

The performance of different classification algorithms is as follows:

Logistic Regression  
- Accuracy: 80%  
- Precision: 78%  
- Recall: 74%  
- F1-Score: 76%  

Decision Tree  
- Accuracy: 73%  
- Precision: 70%  
- Recall: 69%  
- F1-Score: 69%  

Random Forest  
- Accuracy: 85%  
- Precision: 83%  
- Recall: 80%  
- F1-Score: 81%  

K-Nearest Neighbors (KNN)  
- Accuracy: 78%  
- Precision: 75%  
- Recall: 72%  
- F1-Score: 73%  

Support Vector Machine (SVM)  
- Accuracy: 82%  
- Precision: 80%  
- Recall: 77%  
- F1-Score: 78%  

## Best Performing Model

Among all the models, Random Forest Classifier performed the best with the highest accuracy of 85% and balanced Precision, Recall, and F1-Score.

## Conclusion

This project demonstrates how different supervised machine learning algorithms perform on the same dataset.

Key observations:

- Proper data preprocessing significantly improved model performance  
- Random Forest provided the highest accuracy  
- SVM and Logistic Regression also gave good results  
- Decision Tree showed slightly lower performance  
- Feature scaling improved KNN and SVM results  

Overall, Random Forest is the most suitable model for predicting customer churn in this dataset.
