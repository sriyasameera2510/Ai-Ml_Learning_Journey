# Week 4 — Titanic: First Machine Learning Model

## Objective

This week’s goal was to build my **first supervised machine learning models** using the Titanic dataset.  
I applied everything learned so far: data cleaning, feature selection, encoding, train-test split, metrics, and hyperparameter tuning.

---

## Tasks Completed

### 1️⃣ Data Preparation
- Loaded the cleaned Titanic dataset.
- Selected relevant features: `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`, `Sex`, `Embarked`.
- Encoded `Sex` and `Embarked` with `pd.get_dummies()`.
- Filled missing `Age` values with the median.

### 2️⃣ Model Training
- Defined features (**X**) and label (**y**).
- Split data into training and test sets (80/20).
- Trained **Logistic Regression** as a baseline model.
- Trained a **Decision Tree Classifier** for comparison.

### 3️⃣ Evaluation
- Used **accuracy**, **precision**, **recall**, **F1 score** to evaluate.
- Plotted the **confusion matrix** for each model.
- Compared how different models performed and how tuning affected them.

---

## Key Results

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 0.81 | 0.78 | 0.74 | 0.76 |
| Decision Tree | 0.78 | 0.72 | 0.75 | 0.74 |


---

## Insights

- Logistic Regression is a simple but effective baseline.
- Decision Trees can capture more complex patterns but may overfit if not tuned.
- Handling missing data and categorical variables properly is essential for training valid models.

---

## Next Steps

- Try more advanced models: **Random Forest**, **Gradient Boosting**, or **XGBoost**.
- Analyze **feature importance** to see which variables matter most.
- Use **Pipelines** to automate preprocessing + modeling.
- Experiment with cross-validation for more robust estimates.
