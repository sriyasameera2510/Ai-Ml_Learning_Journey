# Heart Disease Prediction Project (Week 6)

This project focuses on predicting the presence of heart disease using clinical data. We use multiple machine learning models to train and evaluate performance on a public dataset.

---

## 📊 Dataset

**Source**: [Kaggle - Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)  
**File used**: `heart.csv.xls`

---

## 🎯 Objective

To build an end-to-end machine learning pipeline that:
- Cleans and prepares the dataset
- Trains multiple models
- Evaluates and compares performance
- Identifies important features

---

## 🔧 Steps Performed

1. **Data Loading & Exploration**
   - Loaded `heart.csv` and explored shape, nulls, and datatypes.

2. **Data Cleaning**
   - Verified no missing values.
   - Encoded categorical columns using one-hot encoding.

3. **Feature Definition**
   - `X`: All columns except `HeartDisease`
   - `y`: The `HeartDisease` column (target)

4. **Model Training**
   - Logistic Regression
   - Random Forest Classifier
   - Decision Tree Classifier

5. **Evaluation**
   - Metrics used: Accuracy, Precision, Recall, F1-score

6. **Feature Importance**
   - Visualized top features using the trained Random Forest model

---

## 🏆 Best Model

**Random Forest Classifier**

| Metric      | Value     |
|-------------|-----------|
| Accuracy    | 87%       |
| F1-score    | 0.87      |

---

## ✅ Conclusion

- After training Logistic Regression, Random Forest, and Decision Tree models, Random Forest performed       best with an accuracy of 87% and balanced precision/recall. It also achieved the highest F1-score,         making it the most effective at identifying heart disease without overfitting.


