# ❤️ Heart Disease Prediction using Machine Learning

This project is a machine learning-based web application that predicts the likelihood of a person having heart disease based on key health metrics. It aims to assist in early diagnosis and awareness using data-driven predictions.

## 📌 Table of Contents


- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Installation](#installation)



---



---

## ✅ Features

- Predicts heart disease risk from user-inputted health metrics.
- Clean, simple frontend for user input.
- Model trained on real-world medical data.
- Metrics displayed: Accuracy, Precision, Recall, F1-Score, ROC AUC.
- Visualizations to understand model and data patterns.

---

## 🧠 Tech Stack

| Area           | Technology                          |
|----------------|-------------------------------------|
| ML Model       | Scikit-learn                        |
| Backend        | Flask / FastAPI                     |
| Frontend       | HTML/CSS                            |
| Visualization  | Matplotlib, Seaborn, Plotly         |
| Deployment     | Vercel                              |

---

## 📊 Dataset

- **Source**: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
- **Attributes**:
  - `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`
- **Target**:
  - `0` = No Heart Disease
  - `1` = Heart Disease

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
pip install -r requirements.txt
python app.py  # or streamlit run app.py
