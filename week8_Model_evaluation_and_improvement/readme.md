# 🫀 Heart Disease Prediction - Week 8

This project focuses on evaluating multiple machine learning models to determine the best performer for predicting heart disease. This task is part of Week 8 in the AI/ML learning journey.

---

## 📌 Objective

Evaluate and compare different classification models:
- Logistic Regression (L2 Regularization)
- Decision Tree
- Random Forest

Identify the best model based on performance metrics.

---

## 📁 Dataset

The dataset used includes clinical features for heart disease diagnosis, with columns such as:

- Age
- RestingBP
- Cholesterol
- FastingBS
- MaxHR
- Oldpeak
- Sex_M, ChestPainType_*, RestingECG_*, etc. (One-hot encoded categorical features)

The target variable is:
- `HeartDisease` (0 = No, 1 = Yes)

---

## ⚙️ Models Trained

1. **Logistic Regression (L2 penalty)**
2. **Decision Tree Classifier**
3. **Random Forest Classifier**

---

## 📊 Model Evaluation

Each model was evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score

### ✅ Final Model Selected: Random Forest

| Model               | Accuracy | Precision (1) | Recall (1) | F1-score (1) |
|---------------------|----------|----------------|------------|--------------|
| Random Forest        | 0.88     | 0.90           | 0.89       | 0.89         |
| Decision Tree        | 0.85     | 0.88           | 0.87       | 0.87         |
| Logistic Regression  | 0.85     | 0.90           | 0.84       | 0.87         |

Random Forest gave the highest performance overall and was chosen as the final model.

---

## 🗂️ Files

- `week8_model_evaluation.ipynb`: Jupyter Notebook containing all training, evaluation, and results.
- `README.md`: Project overview.

