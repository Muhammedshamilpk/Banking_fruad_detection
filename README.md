# 🏦 Banking Fraud Detection System

An end-to-end Machine Learning application that detects fraudulent credit card transactions using a Random Forest classifier. The project includes data preprocessing, model training, prediction pipeline, and an interactive Streamlit dashboard for fraud analysis.

---

## 📌 Project Overview

Financial fraud is one of the biggest challenges in the banking industry. This project uses Machine Learning to classify credit card transactions as **Fraudulent** or **Genuine** based on historical transaction data.

The application allows users to upload transaction data, predict fraud in real time, visualize results through an interactive dashboard, and export prediction reports.

---

## ✨ Features

- 📂 Upload transaction CSV files
- 🤖 Fraud detection using a trained Random Forest model
- 📊 Interactive dashboard with fraud statistics
- 📈 Fraud vs Genuine transaction visualization
- 🚨 View detected fraudulent transactions
- 📋 Display prediction results with fraud probability
- 📥 Download prediction results as CSV
- 🧩 Modular and scalable project structure

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Random Forest Classifier

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly
- Streamlit

### Model Serialization

- Joblib

---

## 📂 Project Structure

```text
Banking_Fraud_Detection/
│
├── app/
│   ├── app.py
│   ├── dashboard.py
│   ├── components.py
│   └── styles.py
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── predict.py
│   ├── utils.py
│   └── __init__.py
│
├── models/
│   ├── random_forest_balanced.pkl
│   └── scaler.pkl
│
├── data/
│   ├── demo_dataset.csv
│   ├── fraud_transactions.csv
│   └── raw/
│
├── notebooks/
│   └── EDA.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

This project uses the **Credit Card Fraud Detection Dataset** from Kaggle.

**Dataset Source**

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Dataset Statistics

- Total Transactions: **284,807**
- Fraudulent Transactions: **492**
- Genuine Transactions: **284,315**
- Features: **30**
- Target Column: **Class**

---

## ⚙️ Machine Learning Pipeline

### Data Preprocessing

- Handle missing values
- Feature scaling using StandardScaler
- Train-test split
- Class imbalance handling

### Model Training

- Random Forest Classifier
- Hyperparameter tuning
- Model evaluation

### Prediction

- Load trained model
- Load scaler
- Preprocess uploaded dataset
- Predict fraud probability
- Display dashboard

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 99.95% |
| Precision | 91% |
| Recall | 76% |
| F1 Score | 83% |

> Performance may vary slightly depending on train-test split and model parameters.

---

## 🖥️ Dashboard Features

The Streamlit dashboard provides:

- Transaction overview
- Fraud statistics
- Fraud rate
- Fraud distribution chart
- Fraud transaction table
- Download prediction report

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Muhammedshamilpk/Bank-fraud-detection.git

cd Bank-fraud-detection
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app/app.py
```

The application will open at:

```
http://localhost:8501
```

---

## 📸 Application Workflow

1. Upload a transaction CSV file
2. Click **Predict Fraud**
3. View fraud statistics
4. Analyze detected fraud transactions
5. Download prediction report

---

## 📌 Future Improvements

- AWS deployment
- XGBoost model comparison
- Explainable AI using SHAP
- Real-time fraud detection API
- Docker containerization
- User authentication
- Database integration
- Live transaction monitoring

---

## 🎯 Learning Outcomes

Through this project I gained hands-on experience in:

- Machine Learning model development
- Fraud detection techniques
- Data preprocessing
- Model evaluation
- Streamlit application development
- Modular Python project architecture
- Model deployment

---

## 👨‍💻 Author

**Muhammed Shamil P K**

Python Developer | AI & Machine Learning Enthusiast

LinkedIn:
https://www.linkedin.com/in/muhammedshamilpk/

GitHub:
https://github.com/Muhammedshamilpk

---

## 📜 License

This project is intended for educational and portfolio purposes.
