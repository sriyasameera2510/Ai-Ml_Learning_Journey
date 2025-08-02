
# Week 9 – Hyperparameter Tuning

## 🔍 Objective

Optimize machine learning models using hyperparameter tuning techniques like **GridSearchCV** and **RandomizedSearchCV**. Learn how tuning impacts model performance and improves generalization.

---

## 🧠 Dataset Used

> Dataset: *Iris Dataset (or specify your actual dataset)*  
> Target Variable: `Species`  
> Task: Multiclass classification

---

## 🔨 Models Used

- **Random Forest Classifier**
- Evaluation Metrics: Precision, Recall, F1-Score, Accuracy

---

## 🧪 Experiments Performed

### ✅ Base Model
- Random Forest Classifier trained with default parameters.

### ✅ GridSearchCV
- Exhaustive search over parameter grid:
  ```python
  param_grid = {
      'n_estimators': [50, 100, 150],
      'max_depth': [None, 5, 10],
      'min_samples_split': [2, 4, 6]
  }
  ```
- Cross-validation used to select the best parameter combination.

### ✅ RandomizedSearchCV
- Performed random sampling from parameter distributions:
  ```python
  param_dist = {
      'n_estimators': randint(50, 200),
      'max_depth': randint(3, 15),
      'min_samples_split': randint(2, 10)
  }
  ```
- Faster than grid search for large parameter spaces.

---

## 🧾 Results

### 🎯 GridSearchCV Best Model:
- Accuracy: **1.00**
- Precision / Recall / F1 (for all classes): **1.00**

### 🎯 RandomizedSearchCV Best Model:
- Accuracy: **1.00**
- Precision / Recall / F1 (for all classes): **1.00**

✅ Both models achieved perfect accuracy on the test set (possibly due to simple data or small test size).

---

## 📊 Conclusion

- **Both GridSearchCV and RandomizedSearchCV** led to optimal model performance.
- RandomizedSearchCV is generally faster for large parameter spaces.
- GridSearchCV is better when you can afford to try all combinations and have limited parameters.
