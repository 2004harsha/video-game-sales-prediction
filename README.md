# Video Game Sales Prediction

This project focuses on analyzing and predicting video game sales using machine learning. It involves thorough exploratory data analysis (EDA), feature engineering, and model building with XGBoost to forecast global sales based on various features like platform, genre, and regional performance.

---

## Project Objective

The goal is to build a regression model that predicts **Global Sales** of a video game using features such as platform, genre, publisher, and regional sales statistics. The model is trained on a cleaned and preprocessed version of the [Video Game Sales Dataset](https://www.kaggle.com/datasets/gregorut/videogame-sales-with-ratings) from Kaggle.

---

## Dataset Summary

- **Total Records:** 16,598
- **Columns Used:** 11
- **Target Variable:** `Global_Sales`
- **Missing Values:** Handled via row removal (e.g., `Year`, `Publisher`)
- **File Used:** `modeling.ipynb`

---

## Exploratory Data Analysis (EDA)

Visualizations were created to understand the sales trends and feature distributions:

1. **Top Genres by Global Sales**  
2. **Top Platforms by Global Sales**  
3. **Regional Sales Comparison (NA, EU, JP)**  
4. **Sales Trend Over Years**  
5. **Correlation Heatmap of Regional and Global Sales**

EDA helped identify which variables significantly influence global sales.

---

## Feature Engineering

- **Dropped Columns:**  
  - `Name`, `Rank`, `Year`, `Publisher` (not useful or caused data leakage)
- **One-Hot Encoding** for:
  - `Platform`, `Genre`
- Final features selected based on correlation, relevance, and usability in a regression task.

---

## Model Used

- **XGBoost Regressor**
- Hyperparameters:
  - `n_estimators = 100`
  - `learning_rate = 0.1`
  - `max_depth = 6`

---

## Model Evaluation

Train/test split: 68% train, 32% test

**XGBoost Model Results:**

- **RMSE:** 1.6849  
- **MAE:** 0.4897  
- **R² Score:** 0.1043

Note: The R² score indicates that while the model captures some variance, sales data is noisy and may depend on external factors not captured in the dataset.

---

## Feature Importance Plot

A feature importance graph was generated to visualize which features contributed most to the prediction. Platform and genre were among the top contributors.

---

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost

---

## Conclusion

This project demonstrates the end-to-end process of building a machine learning pipeline for regression tasks. While the model performs modestly, the project covers:

- Data cleaning and EDA
- Feature engineering
- Regression modeling
- Performance evaluation

This serves as a solid example of applying data science and machine learning techniques to real-world business data.

---

## Future Improvements

- Include external data such as critic/user scores
- Tune model using advanced search (GridSearchCV or Optuna)
- Explore deep learning or ensemble models
- Build a front-end interface using Streamlit (optional demo)

---

## Folder Structure

```
.
├── modeling.ipynb          # Full EDA and model in one notebook
├── README.md               # Project documentation
├── plots/                  # Optional folder for images
└── data/                   # Original CSV file (optional)
```

---

## License

This project is for educational use only. Dataset credits to original creators on Kaggle.
