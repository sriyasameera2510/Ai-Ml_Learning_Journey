# 📊 Week 3 — Model Evaluation & Metrics

## 🎯 Objective

This week’s goal was to understand how to evaluate machine learning models before building them. I practiced key concepts like **train/test splitting**, **bias vs variance**, and **evaluation metrics** (accuracy, precision, recall, F1 score). I also visualized a confusion matrix for a simple rule-based prediction.

---

## 📁 Tasks Completed

### ✅ 1️⃣ Train/Test Split
- Used `train_test_split` from `scikit-learn` to divide the Titanic dataset into training and testing sets (70/30 split).
- Verified shapes to confirm proper split.

### ✅ 2️⃣ Manual Metrics Calculation
- Created a hypothetical confusion matrix with TP, FP, FN, TN values.
- Manually calculated accuracy, precision, recall, and F1 score using basic math formulas.

### ✅ 3️⃣ Visual Confusion Matrix
- Made a simple prediction rule: predict all females survived, all males didn’t.
- Compared predictions to true survival labels.
- Plotted a confusion matrix using `ConfusionMatrixDisplay`.

### ✅ 4️⃣ Verified with `scikit-learn` Metrics
- Used `accuracy_score`, `precision_score`, `recall_score`, and `f1_score` to confirm manual results.

### ✅ 5️⃣ Conceptual Explanations
- Wrote a short note on **Bias vs Variance** and its impact on model fitting.
- Wrote a scenario explaining when to prefer **precision vs recall** (e.g., cancer detection vs spam filtering).

---

## 📊 Key Learnings

- **Bias vs Variance:** High bias means underfitting (too simple); high variance means overfitting (too complex).
- **Accuracy alone is not enough:** For imbalanced datasets, precision and recall give better insight into model quality.
- **Confusion Matrix:** Helps see true positives, false positives, true negatives, and false negatives visually.

