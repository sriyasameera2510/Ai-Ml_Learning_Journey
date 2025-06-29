# 📘 Week 5 — Titanic: Advanced Models & Pipelines

## 🎯 Objective

This week focused on advancing my Titanic survival prediction model using more professional and robust machine learning techniques, including:
- Random Forest (Ensemble method)
- Pipelines for clean preprocessing
- Feature importance analysis
- Cross-validation
- Model comparison

---

## ✅ Tasks Completed

### 1️⃣ Data Preparation
- Loaded and cleaned the Titanic dataset
- Categorical variables (`Sex`, `Embarked`) were encoded using `pd.get_dummies`
- Missing values in `Age` and `Fare` were filled using the **median**

### 2️⃣ Model Training: Random Forest
- Trained a `RandomForestClassifier` on selected features
- Evaluated performance using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - Confusion matrix

### 3️⃣ Feature Scaling
- Applied `StandardScaler` to numerical features (mainly for pipeline and other models)

### 4️⃣ Pipelines
- Created a `Pipeline` using:
  - `SimpleImputer` (median fill)
  - `StandardScaler`
  - `RandomForestClassifier`
- Trained and evaluated pipeline output

### 5️⃣ Cross-Validation
- Used `cross_val_score` with 5-fold CV to evaluate performance of Random Forest

### 6️⃣ Feature Importance
- Visualized `feature_importances_` to understand which features the Random Forest model relied on most

### 7️⃣ Model Comparison
- Compared Logistic Regression, Decision Tree, and Random Forest based on evaluation metrics

---

## 📊 Model Comparison Table

| Model               | Accuracy | Precision | Recall | F1 Score |
|--------------------|----------|-----------|--------|----------|
| Logistic Regression| 0.81  | 0.78   | 0.74 | 0.76  |
| Decision Tree      | 0.78   | 0.72    | 0.75 | 0.74   |
| Random Forest      | 0.82   | 0.80    | 0.75 | 0.77   |


---

## 🔑 Key Learnings

- Pipelines allow clean chaining of preprocessing + model training
- Random Forest performs well with minimal tuning and provides insight into feature importance
- Cross-validation offers more reliable performance estimates than a single train/test split
- Feature importance helps understand model decisions and potential improvements
