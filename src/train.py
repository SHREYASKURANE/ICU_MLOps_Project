import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from config import (
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    MODEL_PATH,
    MLFLOW_EXPERIMENT,
)

train = pd.read_csv(TRAIN_DATA_PATH)
test = pd.read_csv(TEST_DATA_PATH)

X_train = train.drop("Survive", axis=1)
y_train = train["Survive"]

X_test = test.drop("Survive", axis=1)
y_test = test["Survive"]

mlflow.set_experiment(MLFLOW_EXPERIMENT)

with mlflow.start_run():

    model = LogisticRegression(random_state=42)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    mlflow.log_param("Model", "LogisticRegression")

    mlflow.log_metric("Accuracy", accuracy)

    mlflow.sklearn.log_model(model, "LogisticRegression")

    joblib.dump(model, MODEL_PATH)

    print("Model Trained Successfully")

    print("Accuracy:", accuracy)