# 🛳️ Week 2 – Titanic Dataset Analysis using Pandas & NumPy

## 🎯 Objective

To explore and analyze the Titanic dataset using Pandas and NumPy with the goal of uncovering relationships between passenger features (like age, gender, and embarkation port) and survival outcomes.

---

## 📥 Dataset

- **Source**: [Titanic CSV](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)
- **Shape**: 891 rows × 12 columns
- **Key Columns**: `Survived`, `Pclass`, `Sex`, `Age`, `Embarked`, `Fare`

---

## 🔍 Key Tasks Completed

- ✅ Loaded and explored the dataset using `pandas`
- ✅ Identified and filled missing values (`Age`, `Embarked`)
- ✅ Created new features like:
  - `FamilySize = SibSp + Parch`
  - `AgeBin` (categorized age ranges)
- ✅ Performed group-by analysis:
  - Survival rates by `Sex`, `Pclass`, and `Embarked`
- ✅ Calculated correlations between `Age`, `Fare`, and `Survived`
- ✅ Visualized survival rates using `matplotlib` and `seaborn`

---

## 📊 Key Visualizations

- **Bar Chart – Survival Rate by Embarked Location**  
  Compared average survival rate for passengers boarding from Cherbourg, Queenstown, and Southampton. Showed highest survival from Cherbourg.

- **Histogram – Age Distribution of Passengers**  
  Displayed overall age spread, helping identify groups (children, adults, seniors) for further analysis.

- **Bar Plot – Survival Rate by Gender**  
  Clear difference in survival rate between males and females.

- **Heatmap – Feature Correlation**  
  Visualized correlation between `Age`, `Fare`, and `Survived`, revealing a slight positive correlation with `Fare`.

---

## 💡 Insights

- Passengers who boarded at **Cherbourg (C)** had the highest survival rate.
- **Females had a significantly higher survival rate** than males, especially in 1st and 2nd class.
- **Fare paid showed some correlation** with survival — higher fare, better odds.
- **Young adults and children** had better survival rates compared to older passengers.

---

## 🧠 Learnings

- Practiced Pandas for data cleaning and EDA
- Understood the power of group-by and pivot operations
- Visualizations help surface patterns quickly
- Learned how missing data can impact analysis

---

## 🧪 Next Steps

- Start building machine learning models using this cleaned dataset
- Try logistic regression for survival prediction
- Apply cross-validation and evaluation metrics (Week 4+)

---

## 🛠️ Tools Used

- Python 3.10
- Jupyter Notebook / JupyterLab
- Pandas, NumPy, Matplotlib, Seaborn

---

## 🔗 References

- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
- [Pandas Docs](https://pandas.pydata.org/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

