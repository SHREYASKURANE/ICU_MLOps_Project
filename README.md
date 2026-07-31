# 🏥 ICU Patient Deterioration Prediction using MLOps & DevOps

## 📌 Project Overview

This project predicts whether an ICU patient is likely to survive or deteriorate based on various clinical parameters using Machine Learning. The complete project demonstrates an end-to-end MLOps pipeline integrated with DevOps tools including GitHub, MLflow, Docker, Jenkins, and AWS.

This project was developed as part of a DevOps & MLOps learning project to understand the complete machine learning lifecycle from data preprocessing to cloud deployment.

---

# 🎯 Objectives

- Build a machine learning model for ICU patient survival prediction.
- Track machine learning experiments using MLflow.
- Containerize the application using Docker.
- Automate build and deployment using Jenkins.
- Deploy the application on AWS EC2.
- Maintain version control using Git and GitHub.
- Build a reproducible and scalable MLOps pipeline.

---

# 🛠️ Tech Stack

## Programming Language

- Python 3.11

## Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

## MLOps

- MLflow
- Joblib

## DevOps

- Git
- GitHub
- Docker
- Jenkins

## Cloud

- AWS EC2

## Development Tools

- VS Code
- Jupyter Notebook

---

# 📂 Project Structure

```text
ICU_MLOps_Project/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   │      ICU.csv
│   └── processed/
│          train_processed.csv
│          test_processed.csv
│
├── models/
│      best_model.pkl
│      scaler.pkl
│
├── mlruns/
│
├── notebooks/
│      01_Data_Understanding.ipynb
│      02_Data_Preprocessing.ipynb
│      03_Model_Training.ipynb
│      04_MLflow.ipynb
│
├── src/
│      config.py
│      data_loader.py
│      preprocess.py
│      train.py
│      evaluate.py
│      predict.py
│      utils.py
│
├── tests/
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

The dataset contains ICU patient information collected from hospital records.

Features include:

- Age
- Blood Pressure
- Heart Rate
- Oxygen Saturation
- Temperature
- Glucose Level
- ICU Stay Duration
- Other Clinical Measurements

Target Variable:

```
Survive
```

- 1 → Survived
- 0 → Not Survived

---

# ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Train-Test Split
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Model Saving
10. MLflow Experiment Tracking

---

# 🤖 Machine Learning Model

Current Model:

- Logistic Regression

Future Improvements:

- Random Forest
- XGBoost
- Gradient Boosting
- CatBoost

---

# 📈 Evaluation Metrics

The following metrics are logged using MLflow:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

---

# 📦 MLflow

MLflow is used to:

- Track experiments
- Log parameters
- Log metrics
- Store trained models
- Compare model runs

---

# 🐳 Docker

Docker is used to:

- Package the application
- Ensure reproducibility
- Simplify deployment
- Run the application consistently across environments

---

# ⚙️ Jenkins

Jenkins automates:

- Pull latest code from GitHub
- Install dependencies
- Run preprocessing
- Train the model
- Track experiments in MLflow
- Build Docker image
- Deploy application

---

# ☁️ AWS Deployment

The application will be deployed on:

- AWS EC2

Deployment Steps:

- Launch EC2 Instance
- Install Docker
- Install Jenkins
- Clone GitHub Repository
- Build Docker Image
- Run Docker Container
- Access Application via Public IP

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/SHREYASKURANE/ICU_MLOps_Project.git
```

Move inside the project

```bash
cd ICU_MLOps_Project
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

Run preprocessing

```bash
python src/preprocess.py
```

Train model

```bash
python src/train.py
```

Run MLflow

```bash
mlflow ui
```

Open

```
http://127.0.0.1:5000
```

Run Streamlit

```bash
streamlit run app/streamlit_app.py
```

---

# 📷 Screenshots

Add screenshots for:

- Dataset
- EDA
- MLflow
- Docker Container
- Jenkins Dashboard
- AWS Deployment
- Streamlit Application

---

# 📌 Future Scope

- Deep Learning Models
- Real-Time ICU Monitoring
- Continuous Model Retraining
- Kubernetes Deployment
- CI/CD Pipeline
- Model Monitoring
- Drift Detection

---

# 👨‍💻 Author

**Shreyas Kurane**

Computer Science & Engineering (AI)

DevOps & MLOps Project

---

# 📜 License

This project is developed for educational and learning purposes.


git 